from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("organizations/", views.organization_list, name='organizations_list'),
    path("organizations/<int:pk>/", views.organization_detail, name='organization_detail'),
]
