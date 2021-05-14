# coding=utf-8
"""
@auth: xiaobei
@date: 2021/5/11 
@desc:
"""
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

"""
如果要将表单中的数据写入数据库或者修改记录的值，就要让表单继承 ModelForm，如果提交表单后，不会对数据库中的数据做修改，则使用 Form
"""


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        # 一个内部类，声明我们需要的数据模型，使用 fields 来说明我们选用的属性，或者使用 exclude 来排除我们不需要的属性
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        """
        以 clean_ 开头的方法，会在调用表单实例对象的 is_valid() 方法时被执行
        :return:
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", 'photo')

