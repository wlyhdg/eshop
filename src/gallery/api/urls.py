from django.urls import path
from gallery.views import ClothingView
from gallery.api.views import ListClothes
from gallery.api.views import ChargeView

urlpatterns = [
    path('<int:num>/', ListClothes.as_view()),
    path('charge/<int:num>', ChargeView.as_view(), name='charge_api'),
]