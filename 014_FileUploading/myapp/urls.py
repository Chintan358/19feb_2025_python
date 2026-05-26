from django.urls import path
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
    path("delete",delete_product,name="delete"),
    path("update",update_product,name="update")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)