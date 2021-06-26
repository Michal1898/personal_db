import csv
import datetime
import random
from random import choice, randrange, getrandbits
from datetime import timedelta, date
from random import shuffle
from dateutil.relativedelta import relativedelta
import os
from radar import random_datetime

FEMALE = True
MALE = False

def random_person(sex=FEMALE, age_min = 1, age_max = 99, count=1):
    person={}
    current_date = date.today()
    start_date=current_date-relativedelta(years=age_max)
    end_date=current_date-relativedelta(years=age_min)

    gender = sex

    humaniser_py_path=os.path.dirname(os.path.realpath(__file__))

    if gender==FEMALE:
        first_names_file = os.path.join(humaniser_py_path, "names_cr","krestni_zeny.csv")
        surnames_file= os.path.join(humaniser_py_path, "names_cr","prijmeni_zeny_1.csv")

    else:
        first_names_file = os.path.join(humaniser_py_path, "names_cr","krestni_muzi.csv")
        surnames_file= os.path.join(humaniser_py_path, "names_cr","prijmeni_muzi_1.csv")

    with open(first_names_file, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    first_names_list=data[:150]

    with open(surnames_file, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    surnames_list=data[:150]

    addresses=[]
    address_folder=os.path.join(humaniser_py_path, "addresses_cr")
    for adr_index in range(1,8):
        addr_file_name="adr_" + str(adr_index) + ".csv"
        addr_file=os.path.join(address_folder, addr_file_name)
        with open(addr_file, encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
            addresses.extend(data[1:])

    human_list=[]
    for c in range(0,count):
        person= {}
        person["gender"] = gender

        random_first_name=choice(first_names_list)
        person["firstname"] = random_first_name[1]

        random_surname = choice(surnames_list)
        person["surname"] = random_surname[1]

        random_date = random_datetime(
            start=start_date,
            stop=end_date
        )

        person["day_of_birth"]=random_date.day
        person["month_of_birth"]=random_date.month
        person["year_of_birth"]=random_date.year

        random_address=choice(addresses)
        random_address = random_address[0]
        random_address=random_address.split(";" , -1)

        person["city"] = random_address[0]
        person["street"] = random_address[1]
        person["house_no"] = random_address[2]
        person["plz"] = random_address[3]

        #print (person)
        human_list.append(person)

    #print(human_list)
    return human_list

if __name__ == "__main__":
    # execute only if run as a script
    import json
    a=random_person(MALE,1,99,200)
    shuffle(a)
    #print(a)
    print(64*"*")

    b=random_person(FEMALE,0,100,200)
    shuffle(b)
    #print(b)
    c=a+b
    print(64*"*")
    print(c)
    print(64*"*")
    shuffle(c)
    print(c)
    d={}
    for e in c:
        f=e.get("birthdate")
        birth_day=str(f.day)
        birth_month=str(f.month)
        birth_year=str(f.year)
        f=birth_day + "-" + birth_month + "-" + birth_year
        e["birthdate"]=f

    print(c)
    with open("person_db.json", 'w') as out_file:
        json.dump(c, out_file, indent=2)


