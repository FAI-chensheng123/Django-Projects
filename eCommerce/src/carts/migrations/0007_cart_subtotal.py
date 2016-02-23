# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_remove_cart_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=2.34, max_digits=50),
            preserve_default=False,
        ),
    ]
