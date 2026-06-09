class Student: 
    __slots__=['name','age']
    def display(self):
        print(s.name,s.age,s.city)

s = Student()

s.name = "Heer"
s.age = 21

s.city = "Ahmedabad"   # Error
s.display()