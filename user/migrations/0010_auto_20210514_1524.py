# Generated by Django 2.2.17 on 2021-05-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_country_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='alpha2',
            new_name='sortname',
        ),
        migrations.AddField(
            model_name='country',
            name='phoneCode',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
