from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("license-body/", views.license_list, name="license_body"),
    path("current-users/", views.current_users, name="current_users"),
    path("license-body/add-license/", views.add_license, name='add_license'),
     path("license-body/edit-license/<int:license_id>", views.edit_license, name='edit_license'),


    path("organizations/", views.organization_list, name='organizations_list'),
    path("organizations/add", views.add_organization, name='add_organization'),
    path("organizations/<int:pk>/", views.organization_detail, name='organization_detail'),
    path("organizations/<int:pk>/edit/", views.edit_organization, name="edit_organization"),
    path("organizations/<int:pk>/delete/", views.delete_organization, name='delete_organization'),
    path("organizations/socials", views.organizations_socials, name='organizations_socials'),
    path("organizations/socials/<int:organization_id>/edit", views.edit_socials, name='edit_socials'),
    path("organization-names/", views.organizations_names, name='organization_names'),
    path("organization-leaders/<int:organization_id>/", views.organization_leaders, name='organization_leaders'),
    path("organization-leaders/<int:organization_id>/<int:leader_id>/edit/", views.edit_leader, name='edit_leader'),
    path("organization-leaders/<int:organization_id>/<int:leader_id>/delete", views.delete_leader, name='delete_leader'),
    path("organization-leaders/<int:organization_id>/add", views.add_leader, name='add_leader'),
    path("organizations-contacts/", views.organizations_contacts, name='organizations_contacts'),
    path("organizations-contacts/<int:organization_id>/add/", views.add_contact, name='add_contact'),
    path("organizations-contacts/<int:organization_id>/edit/", views.edit_contact, name='edit_contact'),
    path("organizations-contacts/<int:organization_id>/delete/", views.delete_contact, name='delete_contact'),
    # path("organizations-contacts/<int:organization_id>/", views.contacts, name='contacts'),
    
    # path("organization-leaders/<int:organization_id>/<int:leader_id>/edit/", views.edit_leader, name='edit_leader'),
    
]
