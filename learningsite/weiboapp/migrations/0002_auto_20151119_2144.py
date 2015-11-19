# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weiboapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibo',
            name='weiboid',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='weibo',
            name='context',
            field=models.CharField(max_length=1024),
        ),
    ]
