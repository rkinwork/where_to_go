import argparse
import os
import logging
from io import BytesIO

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.core.management.base import CommandError
import requests
from jsonschema import validate

from places.models import Place, Image

PLACE_SCHEMA = {
    'type': 'object',
    'definitions': {
        'coordinates': {
            'type': 'object',
            'properties': {
                'lng': {
                    'type': 'string',
                    'pattern': r'^[\d\.]+$',
                },
                'lat': {
                    'type': 'string',
                    'pattern': r'^[\d\.]+$',
                },
            },
            'required': [
                'lng',
                'lat',
            ]
        }
    },
    'properties': {
        'title': {'type': 'string'},
        'imgs': {
            'type': 'array',
            'items': {"format": "uri", "pattern": "^https?://"},
        },
        'description_short': {'type': 'string'},
        'description_long': {'type': 'string'},
        'coordinates': {'$ref': '#/definitions/coordinates'},

    },
    'required': [
        'title',
        'imgs',
        'description_short',
        'description_long',
        'coordinates',
    ]
}


class URLType:
    def __call__(self, value: str):
        try:
            URLValidator()(value)
        except ValidationError as e:
            raise argparse.ArgumentTypeError(e.message)
        return value


def load_place_error_wrapper(fnc):
    def wrapper(url: str):
        try:
            fnc(url)
        except requests.HTTPError as e:
            raise CommandError(f'problems with loading {url}, {e}')
        except ValueError as e:
            raise CommandError(f"can't decode json from {url} {e}")

    return wrapper


@load_place_error_wrapper
def load_place_from_url(url: str):
    res = requests.get(url)
    res.raise_for_status()
    parsed_place = res.json()
    validate(parsed_place, PLACE_SCHEMA)
    place, created = Place.objects.get_or_create(
        title=parsed_place['title'],
        defaults={
            'description_short': parsed_place['description_short'],
            'description_long': parsed_place['description_long'],
            'long': parsed_place['coordinates']['lng'],
            'lat': parsed_place['coordinates']['lat']

        }
    )
    if not created:
        return

    for img_url in parsed_place['imgs']:
        filename = os.path.basename(img_url)
        img, created = Image.objects.get_or_create(
            place=place,
            image=filename,
        )
        if not created:
            continue

        res = requests.get(img_url)
        if not res.ok:
            logging.info(
                f'problems with downloading {img_url} for {place.title}'
            )
            continue
        img_bin = BytesIO(res.content)
        img_bin.seek(0)
        img.image.save(name=filename,
                       content=ImageFile(img_bin),
                       save=True)
