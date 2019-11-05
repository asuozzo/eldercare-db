from django.core.management.base import BaseCommand
from eldercare.models import Facility
from django.db.models import Sum



class Command(BaseCommand):

    def handle(self, *args, **options):
        facilities = Facility.objects.all()
        for facility in facilities:
            citation_score = facility.citation_set.all().aggregate(Sum('severity_scope__score'))
            score = int_or_zero(citation_score["severity_scope__score__sum"])
            facility.score = score
            facility.save()


def int_or_zero(score):
    if not score:
        return 0
    return score