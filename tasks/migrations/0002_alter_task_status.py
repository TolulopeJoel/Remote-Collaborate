# Generated by Django 4.1 on 2023-01-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('on hold', 'on hold'), ('completed', 'completed'), ('in review', 'in review'), ('not started', 'not started'), ('in progress', 'in progress')], max_length=20),
        ),
    ]
