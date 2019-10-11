from django.core.management.base import BaseCommand
from eldercare.models import Facility, Inspection
from datetime import datetime
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "static/inspections.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            facility = Facility.objects.get(name=row["Facility"])
            date = datetime.strptime(row["survey date"], "%m/%d/%Y").date()
            if Inspection.objects.filter(facility=facility,date=date,documentcloud_url=row["documentcloud url"]).exists():
                print("skipping{0} - {1}".format(row["Facility"], row["survey date"]))
            else:
                print("adding {0} - {1}".format(row["Facility"], row["survey date"]))
                inspection = Inspection.objects.create(
                    facility=facility,
                    inspection_type=row["survey type"],
                    date=date,
                    documentcloud_url=row["documentcloud url"],
                    state_url=row["state url"]
                )