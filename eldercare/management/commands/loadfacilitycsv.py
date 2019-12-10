from django.core.management.base import BaseCommand
from eldercare.models import Facility
import csv
from datetime import datetime

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
                    capacity=get_capacity(row["RCH - Capacity"], row["ALR - Max Occupancy"]),
                    level=get_level(row["RCH - Level"]),
                    address=row["Address"],
                    town=row["Town"],
                    in_business=get_status(row["In business"]),
                    county=row["County"],
                    opendate=get_date(row["Open date"]),
                    closedate=get_date(row["Close date"]),
                    formername=get_formername(row["Other/Former Names"]),
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

def get_status(status):
    if status=="Open":
        return True
    else:
        return False

def get_date(date):
    if not date:
        return None
    else:
        return datetime.strptime(date, "%m/%d/%Y").date()

def get_formername(former_name):
    if not former_name:
        return None
    else:
        return former_name