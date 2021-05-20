from django.contrib import admin
# to extend our userprfile app in the admin pannel we need to import
from .models import userprofile, Offers
# Register your models here.


# create a class to pass as a argument to the admin register function. This will change the default list view with the given column.
class UserprofleAdmin(admin.ModelAdmin):
    list_display = ('f_name','l_name','emai', 'profile_pic')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')


# 'admin' object have attribute 'site' which have a function 'register' and we are passing our model to that
admin.site.register(userprofile, UserprofleAdmin)
admin.site.register(Offers, OfferAdmin)



