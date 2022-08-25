from asyncio import futures
from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta, datetime
from .models import Schedule
from common.models import User
from .forms import *
from common.decorators import login_required

# Create your views here.

@login_required
def scheduleList(request, **kwargs):
    context = {}
    context['login_session'] = kwargs.get("login_session")
    login_session = request.session.get('user', '')

    # 일단 모든 일정을 가져온 뒤에 목표 날짜가 오늘 날짜보다 이후면 진행중, 목표날짜가 오늘보다 이전날짜면 완료된 일정
    schedules = Schedule.objects.all()
    now = []
    past = []
    future = []

    for schedule in schedules:
        if schedule.start_date > datetime.today() and schedule.end_date > datetime.today():
            future.append(schedule)
        elif schedule.start_date <= datetime.today() and schedule.end_date >= datetime.today():
            now.append(schedule)
        elif schedule.end_date < datetime.today():
            past.append(schedule)

    context['now'] = now
    context['past'] = past
    context['future'] = future
    context['user'] = login_session
    
    return render(request, "schedule_list.html", context)


@login_required
def scheduleWrite(request, **kwargs):
    context = {}
    context['login_session'] = kwargs.get("login_session")

    if request.method == 'GET':
        schedule_form = ScheduleWriteForm()
        context['forms'] = schedule_form
        return render(request, "schedule_write.html", context)

    elif request.method == 'POST':
        schedule_form = ScheduleWriteForm(request.POST)
        
        if schedule_form.is_valid():
            login_session = request.session.get('user', '')
            writer = User.objects.get(id=login_session)
            
            schedule = Schedule(
                writer=writer,
                title=schedule_form.title,
                contents=schedule_form.contents,
                start_date=schedule_form.start_date,
                end_date=schedule_form.end_date
            )
            schedule.save()
            
            return redirect('/schedule')
        else:
            '''
            context['forms'] = join_form
            if join_form.errors:
                for value in join_form.errors.values():
                    context['error'] = value
            '''
            context['forms'] = schedule_form
        return render(request, "schedule_write.html", context)
    
