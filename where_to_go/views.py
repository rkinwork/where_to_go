from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from places.models import Place


def generate_feature(place: Place) -> dict:
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.long, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
        }
    }


def generate_place_info(place: Place) -> dict:
    return {
        "title": place.title,
        "imgs": [image_instance.image.url for image_instance in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.long
        }
    }


def show_index(request):
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": [generate_feature(place) for place in places]
    }

    data = {'places_geojson': places_geojson}
    return render(request, "index.html", context=data)


def show_place(request, by_id):
    place_queryset = Place.objects.prefetch_related('images')
    place = get_object_or_404(place_queryset, pk=by_id)
    return JsonResponse(
        data=generate_place_info(place),
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        }
    )
