# Generated by Django 4.1.5 on 2023-03-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_log_in_registtration_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_in_registtration',
            name='User_name',
            field=models.TextField(max_length=20),
        ),
    ]
