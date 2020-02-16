from django.conf import settings
from django.db import models
from django.utils import timezone
#AO ALTERAR O ARQUIVO NÃO ESQUECER:
#py manage.py makemigrations
#py manage.py migrate


class River(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Sensor(models.Model):
	name = models.ForeignKey(River, on_delete=models.CASCADE)
	sensor_name = models.CharField(max_length=200)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.sensor_name)

class Reading(models.Model):
	name = models.ForeignKey(Sensor, on_delete=models.CASCADE)
	sensor_read = models.CharField(max_length=200)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.sensor_read)