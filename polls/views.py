# Create your views here.
from django.shortcuts import render
from polls.models import Poll

def home(request):
    data = {}
    data['name'] = 'junghan'
    return render(request, 'home.html', data)

def polls(request):
    data = {}
    data['polls'] = Poll.objects.all()
    return render(request, 'polls.html', data)
