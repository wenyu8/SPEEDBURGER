from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('burgerwebsite.urls')),
    path(r'^burgerwebsite/', include('burgerwebsite.urls')),
    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
