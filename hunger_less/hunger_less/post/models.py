from django.db import models
from django.conf import settings

class foodtype(models.Model):
    name = models.CharField(db_index=True,max_length=200)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class post(models.Model):
    date = models.DateTimeField(blank=False, null=False, verbose_name='Post Date')
    collectdate = models.DateTimeField(blank=False, null=False, verbose_name='Collect By Date') 
    address = models.CharField( max_length=300, blank=False, null=False)
    description = models.CharField( max_length=300, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    foodtype = models.ForeignKey(foodtype, on_delete=models.CASCADE)
    quantity = models.IntegerField( blank=False, null=False)
    quality = models.CharField(max_length=300, blank=True, null=True)
    
    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
        
class postlink(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    foodtype = models.ForeignKey(foodtype, on_delete=models.CASCADE)
    quantity = models.IntegerField( blank=False, null=False)
    quality = models.CharField(max_length=300, blank=True, null=True)

