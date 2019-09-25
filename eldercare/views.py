from django.shortcuts import get_object_or_404, render

from .models import Facility, Complaint
from .tables import FacilityTable

def index(request):
    facility_list = Facility.objects.order_by('name')
    table = FacilityTable(facility_list)
    context = {"table":table}
    return render(request, 'eldercare/index.html', context)


def facility_detail(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    complaints = facility.complaint_set.all()
    inspections = facility.inspection_set.all()
    return render(request, 'eldercare/detail.html', {
        "facility":facility,
        "complaints":complaints,
        "inspections":inspections
        })