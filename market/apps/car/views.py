from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_redis import get_redis_connection

from shop.models import Shop_sku


#
#
# class car1(View):
#     """
#     验证登录
#     接收购物车加入的数量(count),当前商品的id(sku_id)
#     验证都为整数,数量大于0 商品id纯在
#     """
#
#     def post(self, request):
#         userid = request.session.get('username')
#
#         sku_id = request.POST.get('sku_id')
#
#         count = request.POST.get('count')
#         sku_id = int(sku_id)
#         count = int(count)
#         a = get_redis_connection('default')
#         re = count - 1
#         a.hdel(userid, sku_id)
#         a.hincrby(userid, sku_id, re)
#         return JsonResponse({'del': 0,'count':re})
#
#     def get(self, request):
#         return render(request, 'shop/shopcart.html')
from user.views import BaseView


class car(View):
    """
    验证登录
    接收购物车加入的数量(count),当前商品的id(sku_id)
    验证都为整数,数量大于0 商品id纯在
    """

    def post(self, request):
        userid = request.session.get('username')
        # 如果登录返回1 没有返回0 2 3 4
        count = request.POST.get('count')
        sku_id = request.POST.get('sku_id')
        try:
            count = int(count)
            sku_id = int(sku_id)
        except Shop_sku.DoesNotExist:
            return JsonResponse({"a": 0, "err": "输入的不为整数"})
        if userid:
            if count > 0:
                if sku_id:
                    cnn = get_redis_connection('default')
                    cnn.hincrby(userid, sku_id, count)

                    return JsonResponse({'a': 1 ,'count':count})
                else:
                    return JsonResponse({'a': 2, "err": "没有该商品"})
            else:
                cnn = get_redis_connection('default')
                cnn.hincrby(userid, sku_id, count)
                return JsonResponse({'a': 3, "err": "删除成功"})
        else:
            return JsonResponse({'a': 4, "err": "没有登录"})

    def get(self, request):

        return render(request,'shop/shopcart.html')


class Carshow(BaseView):
    def post(self,request):
        pass
    def get(self,request):
        userid = request.session.get('username')
        cnn = get_redis_connection('default')
        rs = cnn.hgetall(userid)
        shopskulist=[]
        for skuid ,count in rs.items():
            skuid=int(skuid)
            count=int(count)
        # 获取到该商品的对象
            car=Shop_sku.objects.get(pk=skuid)
            #自定义一个属性来保存count
            car.count=count

            shopskulist.append(car)

        context={
            'car':shopskulist,

        }
        return render(request,'shop/shopcart.html',context)
