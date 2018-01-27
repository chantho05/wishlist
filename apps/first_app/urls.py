from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_signin$', views.submit_signin),
    url(r'^submit_register$', views.submit_registration),
    url(r'^travels$', views.travels),
    url(r'^destination$', views.destination),
    url(r'^add$', views.add),
]