# Generated by Django 4.2.9 on 2024-01-27 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_navbar2_sample'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='sample',
            name='img',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='locale',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='nav2',
        ),
        migrations.DeleteModel(
            name='Navbar2',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]
