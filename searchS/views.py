from django.shortcuts import render
from django.http import JsonResponse
from .models import Hospital
from .models import Medicine


def search_results(request):
    location = request.POST.get('location')
    test = request.POST.get('test')
    
    if test:
        hospitals = Hospital.objects.filter(location=location, tests__icontains=test)
    else:
        hospitals = Hospital.objects.filter(location=location)
    return render(request, 'search_results.html', {'hospitals': hospitals})

def autocomplete_search(request): 
    term = request.GET.get('term')
    if term:
        # Query the tests field of Hospital model for matching test names
        tests = Hospital.objects.filter(tests__icontains=term).values_list('tests', flat=True).distinct()
        suggestions = list(tests)
    else:  
        suggestions = []
    return JsonResponse(suggestions, safe=False)

def med_results(request):
    location = request.POST.get('location')
    test = request.POST.get('test')
    
    if test:
        medicines = Medicine.objects.filter(location=location, medicine__icontains=test)
    else:
        medicines = Medicine.objects.filter(location=location)
    return render(request, 'med_results.html', {'medicines': medicines})

def auto_search(request):
    term = request.GET.get('term')
    if term:
        # Query the medicine field of Medicine model for matching medicine names
        medicines = Medicine.objects.filter(medicine__icontains=term).values_list('medicine', flat=True).distinct()
        suggestions = list(medicines)
    else:
        suggestions = []
    return JsonResponse(suggestions, safe=False)

