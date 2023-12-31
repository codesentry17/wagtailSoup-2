# Generated by Django 5.0 on 2023-12-10 16:13

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('navbar', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='nav_items', to='menus.navbar')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page')),
                ('nav_item', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_lists', to='menus.navitem')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
