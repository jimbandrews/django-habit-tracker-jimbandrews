# Generated by Django 4.0 on 2021-12-08 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_alter_dailyrecord_date_alter_dailyrecord_habit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyrecord',
            options={'ordering': ['habit', 'date']},
        ),
    ]
