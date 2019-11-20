from django.core.management.base import BaseCommand
from eldercare.models import Facility
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "static/facilities.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:

            if Facility.objects.filter(name=row["\ufeffName"]).exists():
                print("skipping {0}, object exists".format(row["\ufeffName"]))
            else:
                print("adding {0}".format(row["\ufeffName"]))
                facility = Facility.objects.create(
                    name=row["\ufeffName"],
                    care_type=row['Type'],
                    id_num=row["ID"],
                    capacity=get_capacity(row["RCF - Capacity"], row["ALR - Max Occupancy"]),
                    level=get_level(row["RCF - Level"]),
                    address=row["Address"],
                    town=row["Town"],
                    county=row["County"]
                )

def get_capacity(rch_capacity, alr_capacity):
    if rch_capacity == "":
        if alr_capacity != "":
            return alr_capacity
        else:
            return None
    elif alr_capacity == "":
        return rch_capacity
    else:
        return 0

def get_level(rch_level):
    if rch_level == "":
        return None
    else:
        return rch_level