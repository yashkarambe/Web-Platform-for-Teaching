# Generated by Django 4.1.5 on 2023-03-12 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choice_1', models.CharField(max_length=200)),
                ('Choice_2', models.CharField(max_length=200)),
                ('Choice_3', models.CharField(max_length=200)),
                ('Choice_4', models.CharField(max_length=200)),
                ('Choice_true', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quize.question')),
            ],
        ),
    ]
