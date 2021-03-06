# Generated by Django 3.0.2 on 2020-01-26 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rios', '0003_sensors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=200)),
                ('river', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rios.River')),
            ],
        ),
        migrations.DeleteModel(
            name='Sensors',
        ),
    ]
