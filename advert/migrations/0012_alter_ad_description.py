# Generated by Django 4.2.9 on 2024-02-28 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0011_alter_ad_dayf_alter_ad_dayt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(),
        ),
    ]