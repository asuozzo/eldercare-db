from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:facility_id>/', views.facility_detail, name="facility_detail")
]