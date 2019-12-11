from django.urls import path
from django.views.generic import TemplateView

from eldercare.views import (
    FacilityListView,
    FacilityDetailView,
    BuildSite, PublishSite
)

urlpatterns = [
    path('build/', BuildSite, name='buildsite'),
    path('publish/', PublishSite, name='publishsite'),
    path('', FacilityListView.as_view(), name='index'),
    path('<str:slug>/', FacilityDetailView.as_view(), name='detail'),
]