from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login


class BulimView(View):
    def get(self,request):
        return render(request,'bulimlar.html')

class Cl_up_View(View):
    def get(self,request):
        return render(request,'client_update.html')


class ClientView(View):
    def get(self, request):
        return render(request, 'clients.html')


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
    def get(self, request):
        return render(request, 'product_update.html')

class ProductsView(View):
    def get(self, request):
        return render(request, 'products.html')

class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')