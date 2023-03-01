
from django.urls import path
from .views import *
urlpatterns = [
    path('bulim/',BulimView.as_view()),  # linkida yozishda: asosiy/bulim
    path('mahsulotlar/',ProductsView.as_view()), # linkida yozishda: asosiy/mahsulotlar
    # path('mahsulot/',ProductsView.as_view()),
    path('stats/',StatsView.as_view()),
    path('client/',ClientView.as_view()),
    path('logout/',LogautView.as_view()),
    path('pr_up/<int:son>',Pr_up_View.as_view()),
    path('mahsulot_del/<int:son>',ProductsDelView.as_view()),
    path('ClientDel/<int:son>',ClientDelView.as_view()),
    path('cl_up/<int:son>',Cl_up_View.as_view())

]