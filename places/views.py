from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Location


def index(request):
    locations = Location.objects.all()
    places = {
        "type": "FeatureCollection",
        "features": []
    }
    for location in locations:
        places['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat]
            },
            "properties": {
                "title": location.title,
                "placeId": location.id,
                "detailsUrl": reverse(
                    'place_detail', kwargs={'place_id': location.id}
                    )
            }
        })
    places_geojson = {
        'places': places
    }
    return render(request, 'index.html', context=places_geojson)


def place_detail(request, place_id):
    place = get_object_or_404(Location, pk=place_id)
    images = [img.image.url for img in place.imgs.all()]
    place_json = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(
        place_json, safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
        )
