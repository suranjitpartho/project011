from django.urls import path
from App_RFA.views import *
from App_RFA import views



app_name = 'App_RFA'


urlpatterns = [
    path('monthlyupload/', views.MonthlyUpload, name="monthlyupload"),
    path('targetupload/', views.TargetUpload, name="targetupload"),
    path('datasuccess/', views.DataSuccess, name="datasuccess"),
    path('rfadashboard/', views.RFADashboard, name="rfadashboard"),
    path('rfatempdownload/', views.RFATemplateDownload, name="rfatempdownload"),
]