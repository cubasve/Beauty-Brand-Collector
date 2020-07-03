from django.shortcuts import render
from .models import Brand

# Create your views here.
# Add the following import

# from django.http import HttpResponse

# class Beauty:
#     def __init__(self, name, country, description, founded):
#         self.name = name
#         self.country = country
#         self.description = description
#         self.founded = founded

# beauty = [
#     Beauty('Marcelle', 'Canada', 'Offers skincare and makeup products for sensitive skin', 1910),
#     Beauty('Deciem', 'Canada', 'Offers affordable, mid-range, and luxury skincare products', 2013),
#     Beauty('Elate Cosmetics', 'Canada', 'Sustainable makeup brand that has eco-friendly packaging', 2014)
# ]


# Define the home view
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
