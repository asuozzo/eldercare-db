from django.db import models
from django.urls import reverse

# Create your models here.
class Facility(models.Model):

    class Meta:
        verbose_name_plural = "facilities"

    name = models.CharField(max_length=200)
    care_type = models.CharField(
        max_length=100
    )
    id_num = models.CharField(max_length=200,blank=True)
    capacity = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    in_business = models.BooleanField(blank=True, null=True)
    accs = models.BooleanField(default=False)
    erc = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    

class Inspection(models.Model):
    facility = models.ForeignKey(
        Facility,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    inspection_type = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True,null=True)
    documentcloud_url = models.URLField(blank=True, null=True)
    state_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.documentcloud_url
    #     return ("{0} - {1} {2}".format(self.facility.name, self.inspection_type, self.date))

class Complaint(models.Model):
    facility = models.ForeignKey(
        Facility,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    intake_id = models.CharField(
        max_length=200, unique=True, blank=True, null=True
    )
    received_start_date = models.DateField()

    related_inspection = models.ForeignKey(
        Inspection,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.intake_id

class Allegation(models.Model):
    facility = models.ForeignKey(
        Facility, on_delete=models.SET_NULL,
        blank=True, null=True
    )
    complaint = models.ForeignKey(
        Complaint, on_delete=models.SET_NULL,
        blank=True, null=True
    )
    allegation_num = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=300, blank=True, null=True)
    subcategory = models.CharField(max_length=300, blank=True, null=True)
    seriousness = models.CharField(max_length=300, blank=True, null=True)
    substantiation = models.CharField(max_length=300, blank=True, null=True)
    finding = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return ("{0}-{1}".format(self.complaint.intake_id, self.allegation_num))

class Penalty(models.Model):

    class Meta:
        verbose_name_plural = "penalties"

    facility = models.ForeignKey(
        Facility, on_delete=models.SET_NULL,
        blank=True, null=True
    )
    date = models.DateField()
    penalty = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return ("{0}-{1}".format(self.facility, self.date))
