from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Product
from . forms import ProductForm
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





