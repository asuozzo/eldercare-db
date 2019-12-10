from django.shortcuts import get_object_or_404, render
from django.db.models import Sum, Func, Count
from django.core.serializers.json import DjangoJSONEncoder
import json
import pandas as pd
from django.db import models
from bakery.views import BuildableDetailView, BuildableListView, BuildableTemplateView

from .models import Facility, Complaint

class FacilityListView(BuildableListView):
    model = Facility

    ## vue template
    template_name = 'eldercare/index.html'
    context_object_name = 'facilities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        facilities = context['facilities']
        facilities_json = []
        for facility in facilities:
            facility_dict = {
                "name":facility.name,
                "lat":facility.lat,
                "lon":facility.lon,
                "address":facility.address,
                "id":facility.id,
                "capacity":facility.capacity,
                "type":facility.care_type,
                "town":facility.town,
                "status":facility.in_business,
                "county":facility.county,
                "slug":facility.slug
            }
            facilities_json.append(facility_dict)
        context["facilities_json"] = json.dumps(facilities_json,cls=DjangoJSONEncoder)

        return context


class FacilityDetailView(BuildableDetailView):
    model = Facility
    template_name = 'eldercare/detail.html'
    context_object_name = 'facility'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        facility = context['facility']
        context["inspections"] = facility.inspection_set.all()
        context["scores"] = list(Facility.objects.values_list('score', flat=True))
        citation_summary = facility.citation_set.annotate(year=Year('inspection__date')).values('year','severity_scope__letter').annotate(Count('severity_scope__letter'))
        citations_dict = citations_to_df(citation_summary)
        context["citation_type_json"] = citations_dict
        citation_totals = facility.citation_set.annotate(year=Year('inspection__date')).values('year').annotate(Count('severity_scope'))
        context["citation_json"] = json.dumps(list(citation_totals), cls=DjangoJSONEncoder)
        context["complaints_count"] = facility.allegation_set.count()
        context["substantiated_count"] = facility.allegation_set.filter(substantiation="Substantiated").count()
        context["tot_penalties"] = num_or_zero(facility.penalty_set.aggregate(Sum('penalty'))['penalty__sum'])
        return context


class Year(Func):
    function = "EXTRACT"
    template = '%(function)s(YEAR from %(expressions)s)'
    output_field = models.IntegerField()

def num_or_zero(num):
    if num == None:
        return 0
    return num

def citations_to_df(citation_summary):
    try:
        severity_code = {
            "A":1,
            "B":1,
            "C":1,
            "D":2,
            "E":2,
            "F":2,
            "G":3,
            "H":3,
            "I":3,
            "J":4,
            "K":4,
            "L":4
        }
        citations = pd.DataFrame(citation_summary)
        citations.rename(columns={"severity_scope__letter__count":"count"}, inplace=True)
        citations["severity_code"] = citations["severity_scope__letter"].map(severity_code)
        citations = citations[["year","severity_code","count"]]
        citations = citations.groupby(["year","severity_code"]).sum().reset_index()

        return json.dumps(citations.to_dict("records"))
    except KeyError:
        return json.dumps({})