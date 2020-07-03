from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Brand


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def brands_index(request):
    brands = Brand.objects.all()
    return render(request, 'brands/index.html', {'brands': brands})


def brands_detail(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return render(request, 'brands/detail.html', {'brand': brand})


class BrandCreate(CreateView):
    model = Brand
    fields = '__all__'
