from django.conf.urls import url, include
from .views import all_products, baby, christening, communions, engagement, family, fathersday, fingerprint, mothersday, teacher, wedding

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^baby', baby, name='baby'),
    url(r'^christening', christening, name='christening'),
    url(r'^communions', communions, name='communions'),
    url(r'^engagement', engagement, name='engagement'),
    url(r'^family', family, name='family'),
    url(r'^fathersday', fathersday, name='fathersday'),
    url(r'^fingerprint', fingerprint, name='fingerprint'),
    url(r'^mothersday', mothersday, name='mothersday'),
    url(r'^teacher', teacher, name='teacher'),
    url(r'^wedding', wedding, name='wedding'),
]
