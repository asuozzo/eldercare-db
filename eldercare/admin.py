from django.contrib import admin

from .models import Facility, Inspection, Allegation, Complaint, Penalty


# Register your models here.
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'care_type', 'capacity', 'town', 'county')
    search_fields = ('name',)

admin.site.register(Facility, FacilityAdmin)

class InspectionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'facility', 'inspection_type', 'date')
    search_fields = ('facility__name', 'inspection_type', 'date', 'documentcloud_url')

admin.site.register(Inspection, InspectionAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'facility', 'received_start_date')
    search_fields = ('intake_id','facility__name', 'received_start_date')

admin.site.register(Complaint, ComplaintAdmin)

class AllegationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'facility', 'substantiation','finding', 'seriousness')


admin.site.register(Allegation, AllegationAdmin)

class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'penalty')

admin.site.register(Penalty, PenaltyAdmin)