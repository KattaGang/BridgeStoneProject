# Generated by Django 4.1.4 on 2023-01-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_alter_businessunit_jury'),
        ('account', '0006_rename_isadmin_profile_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='jury_programs',
            field=models.ManyToManyField(blank=True, to='program.program'),
        ),
    ]