# Generated by Django 2.2.1 on 2019-05-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_auto_20190510_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='type',
            field=models.CharField(default='cottage', max_length=50),
            preserve_default=False,
        ),
    ]
