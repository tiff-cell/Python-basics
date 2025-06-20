#Object- Oriented Programming

#Properties/Attributes

class student:
    name= "Eliud"
    gender = "Male"
    age = 34

    def study(self):
        print(" Student is studying")
    def movement(self):
        print("Student is walking")
#Creating an Object
student1 = student()
student1.movement()
print(student1.name)

student2= student
print(student2.name)