def add(x,y):
 return x+y

def subtract(x,y):
 return x-y

def multiply(x,y):
 return x*y

def divide(x,y):
 return x/y

print("Enter the first number:")
x=int(input())
print("Enter the second number:")
y=int(input())
 
print("Enter the operation:")
a=int(input())

if a==1 :
 print(x,"+",y,"=",add(x,y))
elif a==2:
 print(x,"-",y,"=",subtract(x,y))
elif a==3:
 print(x,"x",y,"=", multiply(x,y))
elif a==4:
 print(x,"÷",y,"=",divide(x,y))
else:
 print("Invalid Input")
