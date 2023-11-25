from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

