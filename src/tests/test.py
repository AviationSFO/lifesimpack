import lifesim as ls
import time
zachary = ls.Person("Zachary Sakowitz", 60, 100, age = 13)
while True:
    zachary.ageup()
    print(zachary.age)
    time.sleep(0.0125)
