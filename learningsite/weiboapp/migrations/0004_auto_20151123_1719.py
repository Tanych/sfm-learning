# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weiboapp', '0003_auto_20151123_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weibo',
            old_name='weiboid',
            new_name='weibo_id',
        ),
        migrations.AlterField(
            model_name='weibo',
            name='context',
            field=models.CharField(max_length=1024, verbose_name=b'context'),
        ),
    ]
