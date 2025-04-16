from django.shortcuts import render
from .pest_data import pests

def index(request):
    return render(request, 'app_assign1/index.html')

def about(request):
    return render(request, 'app_assign1/about.html')

def pest_list(request):
    return render(request, 'app_assign1/list.html', {'pests': pests})

def pest_details(request, pest_id):
    selected = next((p for p in pests if p.id == pest_id), None)
    return render(request, 'app_assign1/details.html', {'pest': selected})
