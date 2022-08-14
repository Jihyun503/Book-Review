from dataclasses import field
from socket import fromshare
from django import forms
from .models import *
#from argon2 import PasswordHasher

class joinForm(forms.ModelForm):
    id = forms.CharField(
        label="아이디",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "id" : "id",
            }
        ),
        error_messages={"required" : "아이디를 입력해주세요."}
    )
    pwd = forms.CharField(
        label="비밀번호",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "id" : "pwd",
            }
        ),
        error_messages={"required" : "비밀번호를 입력해주세요."}
    )
    name = forms.CharField(
        label="이름",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "id" : "name",
            }
        ),
        error_messages={"required" : "이름을 입력해주세요."}
    )
    email = forms.EmailField(
        label="이메일",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "id" : "email",
            }
        ),
        error_messages={"required" : "이메일을 입력해주세요."}
    )
    nickname = forms.CharField(
        label="닉네임",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "id" : "nickname",
            }
        ),
        error_messages={"required" : "닉네임을 입력해주세요."}
    )

    fields = [
            'id',
            'pwd',
            'name',
            'email',
            'nickname'
    ]

    class Meta:
        model = User
        fields = [
            'id',
            'pwd',
            'name',
            'email',
            'nickname'
        ]
    
    def clean(self):
        cleaned_data = super().clean()

        id = cleaned_data.get('id')
        pwd = cleaned_data.get('pwd')
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        nickname = cleaned_data.get('nickname')
        
        if len(pwd) < 8:
            return self.add_error("pwd", "비밀번호는 8자 이상으로 입력해주세요.")
        else:
            self.id = id
            self.pwd = pwd
            self.name = name
            self.email = email
            self.nickname = nickname
            


