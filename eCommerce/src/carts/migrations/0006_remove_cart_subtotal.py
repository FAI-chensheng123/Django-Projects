# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-20 23:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_cart_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
    ]
