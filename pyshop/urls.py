"""pyshop URL Configuration

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
from django.urls import path, include
# need to define the static file so django can use it
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# it will direct where the media url is to the django
from django.conf.urls.static import static
# this will import all the variable we created in the setting file
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # we link our app/ package to the main app.
    # passing the urls to our userprofile app urls handler whenever there is 'profile/'
    path('profile/', include('userprofile.urls'))
]


# adding static files
urlpatterns += staticfiles_urlpatterns()
# adding media URLs , so that they can be accessible.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)