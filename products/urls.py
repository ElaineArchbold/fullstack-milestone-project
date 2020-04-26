from django.conf.urls import url, include
from .views import all_products, baby, christening, communions, engagement_anniversary, family, fingerprint, mothersdayfathersday, teacher, wedding, gallery

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^baby', baby, name='baby'),
    url(r'^christening', christening, name='christening'),
    url(r'^communions', communions, name='communions'),
    url(r'^engagement-anniversary', engagement_anniversary, name='engagement-anniversary'),
    url(r'^family', family, name='family'),
    url(r'^fingerprint', fingerprint, name='fingerprint'),
    url(r'^mothersdayfathersday', mothersdayfathersday, name='mothersdayfathersday'),
    url(r'^teacher', teacher, name='teacher'),
    url(r'^wedding', wedding, name='wedding'),
    url(r'^gallery', gallery, name='gallery'),
]
