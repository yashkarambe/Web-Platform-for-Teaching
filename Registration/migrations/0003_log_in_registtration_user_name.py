# Generated by Django 4.1.5 on 2023-03-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_remove_log_in_registtration_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_in_registtration',
            name='User_name',
            field=models.TextField(default='user', max_length=20),
        ),
    ]
