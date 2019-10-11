from django.shortcuts import get_object_or_404, render
from django.db.models import Sum
from bakery.views import BuildableDetailView, BuildableListView

from .models import Facility, Complaint

class FacilityListView(BuildableListView):
    model = Facility
    # queryset = Facility.objects.all()
    template_name = 'eldercare/index.html'
    

class FacilityDetailView(BuildableDetailView):
    model = Facility
    template_name = 'eldercare/detail.html'
    context_object_name = 'facility'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        facility = context['facility']
        context["inspections"] = facility.inspection_set.all()
        context["complaints"] = facility.complaint_set.all()
        context["tot_penalties"] = num_or_zero(facility.penalty_set.aggregate(Sum('penalty'))['penalty__sum'])
        print(context["tot_penalties"])
        return context
        
        # print(facility)
        # print(facility.penalty_set.aggregate(Sum('penalty'))['penalty__sum'])

    #     context = super().get_context_data(**kwargs)
    #     context["tot_penalties"] = 20000
        # context["tot_penalties"] = num_or_zero(self.object.penalty_set.aggregate(Sum('penalty'))['penalty__sum'])
    # facility = get_object_or_404(Facility, pk=facility_id)
    # complaints = facility.complaint_set.all()
    # inspections = facility.inspection_set.all()
    # tot_penalties = num_or_zero(facility.penalty_set.aggregate(Sum('penalty'))['penalty__sum'])
    # return render(request, 'eldercare/detail.html', {
    #     "facility":facility,
    #     "complaints":complaints,
    #     "inspections":inspections,
    #     "tot_penalties":tot_penalties
    #     })


def num_or_zero(num):
    if num == None:
        return 0
    return num