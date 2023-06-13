from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Organization

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

def organization_detail(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    return render(request, 'base/organization_detail.html', {'organization': organization})