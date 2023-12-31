# Generated by Django 3.1.13 on 2021-10-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_export', '0002_auto_20210921_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='export',
            name='title',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='export',
            name='status',
            field=models.CharField(
                choices=[
                    ('created', 'Created'),
                    ('in_progress', 'In progress'),
                    ('failed', 'Failed'),
                    ('completed', 'Completed'),
                ],
                default='created',
                max_length=64,
                verbose_name='Export status',
            ),
        ),
    ]
