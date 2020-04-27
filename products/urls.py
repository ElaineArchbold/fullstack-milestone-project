from django.conf.urls import url
from .views import all_products, category_view, gallery

urlpatterns = [
    url(r'^$', all_products, name='products'),
     url(r'^gallery', gallery, name='gallery'),
    url(r'^(?P<category>[a-zA-Z]+)$', category_view, name='specific_category'),
   
]
