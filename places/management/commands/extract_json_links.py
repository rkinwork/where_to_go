from urllib.parse import urljoin

from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests

from ._load_place import URLType, load_place_from_url

GITHUB_RAW_HOST = 'https://raw.githubusercontent.com/'


class Command(BaseCommand):
    help = 'Extract json links from github folder'

    def add_arguments(self, parser):
        parser.add_argument(
            'gh_url',
            help='Url from github containing json files',
            type=URLType())

    def handle(self, *args, **options):
        gh_url = options['gh_url']
        with requests.get(gh_url) as req:
            if not req.ok:
                raise CommandError(f'Problems with accessing {gh_url}')
            response_text = req.text

        soup = BeautifulSoup(response_text, 'lxml')
        links = soup.select('a[title$=".json"]')
        for extracted_link_tag in links:
            updated_url = extracted_link_tag['href'].replace('/blob', '')
            json_url = urljoin(
                GITHUB_RAW_HOST,
                str(updated_url),
            )
            self.stdout.write(json_url)
            load_place_from_url(json_url)
