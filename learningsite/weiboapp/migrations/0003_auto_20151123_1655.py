# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weiboapp', '0002_auto_20151119_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibo',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'post_time'),
        ),
        migrations.AddField(
            model_name='weibo',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name=b'update_time'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='context',
            field=models.CharField(max_length=1024, verbose_name=b'weibo_content'),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='weiboid',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'weibo_id', blank=True),
        ),
    ]
