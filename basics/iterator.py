#iterator object that you can loop over using for, like a list or a tuple
#example: books which alreay have all d
num=[10,11,12,13]

it=iter(num)
print(next(it))

#generator special kind of iterator made using a function and the yield keyword.
#example : netflix episode
def count(num):
    for i in num:
        yield i

num1=count(num)     
print(next(num1)) 