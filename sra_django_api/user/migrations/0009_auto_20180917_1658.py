# Generated by Django 2.0.3 on 2018-09-17 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20180917_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='all_bioprojects',
            new_name='no_bioprojects_all',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='all_experiments',
            new_name='no_experiments_all',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='all_runs',
            new_name='no_runs_all',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='all_size',
            new_name='size_all',
        ),
    ]