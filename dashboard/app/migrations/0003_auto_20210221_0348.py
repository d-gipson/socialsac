# Generated by Django 3.1.7 on 2021-02-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210220_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='c19testsite',
            name='link',
            field=models.CharField(default='https://www.projectbaseline.com/studies/covid-19/eligibility/', max_length=200),
        ),
        migrations.AddField(
            model_name='c19vaccsite',
            name='link',
            field=models.CharField(default='https://myturn.ca.gov/landing', max_length=200),
        ),
    ]
