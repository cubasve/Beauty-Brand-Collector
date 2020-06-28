from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

class Beauty:
    def __init__(self, name, country, description, founded):
        self.name = name
        self.country = country
        self.description = description
        self.founded = founded

beauty = [
    Beauty('Marcelle', 'Canada', 'Offers skincare and makeup products for sensitive skin', 1910),
    Beauty('Deciem', 'Canada', 'Offers affordable, mid-range, and luxury skincare products', 2013),
    Beauty('Elate Cosmetics', 'Canada', 'Sustainable makeup brand that has eco-friendly packaging', 2014)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def beauty_index(request):
    return render(request, 'beauty/index.html', {'beauty': beauty})