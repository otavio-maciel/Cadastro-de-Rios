# Generated by Django 3.0.1 on 2020-01-31 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rios', '0006_reading'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='password',
            field=models.CharField(default=123456, max_length=200),
            preserve_default=False,
        ),
    ]
