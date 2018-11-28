import hashlib
import os
import random
import uuid

from django.conf import settings
from django.http import  JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django_redis import get_redis_connection

from db.help import send_sms
from user.forms import User_form, Myinfor, Addressform
from user.models import User, my_infor, User_Address
import re


#  创建一个session装饰器
def sess(old):
    def news(request, *aw, **kaw):
        b = request.session
        c = b.get('username')
        if c:
            return old(request, *aw, **kaw)
        else:
            return redirect('用户:登录')

    return news
class BaseView(View):
    """
    基础视图类用于验证是否登录
    """
    @method_decorator(sess)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView,self).dispatch(request, *args, **kwargs)

# 登录
def user_login(request):
    #  判断是post提交还是get提交
    if request.method == 'POST':
        # 获取post提交的的form表单数据
        hq = request.POST
        #  验证用户名
        if User.objects.filter(username=hq.get('username')):
            a1 = hq.get('password1')
            # 获取到form的密码并且哈希加密
            h = hashlib.md5(a1.encode('utf-8'))
            a1 = h.hexdigest()
            #  验证密码
            if User.objects.filter(password=a1):
                # 创建session
                # 跳转到商城首页
                ida=User.objects.filter(password=a1).first()
                id=ida.pk
                request.session['username'] = hq.get('username')
                request.session['id'] = id
                ne=request.GET.get("ne")
                if ne:
                    return redirect(ne)
                else:
                    return redirect('商城:首页')
            else:
                # 如果密码错误返回当前页并且报错
                context = {
                    'err': '用户或密码错误!!',
                    'hq': hq
                }
                return render(request, 'user/login.html', context)
        else:
            # 若果用户名错误返回当前页并且报错
            context = {
                'err': '用户或密码错误!!!',
                'hq': hq
            }
            return render(request, 'user/login.html', context)
    else:
        # get提交
        return render(request, 'user/login.html')


# 注册
def reg_login(request):
    #  判断是post提交还是get提交
    if request.method == 'POST':
        # 获取post提交的的form表单数据
        aa = request.POST
        # 判断用户是否勾选用户协议
        if aa.get('checkbox'):
            # 判断用户名是否存在于数据库,是否已被注册
            if User.objects.filter(username=aa.get('username')):
                context = {
                    'zc': '用户名已被注册'
                }
                return render(request, 'user/reg.html', context)
            else:
                # 没有注册调用form类
                data = User_form(aa)
                # 验证数据合法性
                if data.is_valid():
                    # 清洗数据
                    a = data.cleaned_data
                    # 处理数据 哈希加密密码 用户名密码加入数据库
                    a1 = a.get('password')
                    h = hashlib.md5(a1.encode('utf-8'))
                    a1 = h.hexdigest()
                    User.objects.create(username=a.get('username'), password=a1)
                    # 返回登录页面
                    return redirect('用户:登录')
                else:
                    # 数据不合法报错
                    context = {
                        'err': data.errors
                    }
                    return render(request, 'user/reg.html', context)
        else:
            # 没有勾选用户协议报错并回显以前填写的数据
            context = {
                'er': '请同意用户协议',
                'aa': aa
            }
            return render(request, 'user/reg.html', context)
    else:
        return render(request, 'user/reg.html')


# 忘记密码
def forget_password(request):
    if request.method=='POST':
        hq=request.POST
        phone=hq.get('username')
        a=User_form(hq)
        if User.objects.filter(username=phone):
            if a.is_valid():
                data=a.cleaned_data
                data1=data.get('password')
                h = hashlib.md5(data1.encode('utf-8'))
                a1 = h.hexdigest()
                User.objects.filter(username=phone).update(password=a1)
                return redirect('商城:首页')
            else:
                context={
                    'err':a.errors
                }
                return render(request, 'user/forgetpassword.html',context)
        else:
            context = {
                'a':'手机号码错误'
            }
            return render(request,'user/forgetpassword.html',context)
    else:
        return render(request, 'user/forgetpassword.html')


