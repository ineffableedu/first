# Generated by Django 4.2.4 on 2023-08-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myineffable', '0009_centreregisteradmin_owner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='centreregisterstudent',
            name='studentdatetime',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
