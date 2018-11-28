from django.db  import models

#  创建一个基类用于保存创建时间和更新时间 是否假删除
class BaseModel(models.Model):
    create_time = models.DateField(auto_now_add=True,verbose_name='创建')
    update_time = models.DateField(auto_now=True,verbose_name='更新时间')
    is_delete=models.BooleanField(default=False,verbose_name='假删除')


    class Meta:
        #说明抽样类,不会被迁移
        abstract=True



