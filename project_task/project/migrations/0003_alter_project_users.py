# Generated by Django 4.2.5 on 2023-10-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to='project.user', verbose_name='User'),
        ),
    ]
