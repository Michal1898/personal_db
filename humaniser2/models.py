from django.db.models import Model, CharField, DateField, IntegerField, BooleanField


class Person(Model):
    firstname = CharField(max_length=30, default=None)
    surname = CharField(max_length=30, default=None)
    gender = BooleanField(default=None)
    birthdate = DateField(default=None)
    city = CharField(max_length=50, default=None)
    street = CharField(max_length=50, default=None)
    house_no = IntegerField(default=None)
    plz = IntegerField(default=None)

    def __str__(self):
        person_label = f"{self.firstname} {self.surname} from {self.city}."
        return person_label


from django.db import models

# Create your models here.
