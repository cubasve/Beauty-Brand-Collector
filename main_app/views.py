from django.shortcuts import render, redirect
from .models import Brand, Product
from .forms import PurchaseForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def brands_index(request):
    brands = Brand.objects.all()
    return render(request, 'brands/index.html', {'brands': brands})


def brands_detail(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    purchase_form = PurchaseForm()
    return render(request, 'brands/detail.html', {
        'brand': brand,
        'purchase_form': purchase_form
    })


class BrandCreate(CreateView):
    model = Brand
    fields = '__all__'


class BrandUpdate(UpdateView):
    model = Brand
    fields = ['country', 'description', 'founded']


class BrandDelete(DeleteView):
    model = Brand
    success_url = '/brands/'


def add_purchase(request, brand_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.brand_id = brand_id
        new_purchase.save()
    return redirect('detail', brand_id=brand_id)


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name']


class ProductDelete(DeleteView):
    model = Product
    success_url = '/products/'
