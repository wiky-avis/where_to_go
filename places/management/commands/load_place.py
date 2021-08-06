import json
import os
from io import BytesIO

import requests
from django.core.management.base import BaseCommand

from places.models import Location
from where_to_go.settings import LOAD_ROOT


def upload_imgs(location, urls):
    for num, url in enumerate(urls, 0):
        response = requests.get(url)
        response.raise_for_status()
        img = BytesIO(response.content)
        img_name = os.path.basename(url)
        image, created = location.imgs.get_or_create(
            location=location.id, order=num
            )
        image.image.save(img_name, img, save=True)


class Command(BaseCommand):
    def handle(self, *args, **options):
        os.chdir(LOAD_ROOT)
        for file in os.listdir("."):
            with open(file, 'r', encoding='utf-8') as f:
                serialized_location = json.load(f)
            location, created = Location.objects.update_or_create(
                title=serialized_location['title'],
                lng=serialized_location['coordinates']['lng'],
                lat=serialized_location['coordinates']['lat'],
                defaults={
                    'description_short': serialized_location[
                        'description_short'
                        ],
                    'description_long': serialized_location[
                        'description_long'
                        ],
                    }
                )
            upload_imgs(location, serialized_location['imgs'])
