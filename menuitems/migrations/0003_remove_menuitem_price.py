# Generated by Django 3.2.8 on 2021-10-12 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0002_rename_menuitems_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='price',
        ),
    ]
