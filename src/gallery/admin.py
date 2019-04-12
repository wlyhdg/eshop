from django.contrib import admin
from .models import ClothingModel, ChargeModel

# Register your models here.
class ClothingAdmin(admin.ModelAdmin):
	readonly_fields = ('net_price',)

class ChargeAdmin(admin.ModelAdmin):
	readonly_fields = ('owner', 'charge_info')

admin.site.register(ClothingModel, ClothingAdmin)
admin.site.register(ChargeModel, ChargeAdmin)