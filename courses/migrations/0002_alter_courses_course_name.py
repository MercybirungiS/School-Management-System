# Generated by Django 3.2.6 on 2021-08-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(max_length=40),
        ),
    ]
