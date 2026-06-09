class Age:
    def __get__(self, obj, objtype):
        print("getting values....")
        return obj._age


    def __set__(self, obj, value):
        print("setting values....")
        if value < 0:
            raise ValueError("Age cannot be negative")
        obj._age = value


class Person:
    age = Age()


p = Person()
p.age =22
print(p.age)