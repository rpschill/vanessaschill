from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name="home"),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)