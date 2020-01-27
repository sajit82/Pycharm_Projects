# Program to call a function
def test_function():
    print("This is called from a functionsss")
def greet():
    return ("Hello")

print("Hello")
test_function()

print(greet(),"Sajit")

def stuff():
    print('Hello')
   # return
    print('World')

stuff()

def computepay(h,r):
    if h>40:
       gp= (40*r) + ((h-40)*(1.5*r))
    else:
       gp = h*r
    return gp

hrs = input("Enter Hours:")
rate= input("Enter Rate:")
hr = float(hrs)
ra =float(rate)
p = computepay(hr,ra)
print("Pay",p)