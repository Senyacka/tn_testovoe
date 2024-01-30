"""
URL configuration for mvp_task3_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from azs_fuel.views import (FuelDetail,
                            FuelList,
                            AZSFuelList,
                            AZSFuelDetail,
                            )
from azs.views import (AZSList,
                       AZSDetail,
                       ServiceList,
                       ServiceDetail,
                       AZSServiceList,
                       AZSServiceDetail,
                       ImageList,
                       ImageDetail,
                       AZSImageList,
                       AZSImageDetail,
                       )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('azs/', AZSList.as_view(), name='azs-list'),
    path('azs/<int:pk>/', AZSDetail.as_view(), name='azs-detail'),
    path('fuel/', FuelList.as_view(), name='fuel-list'),
    path('fuel/<int:pk>/', FuelDetail.as_view(), name='fuel-detail'),
    path('azs/fuel/', AZSFuelList.as_view(), name='azs-fuel-list'),
    path('azs/fuel/<int:pk>/', AZSFuelDetail.as_view(), name='azs-fuel-detail'),
    path('service/', ServiceList.as_view(), name='service-list'),
    path('service/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
    path('azs/service/', AZSServiceList.as_view(), name='azs-service-list'),
    path('azs/service/<int:pk>/', AZSServiceDetail.as_view(), name='azs-service-detail'),
    path('image/', ImageList.as_view(), name='image-list'),
    path('image/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('azs/image/', AZSImageList.as_view(), name='azs-image-list'),
    path('azs/image/<int:pk>/', AZSImageDetail.as_view(), name='azs-image-detail'),
]
