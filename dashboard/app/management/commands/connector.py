import os
import json
from django.core.management.base import BaseCommand, CommandError
from app.models import Freedge, Shelter

class Command(BaseCommand):

    help = 'runs the ingest cycle on jsons in the ingest folder'

    def handle(self, *args, **options):
        ingestFolder = r'./core/static/ingest/'
        ingests = os.scandir(ingestFolder)

        for file in ingests:
            #with open(file.path) as f:
            f = open(file.path, 'r')
            contents = f.read()
            data = json.loads(contents)
            if 'food' in f.name:
                for entry in data:
                    print(entry)
                    record = Freedge(
                                    name = entry['title'],
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
                                    name = entry['title'],
                                    address = entry['StreetAddress'],
                                    location = entry['StreetAddress'],
                                    availability = 'y',
                                    date_updated = ''
                                )
                    print(record)