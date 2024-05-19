"""
URL configuration for real_estate project.

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
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("propertytype/", views.propertytype, name="propertytype"),
    path("propertylist/", views.propertylist, name="propertylist"),
    path("propertyagent/", views.propertyagent, name="propertyagent"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("404/", views.custom_404, name="404"),
    path("__reload__/", include("django_browser_reload.urls")),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", views.profile, name="profile",),
    path("accounts/login/", views.login, name="login",)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.custom_404'