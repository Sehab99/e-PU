from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        return redirect('courses')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('courses/')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'index.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.user.is_authenticated:
        return redirect('courses')
    else:
        if request.method == 'POST':
            form = Registration(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = Registration()
        context = {'form': form}
        return render(request, 'register.html', context)


@login_required(login_url='index')
def courses(request):
    courses = Courses.objects.all().order_by('-id')
    form = AddCourse()

    if request.method == 'POST':
        form = AddCourse(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form, 'courses': courses}
    return render(request, 'courses.html', context)


@login_required(login_url='index')
def topics(request, courseid):
    courses = Courses.objects.get(id=courseid)
    topics = courses.topics_set.all()
    form = AddTopic(initial={'courses': courses})

    if request.method == 'POST':
        form = AddTopic(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'courses': courses,
        'topics': topics,
        'video': video
    }
    return render(request, 'topics.html', context)


@login_required(login_url='index')
def video(request, courseid, topicid):
    courses = Courses.objects.get(id=courseid)
    topics = courses.topics_set.all()
    video = courses.topics_set.get(id=topicid)
    context = {'courses': courses, 'topics': topics, 'video': video}
    return render(request, 'video.html', context)
