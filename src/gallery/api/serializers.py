from ..models import ChargeModel, ClothingModel
from rest_framework import serializers
from django.contrib.auth.models import User, Group

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingModel
        fields = '__all__'

class ChargeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChargeModel
		fields = '__all__'