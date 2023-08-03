from django.urls import include, path
from rest_framework import routers
from jamming import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jamming.urls')), # Replace 'music' with your app name
]
