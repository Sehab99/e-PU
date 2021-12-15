from django.http import HttpResponse
from .forms import *
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def courses(request):
    courses = Courses.objects.all().order_by('-id')
    form = AddCourse()

    if request.method == 'POST':
        form = AddCourse(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form, 'courses': courses}
    return render(request, 'courses.html', context)


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


def video(request, courseid, topicid):
    courses = Courses.objects.get(id=courseid)
    topics = courses.topics_set.all()
    video = courses.topics_set.get(id=topicid)
    context = {'courses': courses, 'topics': topics, 'video': video}
    return render(request, 'video.html', context)
