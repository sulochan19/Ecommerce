# Generated by Django 2.2.3 on 2019-08-05 02:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190724_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='producthasreview',
            name='pubdate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]