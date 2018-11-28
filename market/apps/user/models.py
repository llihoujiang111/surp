from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
# 调用基类
from db.base_model import BaseModel


#  创建一个用户登录表继承与基类
class User(BaseModel):
    username = models.CharField(max_length=11, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='用户密码')


#  创建一个用户信息表继承与基类 和用户登录表是一对多的关系一个用户id查询一条数据
class my_infor(BaseModel):
    # 设置性别列表在字段上使用choices属性默认为男
    sex_list = (
        (1, "男"),
        (2, '女')
    )
    my_name = models.CharField(max_length=11, verbose_name='用户昵称')
    sex = models.IntegerField(choices=sex_list, default=1, verbose_name='用户性别')
    my_data = models.DateField(blank=True, verbose_name='生日')
    my_school = models.CharField(max_length=10, verbose_name='学校')
    my_address = models.CharField(max_length=50, verbose_name='用户地址')
    my_from = models.CharField(max_length=50, blank=True, verbose_name='用户家乡')
    my_tel = models.CharField(max_length=11, verbose_name='用户电话')
    user = models.ForeignKey(to='User', verbose_name='关联用户注册表')
    user_img = models.ImageField(upload_to='booktest', default='images/infortx.png', verbose_name='头像')



# 创建收货地址
class User_Address(BaseModel):
    hcity=models.CharField(max_length=20,verbose_name='省')
    hproper=models.CharField(max_length=20,verbose_name='市')
    harea=models.CharField(max_length=20,null=True,blank=True,verbose_name='区')
    add_name=models.CharField(max_length=11,verbose_name='收货人')
    add_tel=models.CharField(max_length=11,verbose_name='收货电话',validators=[(RegexValidator(r'^1[3-9]\d{9}$','手机格式错误'))])
    add_detailed=models.CharField(max_length=255,verbose_name='详细地址')
    user=models.ForeignKey(to='User',verbose_name='用户id')
    isdefault=models.BooleanField(default=False,verbose_name='默认选中')

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.add_name
