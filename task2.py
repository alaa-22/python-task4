import re

from django.core.mail import send_mail


class Person:
    mood = ["happy", "lazy", "tired"]
    healthrate = ""

    def __init__(self, name, money, ):
        self.name = name
        self.money = money

    def sleep(self):
        sleeptime = int(input("enter sleep time "))
        if sleeptime == 7:
            self.mood = "happy"
        elif sleeptime > 7:
            self.mood = "lazy"
        elif sleeptime < 7:
            self.mood = "tired"

    def eat(self):
        meals = int(input("enter meals "))
        if meals == 3:
            self.healthrate = "100%"
        elif meals == 2:
            self.healthrate = "75%"
        elif meals == 1:
            self.healthrate = "50%"

    def buy(self):
        item = int(input("please enter num of item"))
        self.money = self.money - (10 * item)

    def getdata(self):
        print(f"""
        name = {self.name}
        money = {self.money}
        mood = {self.mood}
        healthrate = {self.healthrate} 
        """)


class Employee(Person):

    def __init__(self, name, money, id, car, email, salary, distancetowork):
        super().__init__(name, money)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distancetowork = distancetowork

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            self.email = email
        else:
            print("Invalid Email")

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, salary):
        if salary > 1000:
            self.salary = salary
        else:
            print("salary is smaller than 1000")

    def work(self):
        work = int(input("enter work time "))
        if work == 8:
            self.mood = "happy"
        elif work < 8:
            self.mood = "lazy"
        elif work > 8:
            self.mood = "tired"

    def drive(self):
        pass

    def reful(self):
        pass

    def send_mail(self):
        mail = input("please enter mail ypu wont to send to")
        send_mail("subject", "message", self.email, mail)

    """
    def getdata(self):
        print(f'''
            name = {self.name}
            money = {self.money}
            mood = {self.mood}
            healthrate = {self.healthrate} 
            email= {self.email}
            salary = {self.salary}
            distanceTowork ={self.distancetowork}
            '''')"""


class office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass


class Car:
    def __init__(self, name, fuelrate, velocity):
        self.name = name

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if velocity >= 0 and velocity <= 200:
            self.__velocity = velocity
        else:
            print("invalid velocity")

    @property
    def fuelrate(self):
        return self.fuelrate

    @fuelrate.setter
    def fuelrate(self, fuelrate):
        if fuelrate <= 100 and fuelrate >= 0:
            self.fuelrate = fuelrate
        else:
            print("invalid fuel rate")

    def run(self):
        pass

    def stop(self):
        pass
'''
    def getcar(self):
        print(f"""
        car name = {self.name}
        car fuelRate = {self.fuelrate}
        car speed = {self.velocity}
        """)'''


