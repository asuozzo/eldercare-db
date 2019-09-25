from django.core.management.base import BaseCommand
from eldercare.models import Facility, Inspection, Complaint, Allegation
from datetime import datetime
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "static/allegations.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            intake_id = row["Intake ID"]
            complaint = Complaint.objects.filter(intake_id=intake_id)
            # if complaint doesn't exist yet, add it
            if not complaint:
                print("adding complaint {0}".format(intake_id))
                facility = Facility.objects.get(name=row["Facility"])
                date = datetime.strptime(row["Received Start Date"], "%m/%d/%Y").date()

                complaint = Complaint.objects.create(
                    facility=facility,
                    intake_id=row["Intake ID"],
                    received_start_date=date,
                )
            else:
                complaint = complaint[0]
            
            # if the allegation doesn't have a number, don't add it to the database
            if row["Allegation No."] == "":
                print("Skipping complaint {0}, no allegations".format(intake_id))
            else:
                if Allegation.objects.filter(complaint=complaint,allegation_num=row["Allegation No."]).exists():
                    print("skipping{0} - {1}, already entered".format(row["Facility"], intake_id))
                else:
                    facility = complaint.facility
                    substantiation, finding = get_substantiation(row["Findings"])
                    allegation = Allegation.objects.create(
                        facility=facility,
                        complaint=complaint,
                        allegation_num=row["Allegation No."],
                        category=row["Category"],
                        subcategory=row["Subcategory"],
                        seriousness=row["Seriousness"],
                        substantiation=substantiation,
                        finding=finding
                    )

def get_substantiation(finding_text):
    if finding_text == "":
       return None, None

    elif (finding_text == "Blank") or (finding_text == "Redacted"):
       return finding_text, None

    else:
        substantiation, finding = finding_text.split(":")
        finding = finding.strip()
        return substantiation, finding