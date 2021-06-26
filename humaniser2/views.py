from django.http import HttpResponse

from humaniser2.humaniser import random_person

def hello(request, s):
  return HttpResponse(f'Hello, {s} world!')

def stranger(request):
  stranger=random_person()
  print(stranger)
  return HttpResponse(stranger)