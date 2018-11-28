from django.conf import settings
from django.db import models

# Create your models here.

# 轮播图片
from db.base_model import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField


# 轮播图
class Index_lunbo(BaseModel):
    pic_name = models.CharField(max_length=20, verbose_name='轮播名字')
    pic = models.ImageField(upload_to='shopbook', default='images/banner.png', verbose_name='轮播图片')
    pic_url = models.URLField(verbose_name='点击图片跳转的地址')
    order = models.IntegerField(verbose_name='排序', default=0)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pic_name


# 商品分类
class Shop_sort(BaseModel):
    sort_name = models.CharField(max_length=50, verbose_name='分类名')
    sort_intro = RichTextUploadingField(verbose_name='分类简介')

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sort_name


# spu商品表
class Shop_spu(BaseModel):
    spu_name = models.CharField(max_length=50, verbose_name='商品名')
    spu_contend = RichTextUploadingField(verbose_name='内容')

    class Meta:
        verbose_name = 'spu商品表'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.spu_name


# 单位表
class Shop_unit(BaseModel):
    unit = models.CharField(max_length=10, verbose_name='商品单位')

    class Meta:
        verbose_name = '单位表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.unit


# sku商品详情

class Shop_sku(BaseModel):
    pricelist = [
        (1, '上架'),
        (0, '下架')
    ]
    sku_name = models.CharField(max_length=50, verbose_name='商品名')
    sku_intro = models.TextField(verbose_name='商品简介')
    sku_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='价格')
    sku_stock = models.IntegerField(verbose_name='库存', default=0)
    sku_sale = models.IntegerField(verbose_name='销量', default=0)
    sku_logo = models.ImageField(upload_to='shop_sku', verbose_name='商品logo')
    sku_sj = models.BooleanField(default=False, choices=pricelist, verbose_name='是否上架')
    spu_id = models.ForeignKey(to=Shop_spu, verbose_name='spu商品id')
    sort_id = models.ForeignKey(to=Shop_sort, verbose_name='分类id')
    sort_unit = models.ForeignKey(to=Shop_unit, verbose_name='单位id')

    def show_logo(self):
        return "<img src='{}{}'/>".format(settings.MEDIA_URL, self.sku_logo)

    show_logo.allow_tags = True
    show_logo.short_description = 'sku_logo'

    class Meta:
        verbose_name = 'sku商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku_name


# 商品相册
class Shop_img(BaseModel):
    img_url = models.ImageField(upload_to='shop', verbose_name='图片')
    sku = models.ForeignKey(to=Shop_sku, verbose_name='sku商品id')

    class Meta:
        verbose_name = '商品相册'
        verbose_name_plural = verbose_name



# 首页活动
class Index_active(BaseModel):
    active = models.CharField(max_length=50, verbose_name='活动名')
    active_img = models.ImageField(upload_to='shop_active', verbose_name='活动图片')
    active_url = models.URLField()

    class Meta:
        verbose_name = '首页活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.active


# 活动专区
class Active_zone(BaseModel):
    zonelist = [
        (1, '上架'),
        (0, '下架')
    ]
    zone = models.CharField(max_length=50, verbose_name='活动专区名')
    zone_contend = RichTextUploadingField(verbose_name='活动描述')
    zone_order = models.IntegerField(verbose_name='排序')
    zone_sj = models.BooleanField(default=False, choices=zonelist, verbose_name='是否上架')

    class Meta:
        verbose_name = '活动专区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zone


# 活动商品
class Active_shop(BaseModel):
    zone_id = models.ForeignKey(to=Active_zone)
    sku_id = models.ForeignKey(to=Shop_sku)

    class Meta:
        verbose_name = '活动商品'
        verbose_name_plural = verbose_name

