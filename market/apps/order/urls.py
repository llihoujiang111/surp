from django.conf.urls import url

from shop.views import index, allorder, category, datail

urlpatterns = [
    url(r'^index/$',index,name='首页'),
    url(r'^allorder/$',allorder,name='订单'),
    url(r'^detail/(?P<id>\d+)/$',datail,name='详情'),
    url(r'^category/(?P<cid>\d+)/(?P<order>\d+)/$',category,name='分类'),
]