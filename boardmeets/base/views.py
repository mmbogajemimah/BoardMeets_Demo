from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Organization, Leader, License
from .forms import OrganizationForm, LeaderForm, ContactForm, SocialForm, LicenseForm

# ORGANIZATIONS VIEW FUNCTIONS
# Create your views here.
def index(request):
    return render(request, 'base/home.html')
    # return HttpResponse("Hello There. You are at the Board Meets Landing Page")

def organization_list(request):
    organizations = Organization.objects.all()
    context = {'organizations': organizations}
    return render(request, 'base/organizations_list.html', context)
    # return render(request, 'base/organizations_list.html')

#Counts the number of organizations in Organizations Model
def organization_number(request):
    organizations = Organization.objects.all()
    organizations_count = organizations.count()
    return render(request, 'base/home.html', {'organizations_count': organizations_count})

# Logic for displaying organizations details
def organization_detail(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    return render(request, 'base/organization_detail.html', {'organization': organization})

# Adding an Organization
def add_organization(request):
    if request.method == "POST":
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizations_list')
    else:
        form = OrganizationForm()
    return render(request, 'base/add_organization.html', {'form': form})
        
#Editing Organization Details
def edit_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)

    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organization_detail', pk=organization.pk)
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'base/edit_organization.html', {'form': form})

# DEleting An Organization from the Model
def delete_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)

    if request.method == "POST":
        organization.delete()
        return redirect('organizations_list')
    return render(request, 'base/delete_organization.html', {'organization': organization})


# ORGANIZATIONS_SOCIAL VIEW FUNCTIONS
def organizations_socials(request):
    organizations = Organization.objects.all()
    context = {'organizations': organizations}
    return render(request, 'base/organizations_socials.html', context)

#Edit Socials
def edit_socials(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)

    if request.method == "POST":
        form = SocialForm(request.POST, instance=organization)
        if form.is_valid():
            organization = form.save()
            return redirect('organizations_socials')
    else:
        form = SocialForm(instance=organization)
    return render(request, 'base/edit_socials.html', {'form': form, 'organization': organization})


# LEADER : ORGANIZATIONS_LEADERS
def organizations_names(request):
    organizations = Organization.objects.all()
    context = {'organizations': organizations}
    return render(request, 'base/organization_names.html', context)


def organization_leaders(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    organization_leaders = Leader.objects.filter(organization=organization)

    context = {
        'organization': organization,
        'leaders': organization_leaders
    }

    return render(request, 'base/organization_leaders.html', context)

#editing a leader
def edit_leader(request, organization_id, leader_id):
    leader = get_object_or_404(Leader, id=leader_id)

    if request.method == "POST":
        form = LeaderForm(request.POST, instance=leader)
        if form.is_valid():
            form.save()
            # Redirect to the leaders page
            return redirect('organization_leaders', organization_id=organization_id)
    else:
        form = LeaderForm(instance=leader)

    return render(request, 'base/edit_leader.html', {'form': form, 'leader': leader})

def delete_leader(request, organization_id, leader_id):
    leader = get_object_or_404(Leader, id=leader_id)

    if request.method == "POST":
        leader.delete()
        #Redirect
        return redirect('organization_leaders', organization_id=organization_id)
    return render(request, 'base/delete_leader.html', {'leader': leader, 'organization_id': organization_id})

#Add a new leader
def add_leader(request, organization_id):
    if request.method == "POST":
        form = LeaderForm(request.POST)
        if form.is_valid():
            leader = form.save(commit = False)
            leader.organization_id = organization_id
            leader.save()
            return redirect('organization_leaders', organization_id=organization_id)
    else:
        form = LeaderForm()

    return render(request, 'base/add_leader.html', {'form': form, 'organization_id': organization_id})


# ORGANIZATION CONTACTS
# A list of all organizations 

def organizations_contacts(request):
    organizations = Organization.objects.all()
    context = {'organizations': organizations}
    return render(request, 'base/organization_contacts.html', context)

# Adds a new contact on the contacts list
def add_contact(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.cleaned_data.get('phone_number')
            existing_contacts = organization.phone_number
            if existing_contacts:
                organization.phone_number = f"{existing_contacts}, {new_contact}"
            else:
                organization.phone_number = new_contact
            organization.save()
            return redirect('organizations_contacts')
    else:
        form = ContactForm()

    return render(request, 'base/add_contact.html', {'form': form, 'organization': organization})


def edit_contact(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data.get('phone_number')
            organization.phone_number = contact
            organization.save()
            return redirect('organizations_contacts')
    else:
        form = ContactForm(instance=organization)

    return render(request, 'base/edit_contact.html', {'form': form, 'organization': organization})

from django.contrib import messages

def delete_contact(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)

    if request.method == "POST":
        contact_to_delete = request.POST.get('contact')
        existing_contacts = organization.phone_number

        if existing_contacts and contact_to_delete in existing_contacts:
            # Remove the contact from the existing contacts
            updated_contacts = existing_contacts.replace(contact_to_delete, '').strip(', ')
            organization.phone_number = updated_contacts
            organization.save()
            messages.success(request, 'Contact deleted successfully.')

    return redirect('organizations_contacts')

# LICENSE
def license_list(request):
    licenses = License.objects.all()
    return render(request, 'base/license_list.html', {'licenses': licenses})

def current_users(request):
    licenses = License.objects.all()
    return render(request, 'base/current_users.html', {'licenses':licenses})

#Adding a license
def add_license(request):
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('license_body')
    else:
        form = LicenseForm()

    context = {'form': form}
    return render(request, 'base/add_license.html', context)

def edit_license(request, license_id):
    license = get_object_or_404(License, id=license_id)
    if request.method =='POST':
        form = LicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            # Redirect to the license page
            return redirect('license_body')
    else:
        form = LicenseForm(instance=license)

    return render(request, 'base/edit_license.html', {'form': form, 'license': license})

def delete_license(request):
    pass