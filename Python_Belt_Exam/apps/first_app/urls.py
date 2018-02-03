from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^submit_signin$', views.submit_signin),
    url(r'^submit_register$', views.submit_registration),
    url(r'^submit_logout$', views.submit_logout),
    url(r'^index$', views.index),
    url(r'^add$', views.add),
    url(r'^show$', views.show),
    url(r'^wish_items/create$', views.create),
    url(r'^logout$', views.logout),

]