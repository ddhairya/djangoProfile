from django.db import models


# Create your models here.


class userprofile(models.Model):

    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    profile_pic = models.CharField(max_length=250 , blank=True)
    emai = models.CharField(max_length=69)


# test model to get hands on
class Offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=69)
    discount = models.FloatField(max_length=5)

