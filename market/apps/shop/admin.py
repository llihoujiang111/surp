from django.contrib import admin

# Register your models here.
from shop.models import Shop_sku, Shop_sort, Shop_img, Shop_spu, Shop_unit, Index_active, Active_zone, Active_shop, \
    Index_lunbo


class Shop_imgAdminInline(admin.TabularInline):
    model = Shop_img # 关联子对象
    extra = 5 # 额外编辑两个子对象




# 添加sku商品详情
@admin.register(Shop_sku)
class SKU_admin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','sku_name','sku_price','sku_stock','sku_sale','sku_sj','show_logo']
    list_display_links = ['id','sku_name','sku_price','sku_stock','sku_sale','sku_sj']
    list_filter = ['sku_name']
    search_fields = ['sku_name']

    # fields = ['name','parent_id']
    fieldsets = (
        ("基本信息",{'fields':("sku_name",)}),
        ("详细信息",{'fields':("sort_id",'sku_intro')}),
        ("价格",{'fields':("sku_price",)}),
        ("单位",{'fields':("sort_unit",)}),
        ("库存",{'fields':("sku_stock",)}),
        ("销量",{'fields':("sku_sale",)}),
        ("商品logo",{'fields':("sku_logo",)}),
        ("是否上架",{'fields':("sku_sj",)}),
        ("sup商品",{'fields':("spu_id",)}),
    )

    inlines = [Shop_imgAdminInline]


#spu商品表
@admin.register(Shop_spu)
class SPU_admin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','spu_name','spu_contend']
    list_display_links = ['id','spu_name','spu_contend']
    list_filter = ['spu_name']
    search_fields = ['spu_name']

    # fields = ['name','parent_id']
    fieldsets = (
        ("基本信息",{'fields':("spu_name",)}),
        ("详细信息",{'fields':("spu_contend",)}),
    )

#商品分类
@admin.register(Shop_sort)
class SORT_admin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','sort_name','sort_intro']
    list_display_links = ['id','sort_name','sort_intro']
    list_filter = ['sort_name']
    search_fields = ['sort_name']

    # fields = ['name','parent_id']
    fieldsets = (
        ("基本信息",{'fields':("sort_name",)}),
        ("详细信息",{'fields':("sort_intro",)}),
    )

# 单位表
@admin.register(Shop_unit)
class UNIT_admin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','unit']
    list_display_links = ['id','unit']
    list_filter = ['unit']
    search_fields = ['unit']

    # fields = ['name','parent_id']
    fieldsets = (
        ("基本信息",{'fields':("unit",)}),
    )
# 首页活动
@admin.register(Index_active)
class ACTIVE_admin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','active','active_img','active_url']
    list_display_links = ['id','active','active_img','active_url']
    list_filter = ['active']
    search_fields = ['active']

    # fields = ['name','parent_id']
    fieldsets = (
        ("基本信息", {'fields': ("active",)}),
        ("详细信息", {'fields': ("active_img","active_url")}),
    )


class ZONEAdminInline(admin.TabularInline):
    model = Active_shop  # 关联子对象
    extra = 3  # 额外编辑两个子对象

# 活动专区
@admin.register(Active_zone)
class ZONE_admin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','zone','zone_contend','zone_order','zone_sj']
    list_display_links = ['id','zone','zone_contend','zone_order','zone_sj']
    list_filter = ['zone']
    search_fields = ['zone']

    # fields = ['name','parent_id']
    fieldsets = (
        ("基本信息", {'fields': ("zone",)}),
        ("详细信息", {'fields': ("zone_contend","zone_order",'zone_sj')}),
    )

    inlines = [ZONEAdminInline,]


@admin.register(Index_lunbo)
class ACTIVE_admin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id','pic_name','pic','pic_url']
    list_display_links = ['id','pic_name','pic','pic_url']
    list_filter = ['pic_name']
    search_fields = ['pic_name']

    # fields = ['name','parent_id']
    fieldsets = (
        ("基本信息", {'fields': ("pic_name",)}),
        ("详细信息", {'fields': ("pic","pic_url",'order')}),
    )