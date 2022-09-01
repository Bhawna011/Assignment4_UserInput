# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
a=float(input (" Enter first side :"))
b=float(input ("Enter second side : "))
c=float(input ("Enter third side : "))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print ("area of a triangle : " , area )