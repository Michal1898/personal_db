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
    n=random_person(True,18, 60, 10)
    #print(n)
    # n=requests.get('https://humaniser2.herokuapp.com/?sex=female&count=10')
    #n=n.json()
    for x in range(len(n)):
      m=n[x]
      print(m)
      firstname = m.get("firstname")
      surname = m.get("surname")
      gender = m.get("gender")
      birth_day = m.get("day_of_birth")
      birth_month = m.get("month_of_birth")
      birth_year = m.get("year_of_birth")

      city = m.get("city")
      street = m.get("street")
      # if street =="":
      #   street = city
      house_no = m.get("house_no")
      plz = m.get("plz")
      print(firstname, surname, gender, birth_day, birth_month, birth_year, city, street, house_no, plz)
      person_obj=Person(
        firstname = firstname,
        surname = surname,
        gender = gender,
        birth_day = birth_day,
        birth_month = birth_month,
        birth_year = birth_year,
        city = city,
        street = street,
        house_no = house_no,
        plz = plz)

      person_obj.save()
      print(person_obj)
    return render(
    request, template_name='person_list_1.html' ,
    context={'people' : Person.objects.all()}
    )


class PeopleListView(ListView):
  Person.objects.all().delete()
  n=requests.get('https://humaniser3.herokuapp.com/?sex=male&count=20&min=5&max=7')
  n=n.json()

  for x in range(len(n)):
    m = n[x]
    print(m)
    firstname = m.get("firstname")
    surname = m.get("surname")
    gender = m.get("gender")
    birth_day = m.get("day_of_birth")
    birth_month = m.get("month_of_birth")
    birth_year = m.get("year_of_birth")
    city = m.get("city")
    street = m.get("street")
    if street == "":
      street = city
    house_no = m.get("house_no")
    plz = m.get("plz")
    print(firstname, surname, gender, birth_day, birth_month, birth_year, city, street, house_no, plz)
    person_obj = Person(
      firstname=firstname,
      surname=surname,
      gender=gender,
      birth_day=birth_day,
      birth_month=birth_month,
      birth_year=birth_year,
      city=city,
      street=street,
      house_no=house_no,
      plz=plz)

    person_obj.save()




  template_name = 'person_list_2.html'
  model = Person