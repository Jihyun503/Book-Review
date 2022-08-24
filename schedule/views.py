from django.shortcuts import render, redirect, get_object_or_404

from .models import Schedule
#from .forms import *
from common.decorators import login_required

# Create your views here.

@login_required
def scheduleList(request, **kwargs):
    context = {}
    context['login_session'] = kwargs.get("login_session")

    # 일단 모든 일정을 가져온 뒤에 목표 날짜가 오늘 날짜보다 이후면 진행중, 목표날짜가 오늘보다 이전날짜면 완료된 일정
    schedule = Schedule.objects.all()

    context['schedules'] = schedule
    
    return render(request, "schedule_list.html", context)
