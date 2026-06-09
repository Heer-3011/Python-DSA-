# MRO means the order in which Python searches for a method when a class has more than one parent
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro()) 