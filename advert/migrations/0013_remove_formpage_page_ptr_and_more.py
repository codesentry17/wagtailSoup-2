# Generated by Django 4.2.9 on 2024-03-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0012_alter_ad_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='formpage',
            name='uploaded_image_collection',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
