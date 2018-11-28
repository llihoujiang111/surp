from django import forms
from django.core import validators
from django.core.validators import RegexValidator

from user.models import my_infor, User_Address


#  创建一个用户注册的form类
class User_form(forms.Form):
    username = forms.CharField(min_length=11, max_length=11,
                               error_messages={'required': '手机号不能为空', 'max_length': ' 用户名最长11',
                                               'min_length': '用户名最短11'},

                               validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式不正确')])
    password = forms.CharField(max_length=15, min_length=6,

                               error_messages={'max_length': '密码最长15', 'min_length': '密码最短6', 'required': '密码不能为空'},

                               validators=[
                                   RegexValidator('^(?![\d]+$)(?![a-zA-Z]+$)(?![!#$%^&*]+$)[\da-zA-Z!#$%^&*]{6,20}$',
                                                  '不能纯数字，纯字母，纯特殊字符,至少包含一个数字和字母')]
                               # 能匹配的组合为：数字 + 字母，数字 + 特殊字符，字母 + 特殊字符，数字 + 字母 + 特殊字符组合，而且不能是纯数字，纯字母，纯特殊字符

                               )
    rpassword = forms.CharField(max_length=15, min_length=6,

                                error_messages={'max_length': '密码最长15', 'min_length': '密码最短6', 'required': '密码不能为空'},

                                validators=[
                                    RegexValidator('^(?![\d]+$)(?![a-zA-Z]+$)(?![!#$%^&*]+$)[\da-zA-Z!#$%^&*]{6,20}$',
                                                   '不能纯数字，纯字母，纯特殊字符,至少包含一个数字和字母')]
                                # 能匹配的组合为：数字 + 字母，数字 + 特殊字符，字母 + 特殊字符，数字 + 字母 + 特殊字符组合，而且不能是纯数字，纯字母，纯特殊字符

                                )
    user_code=forms.CharField(error_messages={
        'required':'请输入验证码'
    })


    #  从新清洗数据来判断两次密码是否一致 如果一样返回清洗后的数据 否则抛出异常
    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        rpassword = data.get('rpassword')
        if password != rpassword:
            raise forms.ValidationError({'rpassword': '两次密码不一致请重新输入'})
        else:
            return data



# class Myinfor(forms.ModelForm):
#     class Meta:
#         model = my_infor
#         fields = '__all__'
#         error_messages = {
#             'my_name':{
#                 'max_lengh=11':'用户名不能超过11位',
#                 'required':'用户名必填'
#         },
#             'my_address':{
#                 'required':'地址必填'
#             },
#             'my_school':{
#                 'required':'学校必填'
#             },
#             'sex':{
#                 'required':'性别必填'
#             }
#
#         }
        # validators=[RegexValidator('^[a-zA-Z]{1}([a-zA-Z0-9_]){4,14}|(^[\u4E00-\uFA29]{1}+[a-zA-Z0-9\u4E00-\uFA29]{2,7})','不能包含特殊字符')]



#  设置填写用户个人信息的form类
class Myinfor(forms.Form):
    my_name=forms.CharField(max_length=12,error_messages={'required':'姓名必填'})
    sex=forms.IntegerField(error_messages={'required':'性别必填'})
    my_data=forms.DateField()
    my_school=forms.CharField(max_length=10,error_messages={'required':'学校必填'})
    my_address=forms.CharField(max_length=50,error_messages={'required':'地址必填'})
    my_from=forms.CharField(max_length=50)
    my_tel=forms.CharField(max_length=11,error_messages={'required':'电话必填'})
    user_id=forms.IntegerField()
    user_img=forms.FileField()


# 收货地址
class Addressform(forms.ModelForm):
    class Meta:
        model=User_Address
        fields=['hcity','hproper','harea','add_name','add_tel','add_detailed','user','isdefault']
        error_messages={
            'hcity':{
                'required':'地址必填',
            },
            'add_name':{
                'required':'姓名必填',
                'max_length=11':'姓名不能超过11个字',
            },
            'add_tel':{
                'required':'电话必填',
            },
            'add_detailed':{
                'required':'详细地址必填',
            },
        }

    def clean(self):
        # 验证如果数据库里地址已经超过6六表报错
        user=self.data.get("userid")
        count = User_Address.objects.filter(user_id=user,is_delete=False).count()
        if count >= 6:
            raise forms.ValidationError( "收货地址最多只能保存6条")
        return self.cleaned_data





