from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages

# Create your views here.
def testFunc(request):
    return HttpResponse("this is test product")

def product_show(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)

def category_show(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/allcategory.html', context)

def post_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "add product successfully !")
            return redirect('/products/addproduct')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify product field.')
            return render(request,'products/addproduct.html',{
                'form':form
            })
    
    context = {
        'form':ProductForm
    }

    return render(request, 'products/addproduct.html', context)

def post_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "add category successfully !")
            return redirect('/products/addcategory')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify category field.')
            return render(request,'products/addcategory.html',{
                'form':form
            })
    
    context = {
        'form':CategoryForm
    }

    return render(request, 'products/addcategory.html', context)




