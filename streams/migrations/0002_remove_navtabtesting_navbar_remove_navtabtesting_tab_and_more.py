# Generated by Django 4.2.9 on 2024-03-17 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navtabtesting',
            name='navbar',
        ),
        migrations.RemoveField(
            model_name='navtabtesting',
            name='tab',
        ),
        migrations.DeleteModel(
            name='NavbarTesting',
        ),
        migrations.DeleteModel(
            name='NavTabTesting',
        ),
    ]
