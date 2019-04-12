from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ClothingModel

ITEMS_PER_ROW = 4

# Create your views here.
class ClothingView(ListView):
	model = ClothingModel
	context_object_name = 'cloth_list'
	template_name = 'gallery/clothing_article.html'

	def get_context_data(self, **kwargs):
		context = super(ClothingView, self).get_context_data(**kwargs)
		all_clothes = ClothingModel.objects.all()
		cfilt = [all_clothes[x:x+ITEMS_PER_ROW] for x in range (0,len(all_clothes)+1) if x % ITEMS_PER_ROW == 0]
		context['linedup_clothes'] = cfilt
		return context