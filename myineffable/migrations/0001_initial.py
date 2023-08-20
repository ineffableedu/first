# Generated by Django 4.2.4 on 2023-08-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentreRegisterAdmin',
            fields=[
                ('center_id', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('center_name', models.CharField(blank=True, max_length=500, null=True)),
                ('center_photo', models.CharField(blank=True, max_length=500, null=True)),
                ('center_address', models.CharField(blank=True, max_length=500, null=True)),
                ('center_mobile', models.CharField(blank=True, max_length=500, null=True)),
                ('center_email', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
