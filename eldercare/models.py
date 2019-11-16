from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime

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
    opendate = models.DateField(blank=True, null=True)
    closedate = models.DateField(blank=True, null=True)
    formername = models.CharField(max_length=200,blank=True, null=True)

    score = models.IntegerField(default=0)

    lat = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)

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

    slug = models.SlugField(
        editable=False,
        default="",
        max_length=300,
    )
    
    inspection_type = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True,null=True)
    documentcloud_url = models.URLField(blank=True, null=True)
    state_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        value = self.facility.name + datetime.strftime(self.date,"%m-%d-%Y") + self.inspection_type
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
 
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

class Severity_Scope(models.Model):

    letter = models.CharField(max_length=1)
    score = models.IntegerField(default=0)
    severity = models.CharField(max_length=200,blank=True, null=True)
    severity_code = models.IntegerField(blank=True, null=True)
    scope = models.CharField(max_length=200,blank=True, null=True)
    scope_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (self.letter)

class Citation(models.Model):
    facility = models.ForeignKey(
        Facility,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    inspection = models.ForeignKey(
        Inspection,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    citation_num = models.CharField(max_length=20,blank=True, null=True)
    severity_scope = models.ForeignKey(Severity_Scope, on_delete=models.SET_NULL, blank=True, null=True)
    citation_type = models.CharField(max_length=200,blank=True, null=True)
    citation_subtype = models.CharField(max_length=200,blank=True, null=True)
   