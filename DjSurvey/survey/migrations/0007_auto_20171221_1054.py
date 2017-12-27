# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_add_related_name_for_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text (multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('select_image', 'Select Image'), ('integer', 'integer')], default='text', max_length=200),
        ),
    ]
