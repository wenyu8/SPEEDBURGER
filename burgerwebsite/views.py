from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# importing loading from django template
from django.template import loader


# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('aboutus/products.html')
    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def aboutus(request):
    return render(request, 'aboutus/aboutus.html', {'aboutus': aboutus})

