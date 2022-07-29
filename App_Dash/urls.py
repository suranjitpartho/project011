from django.urls import path
from App_Dash import views

app_name = 'App_Dash'

urlpatterns = [
    path('monthlydata/', views.monthlydata, name='monthlydata'),
    path('', views.servicemapping, name='servicemapping'),
    path('health/', views.health, name='health'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('shelter/', views.shelter, name='shelter'),
]