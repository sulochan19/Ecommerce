# Generated by Django 2.2.3 on 2019-07-21 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190721_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Title',
            new_name='title',
        ),
    ]