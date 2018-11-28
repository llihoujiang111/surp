from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django_redis import get_redis_connection
from shop.models import Shop_sku, Index_lunbo, Index_active, Active_zone, Shop_sort
from user.views import sess


# 商城首页
def index(request):
    a = Index_lunbo.objects.filter(is_delete=False)

    b = Index_active.objects.filter(is_delete=False)

    c = Active_zone.objects.filter(is_delete=False)
    context = {
        'a': a,
        'b': b,
        'c': c
    }
    return render(request, 'shop/index.html', context)


# 提交订单
def allorder(request):
    return render(request, 'shop/allorder.html')


# 商品详情
def datail(request, id):
    try:
        a = Shop_sku.objects.get(pk=id)
    except Shop_sku.DoesNotExist:
        return redirect("商城:首页")
    context = {
        'a': a
    }
    return render(request, 'shop/detail.html', context)


# 商品分类
def category(request, cid, order):
    try:
        cid = int(cid)
        order = int(order)
    except:
        return redirect('商城:分类')
    a = Shop_sort.objects.filter(is_delete=False)
    a1 = a.first()
    if cid == 0:
        cid = a1.pk

    b1 = Shop_sku.objects.filter(is_delete=False)
    order_list = ['id', '-sku_sale', 'sku_price', '-sku_price', 'create_time']
    try:
        c = order_list[order]
    except:
        c = order_list[0]
        order = 0
    b = b1.order_by(c)
    # p=Shop_sku.objects.filter(is_delete=False)
    # limt = 1
    # pag = Paginator(b, limt)
    # pa = request.GET.get('page', 1)
    # try:
    #     aaa = pag.page(pa)
    # except PageNotAnInteger:
    #     aaa = pag.page(1)
    # except EmptyPage:
    #     aaa = pag.page(pag.num_pages)
    username = request.session.get('username')
    cnn = get_redis_connection('default')
    re = cnn.hvals(username)
    rs=0
    for v in re:
        rs+=int(v)
    context = {
        'a': a,
        'b': b ,
        'aid': cid,
        'd': order,
        're':rs
    }
    return render(request, 'shop/category.html', context)

