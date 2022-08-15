from asyncio import exceptions
from dataclasses import field
from enum import unique
from socket import fromshare
from django import forms
import reviews.models
from django.contrib.auth.hashers import check_password
from argon2 import PasswordHasher

class LoginForm(forms.Form):
    id = forms.CharField(
        label="아이디",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "id" : "id",
            }
        ),
        error_messages={
            "required" : "아이디를 입력해주세요."}
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

    def clean(self):
        cleaned_data = super().clean()

        id = cleaned_data.get('id')
        pwd = cleaned_data.get('pwd')
        
        if id and pwd:
            try:
                user = reviews.models.User.objects.get(id = id)
            except reviews.models.User.DoesNotExist:
                return self.add_error("id", "아이디가 존재하지 않습니다.")

            try:
                PasswordHasher().verify(user.pwd, pwd)
            except exceptions.VerifyMismatchError:
                return self.add_error("pwd", "비밀번호가 틀렸습니다.")
            
            self.id = id

            '''
            if not check_password(pwd, user.pwd):
                print(pwd, user.pwd)
                return self.add_error("pwd", "비밀번호가 틀렸습니다.")
            else:
                self.id = id
            '''

