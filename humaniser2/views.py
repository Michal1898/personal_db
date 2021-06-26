from django.http import HttpResponse


def hello(request, s):
  return HttpResponse(f'Hello, {s} world!')