# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productfeatured_make_image_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeatured',
            name='text_css_color',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
