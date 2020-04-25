from django.conf.urls import url
from .views import home, index, contact


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^index', index, name='index'),
    url(r'^contact', contact, name='contact'),
]
