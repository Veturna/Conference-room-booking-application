# Generated by Django 4.1.6 on 2023-02-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
            ],
        ),
    ]
