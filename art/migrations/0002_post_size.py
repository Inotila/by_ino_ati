# Generated by Django 3.2.13 on 2022-05-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='size',
            field=models.CharField(default='cm', max_length=100),
        ),
    ]
