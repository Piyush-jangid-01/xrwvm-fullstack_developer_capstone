from django.contrib import admin
from django.urls import path, include
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),  # IMPORTANT
    path('', views.home),
]