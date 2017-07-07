from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from portfolio import views
from .models import Document


urlpatterns = [
    url(r'^instructional-design/', views.InstructionalList.as_view(), name='instructional'),
    url(r'^sales/', views.SalesList.as_view(), name='sales')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
