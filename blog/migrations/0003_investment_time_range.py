# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_investment_time_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='time_range',
            field=models.IntegerField(default=2, editable=False),
        ),
    ]
