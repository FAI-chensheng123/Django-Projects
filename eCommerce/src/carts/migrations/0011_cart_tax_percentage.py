# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-21 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20160221_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(decimal_places=5, default=0.062, max_digits=10),
        ),
    ]
