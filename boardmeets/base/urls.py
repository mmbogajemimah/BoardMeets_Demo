from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("organizations/", views.organization_list, name='org_list'),
]
