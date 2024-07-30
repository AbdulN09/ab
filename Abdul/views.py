from django.http import HttpResponse


def sample(request):
    return HttpResponse("hii how are you")


def sample1(request):
    return HttpResponse("hello i am fine")


def sample2(request):
    return HttpResponse("welcome to python")
