from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# importing loading from django template
from django.template import loader
from django.db.models import Sum
from _decimal import Decimal


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *
from .forms import SignUpForm

# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('aboutus/products.html')
    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def aboutus(request):
    return render(request, 'aboutus/aboutus.html', {'aboutus': aboutus})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')     
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
now = timezone.now()
