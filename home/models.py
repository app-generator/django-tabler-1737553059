# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    dummy field name = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dummy Model Name(models.Model):

    #__Dummy Model Name_FIELDS__
    dummy field name = models.CharField(max_length=255, null=True, blank=True)

    #__Dummy Model Name_FIELDS__END

    class Meta:
        verbose_name        = _("Dummy Model Name")
        verbose_name_plural = _("Dummy Model Name")



#__MODELS__END
