from dataclasses import field
from enum import unique
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import *


# 독서 일정

class ScheduleWriteForm(forms.ModelForm):
    title = forms.CharField(
        label="책 제목",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
            }
        ),
    )

    contents = forms.CharField(
        label="한줄 코멘트",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
            }
        ),
    )

    start_date = forms.DateField(
        label="시작날짜",
        required=True,
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control', 
                'placeholder': 'Select a date',
                'type': 'date'
            }
        ),
    )

    end_date = forms.DateField(
        label="마감날짜",
        required=True,
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control', 
                'placeholder': 'Select a date',
                'type': 'date'
            }
        ),
    )

    class Meta:
        model = Schedule
    
        fields = [
            'title',
            'contents',
            'start_date',
            'end_date'
        ]
        '''
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }),
                }
        '''
    
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        contents = cleaned_data.get('contents', '')
        start_date = cleaned_data.get('start_date', '')
        end_date = cleaned_data.get('end_date', '')

        if title == '':
            return self.add_error("title", "제목을 입력해주세요.")
        elif start_date == '':
            return self.add_error("start_date", "마감날짜를 선택해주세요.")
        elif end_date == '':
            return self.add_error("end_date", "마감날짜를 선택해주세요.")
        else:
            self.title = title
            self.contents = contents
            self.start_date = start_date
            self.end_date = end_date
        
