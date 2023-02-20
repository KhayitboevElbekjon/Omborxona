
from django.urls import path
from .views import *
urlpatterns = [
    path('bulim/',BulimView.as_view()),  # linkida yozishda: asosiy/bulim
    path('mahsulotlar/',ProductsView.as_view()), # linkida yozishda: asosiy/mahsulotlar
    # path('mahsulot/',ProductsView.as_view()),
    path('stats/',StatsView.as_view()),
    path('client/',ClientView.as_view()),
    path('logout/',LogautView.as_view())

]