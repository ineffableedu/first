# Generated by Django 4.2.4 on 2023-08-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myineffable', '0004_centreregisterstudent_centeruserid'),
    ]

    operations = [
        migrations.AddField(
            model_name='centreregisterstudent',
            name='status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
