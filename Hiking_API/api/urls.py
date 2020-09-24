from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from .routers import router

urlpatterns = [

    # ListView of Models
    path('', include(router.urls)),
]