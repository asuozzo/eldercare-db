import django_tables2 as tables
from django_tables2.utils import A

from .models import Facility


class FacilityTable(tables.Table):
    name = tables.LinkColumn(
        'facility_detail',
        text=lambda record: record.name, args=[A('pk')],
        verbose_name="Facility")

    class Meta:
        model = Facility
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", 'care_type','town','county','capacity')