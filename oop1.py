
class dog:

    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed =breed
        self.age =age
        self.color=color

    def sound(self):
          print(self.name,"Is barking")

dog1 = dog("Victory","German shepherd",5,"White")
print(dog1.name)
print(dog1.sound())

dog2 =dog("Braxton","Siberian husky",3,"Brown")
print(dog2.breed)
print(dog2.sound())

dog3 =dog("Abigael"," Chihuahua",5,"Grey")
print(dog3.color)
print(dog3.sound())
