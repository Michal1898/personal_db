from django.db.models import Model, CharField, DateField, IntegerField, BooleanField


class Person(Model):
    firstname = CharField(max_length=30, default=None)
    surname = CharField(max_length=30, default=None)
    gender = BooleanField(default=None)
    birth_day = IntegerField(default=None, blank=True, null=True)
    birth_month = IntegerField(default=None, blank=True, null=True)
    birth_year = IntegerField(default=None, blank=True, null=True)
    city = CharField(max_length=50, default=None, blank=True, null=True)
    street = CharField(max_length=50, default=None, blank=True, null=True)
    house_no = IntegerField(default=None)
    plz = IntegerField(default=None)

    def __str__(self):
        person_label = f"{self.firstname} {self.surname} from {self.city}."
        return person_label


