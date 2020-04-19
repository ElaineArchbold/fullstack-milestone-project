from django.conf.urls import url
from .views import index, home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^index', index, name='index'),
]
