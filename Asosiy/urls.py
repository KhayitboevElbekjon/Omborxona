
from django.urls import path
from .views import *
urlpatterns = [
    path('bulim/',BulimView.as_view()),  # linkida yozishda: asosiy/bulim
    path('mahsulotlar/',ProductsView.as_view()) # linkida yozishda: asosiy/mahsulotlar
]