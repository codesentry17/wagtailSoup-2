# Generated by Django 4.2.9 on 2024-02-11 01:59

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='advert.formpage'),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='extra_info',
            field=wagtail.fields.StreamField([('Block', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock())]))], blank=True, use_json_field=True),
        ),
    ]
