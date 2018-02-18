from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    BusinessTypes=(
        ('S','Supermarket'),
        ('F','Farm'),
        ('P','Produce Stall'),
        ('Pi','Private Individual'),
        ('Re','Restaurant'),
    )
    ContactName = models.CharField(_('Name of Contact Person'), blank=False, max_length=255)
    CompanyName = models.CharField(_('Name of Company'), blank=False, max_length=255)
    BusinessType = models.CharField(max_length=2,blank=False, choices=BusinessTypes)
    CompanyAddress = models.CharField(_('Business Address'), blank=False, max_length=255)
    OtherInfo = models.CharField(_('Other Info'), blank=True, max_length=255)



    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
