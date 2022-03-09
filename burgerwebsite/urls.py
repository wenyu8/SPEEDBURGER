from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='products'),
    path('aboutus/', views.aboutus, name='aboutus')
    path('signup/', views.signup, name='signup'),  # added

]

