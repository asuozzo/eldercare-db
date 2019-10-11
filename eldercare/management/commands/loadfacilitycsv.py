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
                    care_type=get_care_type(row['Type']),
                    id_num=row["ID"],
                    capacity=get_capacity(row["RCF - Capacity"], row["ALR - Max Occupancy"]),
                    level=row["RCF - Level"],
                    address=row["Address"],
                    town=row["Town"],
                    county=row["County"]
                )


def get_care_type(care_type):
    if care_type == "Residential Care Facility":
        care_type = "RCF"
    else:
        care_type = "ALR"

    return care_type

def get_capacity(rcf_capacity, alr_capacity):
    if rcf_capacity == "":
        if alr_capacity != "":
            return alr_capacity
        else:
            return None
    elif alr_capacity == "":
        return rcf_capacity

def get_level(rcf_level):
    if rcf_level == "":
        return None
    else:
        return rcf_level