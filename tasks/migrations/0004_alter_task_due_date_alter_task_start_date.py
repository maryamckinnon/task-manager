# Generated by Django 4.0.4 on 2022-05-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_due_date_alter_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(),
        ),
    ]