import lifesim as ls
import time
zachary = ls.Person("Zachary Sakowitz", 60, 100, age = 13)
samson = ls.Person("Ari Samson", 58, 135, 12)
samson.kill()
dannyboi = ls.Person("Daniel Kavalerchik", 57, 140, 12)
while True: 
    dannyboi.ageup(True)
    print(dannyboi.age)
    time.sleep(0.0125)