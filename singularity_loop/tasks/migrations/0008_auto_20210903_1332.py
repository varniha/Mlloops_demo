# Generated by Django 3.1.13 on 2021-09-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20210618_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_labeled',
            field=models.BooleanField(db_index=True, default=False, help_text='True if the number of annotations for this task is greater than or equal to the number of maximum_completions for the project', verbose_name='is_labeled'),
        ),
    ]
