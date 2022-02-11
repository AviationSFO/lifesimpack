import lifesim as ls
zachary = ls.Person("Zachary Sakowitz", 60, 100, age = 13)
samson = ls.Person("Ari Samson", 58, 135, 12)
samson.kill()
dannyboi = ls.Person("Daniel Kavalerchik", 57, 140, 12)
while True: 
    dannyboi.grow()
    dannyboi.ageup()
    print(dannyboi.height)
    print(dannyboi.age);
