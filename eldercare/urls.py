from django.urls import path
from django.views.generic import TemplateView

from eldercare.views import (
    FacilityListView,
    FacilityDetailView
)

urlpatterns = [
    path('', FacilityListView.as_view(), name='index'),
    path('<int:pk>/', FacilityDetailView.as_view(), name='detail')
]