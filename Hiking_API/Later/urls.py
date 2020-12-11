from django.urls import path
from .views import LaterTrailsDeleteView
from django.conf.urls import url

urlpatterns = [
    url(r'(?P<user_id>\d+)/delete$', LaterTrailsDeleteView.as_view(), name="delete-group"),
]