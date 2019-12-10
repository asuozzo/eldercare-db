from django.core.management.base import BaseCommand
from eldercare.models import Facility, Penalty
from datetime import datetime
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "static/penalties.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            facility = Facility.objects.get(name=row["Provider"])
            date = datetime.strptime(row["Date"],"%m/%d/%Y").date()
            penalty=float(row["\ufeffFee"].replace("$","").replace(",",""))
            penalty = Penalty.objects.create(
                facility=facility,
                date=date,
                penalty=penalty
            )