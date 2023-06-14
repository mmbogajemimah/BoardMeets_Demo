from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("organizations/", views.organization_list, name='organizations_list'),
    path("organizations/add", views.add_organization, name='add_organization'),
    path("organizations/<int:pk>/", views.organization_detail, name='organization_detail'),
    path("organizations/<int:pk>/edit/", views.edit_organization, name="edit_organization"),
    path("organizations/<int:pk>/delete/", views.delete_organization, name='delete_organization'),
    path("organizations/socials", views.organizations_socials, name='organizations_socials'),
    path("organization-names/", views.organizations_names, name='organization_names'),
    path("organization-leaders/<int:organization_id>/", views.organization_leaders, name='organization_leaders'),
]
