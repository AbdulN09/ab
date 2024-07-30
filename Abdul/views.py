from django.http import HttpResponse


def sample(request):
    return HttpResponse("hii how are you")
