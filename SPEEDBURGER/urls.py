from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('burgerwebsite.urls')),
    path(r'^admin/', admin.site.urls),
    path(r'^burgerwebsite/', include('burgerwebsite.urls'))
]
