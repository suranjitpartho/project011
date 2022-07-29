from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# VIEWS:

@login_required
def monthlydata(request):
    return render(request, 'App_Dash/monthlydata.html')

@login_required
def servicemapping(request):
    return render(request, 'App_Dash/servicemapping.html')

@login_required
def health(request):
    return render(request, 'App_Dash/health.html')

@login_required
def nutrition(request):
    return render(request, 'App_Dash/nutrition.html')

@login_required
def shelter(request):
    return render(request, 'App_Dash/shelter.html')

