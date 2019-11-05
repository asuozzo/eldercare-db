from django.core.management.base import BaseCommand
from eldercare.models import Facility
import requests
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        key = 'AIzaSyBX11djWfV1cYyyV388n7-GUGoxxus3YNs'

        facilities = Facility.objects.all()
        for facility in facilities:
            if not facility.lat:
                address = "{0}, {1} VT".format(facility.address, facility.town)

                url = "https://maps.googleapis.com/maps/api/geocode/json"

                payload = {
                    "address":address,
                    "key":key
                }
                r = requests.get(url, params=payload)

                results = r.json()
                
                if results['status'] == "ZERO_RESULTS":
                    print("failed on {0}".format(facility.name))

                else:
                    latlng = results["results"][0]["geometry"]["location"]

                    facility.lat = latlng["lat"]
                    facility.lon = latlng["lng"]
                    facility.save()
            else:
                print("skipping {0}, already geocoded".format(facility.name))