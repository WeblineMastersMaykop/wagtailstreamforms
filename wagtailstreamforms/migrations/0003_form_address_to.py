# Generated by Django 3.2.11 on 2022-01-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailstreamforms', '0002_form_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='address_to',
            field=models.EmailField(blank=True, help_text='Email to send the message to', max_length=350, verbose_name='Email to'),
        ),
    ]
