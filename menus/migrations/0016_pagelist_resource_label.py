# Generated by Django 4.2.9 on 2024-03-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0015_navbar_redirect_alter_navbar_name1'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelist',
            name='resource_label',
            field=models.CharField(default='unlabelled', max_length=15),
        ),
    ]
