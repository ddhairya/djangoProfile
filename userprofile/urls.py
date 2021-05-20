from django.urls import path
# . (period) defines current directory
# This will import all the views and are ready to display for a specific URL
from . import views

# /profile/ is the default path define is our main project pyshop

urlpatterns = [
    # view index is called when default path is given i.e. /profile/
    path('', views.index),
    # view newprofiletest is called when path is given i.e. /profile/new/
    path('new/', views.newprofiletest)
]