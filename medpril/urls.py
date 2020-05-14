"""medpril URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
path('ckeditor/', include('ckeditor_uploader.urls')),
path('', include('mains.urls',namespace='main')),
path('oncol/', include('oncol.urls')),
path('contact/', include('contacts.urls',)),
path('document/', include('documents.urls',)),
path('job/', include('job.urls',)),
path('drug/', include('drug.urls',)),
path('healthy/', include('healthy.urls',)),
path('histori/', include('histori.urls',)),
path('hospis/', include('hospis.urls',)),
path('patients/', include('patients_info.urls',)),
path('staff/', include('staff.urls',namespace='staff')),
path('manager/', include('staff.urls',namespace='manager')),
path('corruption/', include('corruption.urls')),
path('uporg/', include('up_org.urls')),
]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()