"""appkantin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path
from makanan import views as makananView

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',makananView.home,name='home'),
    path('makanan/<int:makanan_id>', makananView.detail,name='detail'),
    path("about/", makananView.about , name="about")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
