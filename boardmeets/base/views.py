from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Organization
from .forms import OrganizationForm

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