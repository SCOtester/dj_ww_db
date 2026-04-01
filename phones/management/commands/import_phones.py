import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.update_or_create(
                id=int(phone['id']),
                defaults={
                    'name': phone['name'],
                    'image': phone['image'],
                    'price': int(phone['price']),
                    'release_date': datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                    'lte_exists': phone['lte_exists'] == 'True',
                }
            )