# Generated by Django 4.2.5 on 2023-09-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='assigned_projects', to='project.user', verbose_name='Assigned Users'),
        ),
    ]
