# Generated by Django 4.2.9 on 2024-03-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0017_alter_pagelist_external_resource_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelist',
            name='resource_label',
            field=models.CharField(default='---', help_text='Link Short Name', max_length=15),
        ),
    ]
