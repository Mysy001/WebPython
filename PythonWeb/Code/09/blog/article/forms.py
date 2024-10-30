from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='姓名',
        required=True,
        min_length=3,
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "请输入用户名"
        }),
        error_messages={
            'required': '用户名不能为空',
            'min_length': '长度不能小于3个字符',
            'max_length': '长度不能超过10个字符',
        }
    )

    password = forms.CharField(
        label='密码',
        required=True,
        min_length = 6,
        max_length = 50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-0',
            'placeholder':"请输入密码"
        }),
        error_messages={
            'required': '用户名不能为空',
            'min_length': '长度不能少于6个字符',
            'max_length': '长度不能超过50个字符',
        }
    )


