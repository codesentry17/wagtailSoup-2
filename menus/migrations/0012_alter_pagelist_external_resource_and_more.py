# Generated by Django 4.2.9 on 2024-02-25 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('menus', '0011_pagelist_external_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelist',
            name='external_resource',
            field=models.URLField(blank=True, help_text="URL, don't forget to include 'Nav Title'", null=True),
        ),
        migrations.AlterField(
            model_name='pagelist',
            name='page_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page'),
        ),
    ]
