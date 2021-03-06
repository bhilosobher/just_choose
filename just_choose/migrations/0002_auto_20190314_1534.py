# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-14 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just_choose', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='allergy_warning',
            field=models.CharField(choices=[('nuts', 'nuts'), ('milk', 'milk'), ('gluten', 'gluten'), ('glu+mi', 'gluten,milk'), ('glu+nut', 'gluten,nuts'), ('mi+nut', 'milk,nuts'), ('glu+mi+nut', 'milk,nuts,gluten'), ('none', 'none')], default='none', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dietary_mentions',
            field=models.CharField(blank=True, choices=[('vegan', 'vegan'), ('vegetarian', 'vegetarian'), ('halal', 'halal'), ('kosher', 'kosher'), ('none', 'none')], default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.CharField(blank=True, choices=[('starter', 'starter'), ('main', 'main'), ('dessert', 'dessert'), ('side', 'side'), ('drink', 'drink'), ('deal', 'deal')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='delivery_fee',
            field=models.FloatField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
