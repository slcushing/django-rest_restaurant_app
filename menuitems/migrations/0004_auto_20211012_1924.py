# Generated by Django 3.2.8 on 2021-10-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0003_remove_menuitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
