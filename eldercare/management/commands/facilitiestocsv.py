from django.core.management.base import BaseCommand
from eldercare.models import Facility
import csv
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):

        with open("static/facilities_geocoded.csv","w") as f:
            writer = csv.writer(f)
            headers = ["facility","type","town","in_business","lat","lon"]
            writer.writerow(headers)
            facilities = Facility.objects.all()
            for facility in facilities:
                writer.writerow([
                    facility.name,facility.care_type,facility.town,
                    facility.in_business,facility.lat,facility.lon
                    ])

