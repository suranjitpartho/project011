
## PROJECT URL CONFIGURATION

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('App_Dash.urls')),
    path('rfa/', include('App_RFA.urls')),
]
