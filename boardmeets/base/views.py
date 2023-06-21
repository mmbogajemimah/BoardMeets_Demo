from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Organization, Leader
from .forms import OrganizationForm, LeaderForm

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






















# def organizations_contacts(request):
#     organizations = Organization.objects.all()
#     context = {'organizations': organizations}
#     return render(request, 'base/organization_contacts.html', context)

# # Retriving organization's contact
# def contacts(request, organization_id):
#     organization = get_object_or_404(Organization, id=organization_id)
#     contacts = organization.phone_number
#     return render(request, 'base/contact.html', {'organization': organization, 'contacts': contacts})


# def organization_leaders(request):
#     organizations = Organization.objects.all()

#     context = {
#         'organizations': organizations
#     }

#     return render(request, 'organization_leaders.html', context)