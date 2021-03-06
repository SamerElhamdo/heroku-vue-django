from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
  path('admin/', admin.site.urls),
  url(r'^$', TemplateView.as_view(template_name='index.html')),
  path('api_example', include('api_example.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# add static files
