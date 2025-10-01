"""
URL configuration for Sipher_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
    path("admin/", admin.site.urls),
    path("dashboard/", include("apps.core.urls")),  # Include core app URLs
    path("dashboard/", include("apps.student_management.urls")),  # Add student management URLs
    path("dashboard/", include("apps.employee_management.urls")),
    path("dashboard/", include("apps.authentication.urls")),
    path("dashboard/", include("apps.inventory.urls")),
    path("dashboard/", include("apps.finance.urls")),
    path("dashboard/", include("apps.counsellor.urls")),
    path("dashboard/", include("apps.trainer_managment.urls")),
    path("", include("apps.website.urls")),
    path("dashboard/", include("apps.management.urls")),  # Include management app URLs
        # Add website URLs
]