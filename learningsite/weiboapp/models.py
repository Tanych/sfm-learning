from django.db import models


# Create your models here.

class Weibo(models.Model):
    weiboid = models.CharField(max_length=30,blank=True, default='')
    context = models.CharField(max_length=1024)

    # return the context of the weibo
    def __unicode__(self):
        return self.context
