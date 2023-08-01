"""
URL configuration for j_farm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('Jirani.urls')),
    path('jirani/', include('Jirani.urls')),
    path('jirani/register/', include('Jirani.urls')),
    path('jirani/login/', include('Jirani.urls')),
    path('jirani/logout/', include('Jirani.urls')),
    path('jirani/profile/', include('Jirani.urls')),
    path('jirani/tractors/', include('Jirani.urls')),
    path('jirani/tractors/<int:tractor_id>/', include('Jirani.urls')),
    path('jirani/tractors/add/', include('Jirani.urls')),
    path('jirani/tractors/edit/<int:tractor_id>/', include('Jirani.urls')),
    path('jirani/tractors/delete/<int:tractor_id>/', include('Jirani.urls')),
    path('jirani/leases/', include('Jirani.urls')),
    path('jirani/leases/<int:lease_id>/', include('Jirani.urls')),
    path('jirani/leases/create/<int:tractor_id>/', include('Jirani.urls')),
    path('jirani/leases/cancel/<int:lease_id>/', include('Jirani.urls')),
    path('jirani/leases/confirm/<int:lease_id>/', include('Jirani.urls')),
    path('jirani/leases/complete/<int:lease_id>/', include('Jirani.urls')),

]
