# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # boards = Board.objects.all()
    return render(request, 'home.html')


def sample(request):
    # boards = Board.objects.all()
    return render(request, 'sample.html')


def index(request):
    return HttpResponse("Hello, world. I am creating the hamro pustak bhandar.")
