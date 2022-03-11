from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),  # added
    path('contactus/', views.contactus, name='contactus'),

]

