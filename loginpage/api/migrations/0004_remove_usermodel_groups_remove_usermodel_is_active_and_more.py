# Generated by Django 5.0 on 2024-01-02 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_usermodel_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='user_permissions',
        ),
    ]
