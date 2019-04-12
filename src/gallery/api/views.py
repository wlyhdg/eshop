from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import HttpResponseRedirect
from ..models import ClothingModel, ChargeModel
from .serializers import UserSerializer, ClothSerializer, ChargeSerializer
import stripe
from eshop import settings

class ListClothes(ListAPIView):
	serializer_class = ClothSerializer
	authentication_classes = []
	permission_classes = []

	def get_queryset(self):
		_id = self.kwargs['num']
		return ClothingModel.objects.filter(id=_id)

class ChargeView(ListCreateAPIView):
	queryset = ChargeModel.objects.all()
	serializer_class = ChargeSerializer
	permission_classes = [] # add view api permissions for the responsible user only

	def post(self, request, num):
		cloth_obj = ClothingModel.objects.get(id=num)
		data = self.request.data
		stripe.api_key = settings.API_KEY
		charge_rtn_body = stripe.Charge.create(
			amount=int((float(cloth_obj.net_price)*100)),
			currency="usd",
			source=data['stripeToken'], # "tok_visa",  obtained with Stripe.js
			description= "[Stripe charge] " + cloth_obj.description.upper()
		)

		chargemd = ChargeModel(owner=request.user,charge_info=charge_rtn_body)
		chargemd.save()

		return HttpResponseRedirect('/')
