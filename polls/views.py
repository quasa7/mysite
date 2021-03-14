from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello world.")

def second(request):
  return HttpResponse("Second page!")

def third(request):
  return HttpResponse("Third page?")
