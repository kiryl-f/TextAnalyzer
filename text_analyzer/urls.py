"""text_analyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from analyzer.views import data, hello, form, delete_text
from analyzer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin', admin.site.urls),
                  path('path', data, name='data'),
                  path('', hello, name='home'),
                  path('form', form, name='form'),
                  path('delete_text/<title>', delete_text, name='delete'),
                  path('delete_all', views.delete_all_texts, name='delete_all')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
