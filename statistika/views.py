from django.shortcuts import render, redirect
from django.views import View
from .models import *
from Asosiy.models import *
from Asosiy.models import Mahsulot
from Asosiy.models import Ombor


class StatistikaView(View):
    # def post(self,request):
    #     mahsulot=Mahsulot.objects.filter(id=request.POST.get(''))
    def get(self,request):
        if request.user.is_authenticated:
            qidir=request.GET.get('qidirish')

            if qidir :
                l=Statistika.objects.filter(ombor__user=request.user)
            else:
                l =Statistika.objects.filter(ombor__user=request.user,mahsulot__nom__contains=qidir) |Statistika.objects.filter(ombor__user=request.user, client__contains=qidir)

            data={
                'data2':l,
                'mahsulotlar':Mahsulot.objects.filter(ombor__user=request.user)
            }
            return render(request,'stats.html',data)
        return redirect('/')
class StatistikaDelView(View):
    def get(self,request,son):

        l=Statistika.objects.filter(id=son)
        if Ombor.objects.filter(user=request.user)==l.ombor:
            l.delete()
            return redirect('/')


