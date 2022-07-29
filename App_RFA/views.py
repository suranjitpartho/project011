from django.shortcuts import render, redirect
from django.contrib import messages
from App_RFA.models import Monthly, Target
from App_RFA.resources import MonthlyResource, TargetResource
from tablib import Dataset
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required
def MonthlyUpload(request):
    if request.method == 'POST':
        monthly_resource = MonthlyResource()
        dataset = Dataset()
        new_monthlydata = request.FILES['myfile']
        if not new_monthlydata.name.endswith('xlsx'):
            messages.info(request, 'File must be in xlsx format')
            return render(request, 'App_RFA/monthlyupload.html')
        imported_data = dataset.load(new_monthlydata.read(), format='xlsx')
        for data in imported_data:
            value = Monthly(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6],
                data[7], data[8], data[9], data[10], data[11], data[12], data[13],
                data[14], data[15], data[16], data[17], data[18], data[19]
                )
            value.save()
        return redirect('App_RFA:datasuccess')
    return render(request, 'App_RFA/monthlyupload.html')


@login_required
def TargetUpload(request):
    if request.method == 'POST':
        target_resource = TargetResource()
        dataset = Dataset()
        new_targetdata = request.FILES['myfile']
        if not new_targetdata.name.endswith('xlsx'):
            messages.info(request, 'File must be in xlsx format')
            return render(request, 'App_RFA/targetupload.html')
        imported_data = dataset.load(new_targetdata.read(), format='xlsx')
        for data in imported_data:
            value = Target(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6],
                data[7], data[8], data[9], data[10], data[11], data[12]
                )
            value.save()
        return redirect('App_RFA:datasuccess')
    return render(request, 'App_RFA/targetupload.html')




@login_required
def DataSuccess(request):
    return render(request, 'App_RFA/datasuccess.html')

@login_required
def RFADashboard(request):
    return render(request, 'App_RFA/rfa_dashboard.html')

@login_required
def RFATemplateDownload(request):
    return render(request, 'App_RFA/templatedownload.html')
