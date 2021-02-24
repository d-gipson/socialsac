import os, io, json
from django.core.management.base import BaseCommand, CommandError
from app.models import Freedge, Shelter

from pprint import pprint

class Command(BaseCommand):

    help = 'runs the ingest cycle on jsons in the ingest folder'

    def handle(self, *args, **options):
        ingestFolder = r'./core/static/ingest/'
        ingests = os.scandir(ingestFolder)

        for f in ingests:
            file = io.open(f.path, 'r', encoding='utf-8-sig')
            data = json.load(file)
            if 'food' in f.name:
                for entry in data:
                    print(entry)
                    record = Freedge(
                        name = entry['Title'],
                        address = entry['StreetAddress'],
                        location = entry['StreetAddress'],
                        availability = 'y',
                        phone = entry['PhoneNumber'],
                        date_updated = ''
                    )
                    print(record)

            if 'shelter' in f.name:
                for entry in data:
                    print(entry)
                    record = Shelter(
                                    name = entry['Title'],
                                    address = entry['StreetAddress'],
                                    location = entry['StreetAddress'],
                                    availability = 'y',
                                    date_updated = ''
                                )
                    print(record)
