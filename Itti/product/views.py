# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

# Create your views here.
def bibisha(request):
        return render(request,"bibisha.html",{})

def show(request):
    products = Product.objects.all()
    return render(request,"show.html",{'products':products})

@csrf_protect
def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    form = ProductForm()
    csrfContext = RequestContext(request)
    return render(request,'pindex.html',{'form':form}, csrfContext)

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/show")

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request,'edit.html', {'product':product})

def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'product': product})

def raw_sql(request):
    name = ""
    for p in Product.objects.raw('SELECT * from products'):
        name = name + "" + p.pname
    return JsonResponse({'result':name})
