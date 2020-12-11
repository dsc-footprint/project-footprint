from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from Later import urls as later_urls
from .routers import router
from django.conf.urls import url

urlpatterns = [

    # ListView of Models
    path('', include(router.urls)),
    url(r'^Later/', include(later_urls)),
]