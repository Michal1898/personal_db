from django.http import HttpResponse

from humaniser2.humaniser import random_person
from humaniser2.models import Person

import datetime
import requests

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from random import getrandbits

def hello(request, s):
  return HttpResponse(f'Hello, {s} world!')

def stranger(request):
  stranger=random_person()
  print(stranger)
  response=HttpResponse(stranger, content_type="text/plain")
  response['Content-Disposition'] = 'attachment; filename=jmeno_souboru.txt'

  return response

class PeopleView(View):
  def get(self, request):
    Person.objects.all().delete()
    n=random_person(False,18, 60, 10)
    #print(n)
    # n=requests.get('https://humaniser2.herokuapp.com/?sex=female&count=10')
    #n=n.json()
    for x in range(len(n)):
      m=n[x]
      print(m)
      firstname = m.get("firstname")
      surname = m.get("surname")
      gender = m.get("gender")
      birthdate = m.get("birthdate")
      city = m.get("city")
      street = m.get("street")
      if street =="":
        street = city
      house_no = m.get("house_no")
      plz = m.get("plz")
      print(firstname, surname, gender, birthdate, city, street, house_no, plz)
      person_obj=Person(
        firstname = firstname,
        surname = surname,
        gender = gender,
        birthdate = datetime.date.today(),
        city = city,
        street = street,
        house_no = house_no,
        plz = plz)

      person_obj.save()

    return render(
    request, template_name='person_list_1.html' ,
    context={'people' : Person.objects.all()}
    )

class PeopleListView(ListView):
  Person.objects.all().delete()
  n=requests.get('https://humaniser2.herokuapp.com/?sex=female&count=10')
  n=n.json()

  for x in range(len(n)):
    m = n[x]
    print(m)
    firstname = m.get("firstname")
    surname = m.get("surname")
    gender = m.get("gender")
    birthdate = m.get("birthdate")
    city = m.get("city")
    street = m.get("street")
    if street == "":
      street = city
    house_no = m.get("house_no")
    plz = m.get("plz")
    print(firstname, surname, gender, birthdate, city, street, house_no, plz)
    person_obj = Person(
      firstname=firstname,
      surname=surname,
      gender=gender,
      birthdate=datetime.date.today(),
      city=city,
      street=street,
      house_no=house_no,
      plz=plz)

    person_obj.save()

  template_name = 'person_list_2.html'
  model = Person