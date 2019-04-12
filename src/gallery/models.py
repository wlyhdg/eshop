from django.db import models
from decimal import Decimal
import jsonfield

def _photo_upload(instance, filename):
	return "photos/%s/%s" % (instance.brand, filename)

# Create your models here.
class ClothingModel(models.Model):
	NIKE = 'Nike'
	NAUTICA = 'Nautica'
	CALVIN_KLEIN = 'Calvin Klein'
	ADIDAS = 'Adidas'
	COLUMBIA = 'Columbia'

	brand_choices = (
			(NIKE, 'Nike'),
			(NAUTICA, 'Nautica'),
			(CALVIN_KLEIN, 'Calvin Klein'),
			(ADIDAS, 'Adidas'),
			(COLUMBIA, 'Columbia')
		)

	description = models.CharField(max_length=100)
	brand = models.CharField(max_length=100, choices=brand_choices)
	full_price = models.DecimalField(max_digits=9, decimal_places=2)
	discount = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
	image = models.ImageField(default=None, upload_to=_photo_upload)
	net_price = models.DecimalField(max_digits=9, decimal_places=2)

	def __str__(self):
		return "[%s] " % self.brand + self.description

	def save(self, *args, **kwargs):
		full_price = self.full_price
		self.description = self.description.title()
		discount = self.discount / 100
		self.net_price = self.full_price
		if self.discount > 0.00:
			self.net_price = full_price * (1 - discount)

		super().save(*args, **kwargs)

class ChargeModel(models.Model):
	owner = models.CharField(max_length=100, default=" ")
	charge_info = jsonfield.JSONField()

	def __str__(self):
		if hasattr(self.charge_info, 'id'):
			return self.charge_info['id']
		else:
			return 'charge_x'




