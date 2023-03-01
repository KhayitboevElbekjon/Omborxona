from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from .models import *

class BulimView(View):
    def get(self,request):
        return render(request,'bulimlar.html')

class Cl_up_View(View):
    def get(self,request,son):
        data={
            'data':Client.objects.get(id=son)
        }
        return render(request,'client_update.html',data)
    def post(self,request,son):
        Client.objects.filter(id=son).update(
            tel=request.POST.get('tel'),
            qarz=request.POST.get('qarz')
        )
        return redirect('/Asosiy/client/')


class ClientView(View):
    def post(self,request):
        Client.objects.create(
            ism=request.POST.get('ism'),
            nom=request.POST.get('nom'),
            manzil=request.POST.get('manzil'),
            tel=request.POST.get('tel_num'),
            qarz=request.POST.get('qarz'),
            ombor_fk=Ombor.objects.get(user=request.user)
        )
        return redirect('/Asosiy/client')
    def get(self, request):
        kk = Ombor.objects.get(user=request.user)

        soz = request.GET.get('qidirish')
        if soz is None or soz == '':
            cl = Client.objects.filter(ombor_fk=kk)
        else:
            cl = Client.objects.filter(ombor_fk=kk, ism__contains=soz)

        data = {
            "data": cl
        }
        return render(request, 'clients.html', data)



class HomeView(View):
    def post(self,request):
        logi=request.POST.get('l')
        paro=request.POST.get('p')
        foydalanuvchi=authenticate(request,username=logi,password=paro)
        if foydalanuvchi:
            login(request,foydalanuvchi)
            return redirect('/Asosiy/bulim/')
        return redirect('/')
    def get(self, request):
        return render(request, 'home.html')

class LogautView(View):
    def get(self,request):
        logout(request)
        return redirect('/')

class Pr_up_View(View):
    def get(self, request,son):
        data={
            'data':Mahsulot.objects.get(id=son)
        }
        return render(request, 'product_update.html',data)
    def post(self,request,son):
        Mahsulot.objects.filter(id=son).update(
            miqdor=request.POST.get('miqdori'),
            narx=request.POST.get('price')
        )
        return redirect('/Asosiy/mahsulotlar')
class ProductsView(View):
    def post(self,request):
        Mahsulot.objects.create(
            nom=request.POST.get('pr_name'),
            brend=request.POST.get('pr_brand'),
            narx=request.POST.get('pr_price'),
            kelgan_sana=request.POST.get('sana'),
            miqdor=request.POST.get('pr_amount'),
            ulchov=request.POST.get('ulchov'),
            ombor_fk=Ombor.objects.get(user=request.user)
        )
        return redirect('/Asosiy/mahsulotlar')
    def get(self, request):
        kk=Ombor.objects.get(user=request.user)

        soz = request.GET.get('qidirish')
        if soz is None or soz == '':
            cl = Mahsulot.objects.filter(ombor_fk=kk)
        else:
            cl = Mahsulot.objects.filter(ombor_fk=kk,nom__contains=soz,brend__contains=soz)

        data = {
            "data": cl
        }
        return render(request, 'products.html',data)

class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')

class ProductsDelView(View):
    def get(self,request,son):
        d=Mahsulot.objects.get(id=son)
        if Ombor.objects.get(user=request.user)==d.ombor_fk:
            d.delete()
        return redirect('/Asosiy/mahsulotlar/')

class ClientDelView(View):
    def get(self,request,son):
        ll=Client.objects.get(id=son)
        if Ombor.objects.get(user=request.user)==ll.ombor_fk:
            ll.delete()
        return redirect('/Asosiy/client')