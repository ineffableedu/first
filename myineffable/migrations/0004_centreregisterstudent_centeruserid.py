# Generated by Django 4.2.4 on 2023-08-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myineffable', '0003_centreregisterstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='centreregisterstudent',
            name='centeruserid',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]