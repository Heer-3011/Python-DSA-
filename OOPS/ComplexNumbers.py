class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def plus(self, c):
        self.real = self.real + c.real
        self.imag = self.imag + c.imag

    def multiply(self, c):
        real_part = self.real * c.real - self.imag * c.imag
        imag_part = self.real * c.imag + self.imag * c.real

        self.real = real_part
        self.imag = imag_part

    def print(self):
        print(self.real, " + i" + str(self.imag), sep="")
r1, i1 = map(int, input().split())
r2, i2 = map(int, input().split())
choice = int(input())

c1 = ComplexNumber(r1, i1)
c2 = ComplexNumber(r2, i2)

if choice == 1:
    c1.plus(c2)
    c1.print()
elif choice == 2:
    c1.multiply(c2)
    c1.print()
else:
    pass 