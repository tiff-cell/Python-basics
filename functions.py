#1. Builtin functions/Standard Library Function

x = max(76,89,54,90,32)
print("The maximum number is", x)

y = min(86,48,68,25)
print("The min number is", y)

z= pow(7,3)
print("the power of 7 is",z)

#User-Defined Functions

def greeeting ():
    print("Hello world!")
greeeting() #Calling a Function

def school():
    print("My coding school is eMobilis")
school()

#Parameters and Argument

def add(num1, num2 ):
    print(num1+num2)
add(10,12)

def student(fullname,course,gender):
    print(fullname,course,gender)
student("Mary Kagema ","mit","female")

def employee(Fullname,email,age,position,salary,marriagestatus):
    print(Fullname,email,age,position,salary,marriagestatus)
employee("Martha Osiya","ashirawi@gmail.com","56","CEO","850,000","Married")
employee("Maryanne Osiya","maryannei@gmail.com","35","Managing Director","500,00","Married")
employee("Hannah Osiya","hannah@gmail.com","33","Chief of Operation","250,000","Single")
employee("Stephannie Osiya","stephannie@gmail.com","28","Project Manager"," 300,000","Married")
employee("Mitchell Osiya","mitchell@gmail.com","26","Chief Technology Officer"," 350,000",'Single')
