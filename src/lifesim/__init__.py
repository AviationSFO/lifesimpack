# Life simulator module for python by Steven Weinstein on 2-9-2022 (Py ver >= 3.6.0)
# Version v1.1.0
class AyoUrExceptionallyExistent(Exception):
    pass
class AyoUrFatBro(AyoUrExceptionallyExistent):
    pass
class AyoUrTallBro(AyoUrExceptionallyExistent):
    pass
class AyoUrShortBro(AyoUrExceptionallyExistent):
    pass
class AyoUrOldBro(AyoUrExceptionallyExistent):
    pass
class AyoKilledADeadGuy(AyoUrExceptionallyExistent):
    pass
class Person:
    def __init__ (self, name, height, weight, age = 0, alive = True):
        self.fullname = name
        self.firstname = name.split(" ")[0]
        self.lastname = name.split(" ")[1]
        self.age = age
        self.height = height
        self.weight = weight
        self.alive = alive
    def ageup (self):
        self.age = int(self.age)+1
        if self.age >= 420:
            self.kill()
            raise AyoUrOldBro("Wassup, old man, ur dead now")
    def grow (self, interval = 1):
        height = self.height
        self.height = int(height)+int(interval)
        if self.height <= 0:
            self.kill()
            raise AyoUrShortBro("ayo ur short ngl")
        if self.height >= 3421:
            self.kill()
            raise AyoUrTallBro("ayo ur kinda tall tbh")
    def enfatten (self, interval = 1):
        self.weight = int(self.weight)+int(interval)
        if (self.weight > 69420):
            self.kill()
            raise AyoUrFatBro("ayo ur fat bro")
    def kill (self):
        if self.alive:
            self.alive = False
        else:
            raise AyoKilledADeadGuy("AyoKilledADeadGuy")
        print(f"Oops, {self.fullname} is now dead. Have fun!")
