from django.db import models
from django.utils import timezone


# Create your models here.

class Weibo(models.Model):
    weibo_id = models.CharField('weibo_id', max_length=30, blank=True, default='')
    context = models.CharField('context', max_length=1024)

    pub_date = models.DateTimeField('post_time', editable=True, default=timezone.now)
    update_time = models.DateTimeField('update_time', null=True, default=timezone.now)

    # return the context of the weibo
    def __unicode__(self):
        return self.weibo_id
