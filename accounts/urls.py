from django.conf.urls import url, include
from accounts.views import logout, login, cartlogin, registration, cartregistration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^cartlogin/', cartlogin, name="cartlogin"),
    url(r'^register/', registration, name="registration"),
    url(r'^cartregister/', cartregistration, name="cartregistration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password_reset/', include(url_reset))
]
