from django.conf.urls import url
from .views import index, home, contact


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^index', index, name='index'),
    url(r'^contact', contact, name='contact'),
]
