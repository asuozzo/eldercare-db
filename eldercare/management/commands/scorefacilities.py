from django.core.management.base import BaseCommand
from eldercare.models import Facility
from django.db.models import Sum
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


class Command(BaseCommand):

    def handle(self, *args, **options):
        facilities = Facility.objects.all()
        for facility in facilities:
            citation_score = facility.citation_set.all().aggregate(Sum('severity_scope__score'))
            score = int_or_zero(citation_score["severity_scope__score__sum"])
            years_open = get_years_open(facility.opendate, facility.closedate)
            facility.score = score/years_open
            facility.save()


def int_or_zero(score):
    if not score:
        return 0
    return score

def get_years_open(opendate, closedate):
    if not opendate:
        opendate = pd.to_datetime("1/1/14")
    else:
        opendate=pd.to_datetime(opendate)
    if not closedate:
        closedate = pd.to_datetime("9/30/19")
    else:
        closedate = pd.to_datetime(closedate)
    months = (closedate-opendate)/np.timedelta64(1, 'M')
    years = (months/12)
    if years < 1:
        years = 1

    return years