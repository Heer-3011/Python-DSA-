from numpy import genfromtxt
csv_data = genfromtxt('customers-100.csv', delimiter=',') 
print(csv_data)