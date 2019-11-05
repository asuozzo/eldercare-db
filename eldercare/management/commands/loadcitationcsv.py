from django.core.management.base import BaseCommand
from eldercare.models import Facility, Inspection, Citation, Severity_Scope
import csv
from django.utils.text import slugify
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):

        print("Loading CSV")
        csv_path = "static/citations.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            try:
                facility = Facility.objects.get(name=row["Facility"])
                inspection_type = row["Inspection Type"]
                date = datetime.strptime(row["Date"],"%m/%d/%Y")
                date = datetime.strftime(date, "%m-%d-%Y")
                slug_string = facility.name + date + inspection_type
                slug = slugify(slug_string, allow_unicode=True)

                inspection = Inspection.objects.filter(slug=slug)[0]
                citation_num = row["Citation"]
                if Severity_Scope.objects.filter(letter=row["SS"]).exists():
                    severity_scope = Severity_Scope.objects.get(letter=row["SS"])
                else:
                    severity_scope = None

                if Citation.objects.filter(inspection=inspection,citation_num=citation_num).exists():
                    pass
                    # print("skipping, {0} - {1} already exists".format(slug, citation_num))
                else:
                    citation = Citation.objects.create(
                        facility=facility,
                        inspection=inspection,
                        citation_num=citation_num,
                        severity_scope=severity_scope,
                        citation_type=row["Citation Type"],
                        citation_subtype=row["Citation Subtype"]
                    )
            except Exception as e:
                print(e)
                print("failed on {0} {1}".format(row["Inspection"], row["Citation"]))