# 修改中心
@sess
def infor(request):
    #  判断是post提交还是get提交
    if request.method == 'POST':
        # 获取post提交的的form表单数据
        r = request.POST
        a=r.get('my_name')
        # 调用form类
        data = Myinfor(r, request.FILES)
        # 验证数据合法性
        if data.is_valid():
            # 清洗数据 处理数据 返回个人中心
            a1 = data.cleaned_data
            a = my_infor.objects.create(**a1)
            # aa=my_infor()
            a.user_img = a1.get('user_img')
            a.save()
            return redirect('用户:个人中心')
        else:
            # 数据不合法报错
            context = {
                'err': data.errors
            }
            return render(request, 'user/infor.html', context)
    else:
        # 获取get提交的数据 获取session
        re = request.session
        c = re.get('username')
        # 得到用户注册的用户名 id
        xr = User.objects.filter(username=c).first()
        aa = xr.pk
        # 判断修改用户信息表是否有值
        context = {
            'aaa': my_infor.objects.filter(pk=aa),

        }
        return render(request, 'user/infor.html', context)
        # if my_infor.objects.filter(pk=aa):
        #     # 在form表单渲染用户信息表里的数据
        #     context = {
        #         'aaa': my_infor.objects.filter(pk=aa)
        #     }
        #     return render(request, 'user/infor.html', context)
        # else:
        #     # 在form表单渲染用户注册表里的数据,设置为用户昵称 手机号码的默认值
        #     context = {
        #         'xr': xr
        #     }
        #     return render(request, 'user/infor.html', context)


# 个人中心
@sess
def member_user(request):
    a=request.session
    b=a.get('username')
    c=User.objects.filter(username=b).first()
    d=c.pk
    e=my_infor.objects.filter(pk=d).first()
    if e:
        context={
            'e':e
        }
        return render(request, 'user/member.html',context)
    else:
        context={
            'b':b
        }
        return render(request, 'user/member.html',context)


# 上传图片
# def user_img(request):
#     if request.method == 'POST':
#         po = request.POST.get('file')
#         f1 = request.FILES.get(po)
#
#         path = os.path.join(settings.MEDIA_ROOT, 'booktest', f1.name)
#
#         with open(path, 'w') as pic:
#             for p in f1.chunks():
#                 pic.write(p)
#
#         # 保存数据记录到数据库里
#
#         pic1 = my_infor()
#
#         pic1.user_img = 'booktest/{}'.format(f1.name)
#
#         pic1.save()
#         a = request.session
#         xr = User.objects.filter(username=a).first()
#         aa = xr.pk
#         re = my_infor.objects.filter(pk=aa).first()
#         context = {
#             're': re
#         }
#         return render(request, 'user/infor.html', context)
#     else:
#         a = request.session
#         xr = User.objects.filter(username=a).first()
#         aa = xr.pk
#         re = my_infor.objects.filter(pk=aa).first()
#         context = {
#             're': re
#         }
#         return render(request, 'user/infor.html', context)

# 验证码
def user_code(request):
    if request.method == 'POST':
        sj = request.POST.get('username','')
        resj = re.compile('^1[3-9]\d{9}$')
        re_sj = re.search(resj, sj)
        if re_sj:
            codesj = "".join([str(random.randint(0, 9)) for _ in range(4)])
            # print([str(random.randint(0, 9)) for _ in range(4)])
            # print(codesj)
            a=get_redis_connection("default")
            a.set(sj,codesj)
            a.expire(sj,180)
            __business_id = uuid.uuid1()
            # 信息
            params = "{\"code\":\"%s\",\"product\":\"李厚江\"}" % codesj
            send_sms(__business_id, sj, "注册验证", "SMS_2245271", params)
            return JsonResponse({"ok": 1})
        else:
            return JsonResponse({'err': 0, "erra": "cw"})
    else:
        return JsonResponse({'err': 0, "erra": "请求方式错误"})



# 收货地址

def address_show(request):

    return render(request,'user/gladdress.html')


# 添加收货地址
@sess
def address(request):
    userid=request.session.get('id')
    if request.method=='POST':
        data=request.POST
        # data["userid"]=userid
        re=Addressform(data)
        if re.is_valid():
            cdata=re.cleaned_data
            User_Address.objects.create(**cdata)
            return redirect('用户:收货地址')
        else:
            context={
                'err':re.errors
            }
            return render(request, 'user/address.html',context)
    else:
        context = {
            'id': userid
        }
        return render(request,'user/address.html',context)


