from django.conf.urls import url

from car.views import car, Carshow

urlpatterns = [
    url(r'^car/$', car.as_view(), name='购物车'),
    url(r'^showcar/$', Carshow.as_view(), name='购物'),
]