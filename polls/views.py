from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world ")


def sec(request):
    return HttpResponse("second one ")
