from dataclasses import field
from enum import unique
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import *
from .widgets import *
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget


# 리뷰게시판

class ReviewWriteForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
            }
        ),
    )

    contents = SummernoteTextField()
    
    meta_json = forms.CharField(
        label="별점",
        required=True,
        widget=starWidget
    )

    class Meta:
        model = Board
    
        fields = [
            'title',
            'contents',
            'meta_json'
        ]

        widgets = {
            'contents' : SummernoteWidget(),
            'meta_json' : starWidget,
        }
    
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        contents = cleaned_data.get('contents', '')
        meta_json = cleaned_data.get('meta_json', '')

        if title == '':
            return self.add_error("title", "제목을 입력해주세요.")
        elif contents == '':
            return self.add_error("contents", "내용을 입력해주세요.")
        elif meta_json == 0:
            return self.add_error("meta_json", "별점을 선택해주세요.")
        else:
            self.title = title
            self.contents = contents
            self.meta_json = meta_json


# 별점만 표시하기 위한 폼
class ScopeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.val = kwargs.pop('value')
        super().__init__(*args, **kwargs)
        self.fields['scope'].widget.attrs.update({'value': self.val})
        
    scope = forms.CharField(
        label="별점",
        required=True,
        widget=starWidget(
            attrs={
                "readonly" : "true",
                "class" : "form-control"
            }
        ),
    )
    



