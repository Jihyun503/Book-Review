"""bookreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import home.views
import reviews.views
import common.views
import bestseller.views
import schedule.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.index, name = 'index'),
    path('write/', reviews.views.writeReview, name = 'review_write'),
    path('review/', reviews.views.reviewList, name = 'review'),
    path('review/detail/<int:pk>/', reviews.views.reviewDetail, name = 'review_detail'),
    path('review/detail/<int:pk>/delete/', reviews.views.reviewDelete, name = 'review_delete'),
    path('review/detail/<int:pk>/modify/', reviews.views.reviewModify, name = 'review_modify'),
    path('best/', bestseller.views.bestSellerList, name = 'best'),
    path('signup/', common.views.signup, name = 'signup'),
    path('login/', common.views.login, name = 'login'),
    path('logout/', common.views.logout, name = 'logout'),
    path('freeboard/', reviews.views.reviewList, name = 'freeboard'),
    path('schedule/', schedule.views.scheduleList, name = 'schedule'),
    path('scheduleWrite/', schedule.views.scheduleWrite, name = 'schedule_write'),
    path('schedule/<int:pk>/modify/', schedule.views.scheduleModify, name = 'schedule_modify'),
    path('schedule/<int:pk>/delete/', schedule.views.scheduleDelete, name = 'schedule_delete'),
    path('summernote/', include('django_summernote.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
