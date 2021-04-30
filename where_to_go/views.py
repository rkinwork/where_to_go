from django.shortcuts import render
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


def show_index(request):
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": [generate_feature(place) for place in places]
    }

    data = {'places_geojson': places_geojson}
    return render(request, "index.html", context=data)
