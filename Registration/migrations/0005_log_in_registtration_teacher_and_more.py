# Generated by Django 4.1.5 on 2023-03-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0004_alter_log_in_registtration_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_in_registtration_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.TextField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('password', models.TextField(max_length=20)),
                ('account_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='log_in_registtration',
            new_name='log_in_registtration_student',
        ),
    ]
