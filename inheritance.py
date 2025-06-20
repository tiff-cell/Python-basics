#Parent Class/Super class/Base Class
class animal:
    def speak(self):
        print("Animal is speaking")
    def eat(self):
        print("Animal is eating")

#Child class/Sub class/Derived class
class dog (animal):
    def barking(self):
        print("Dog is barking")
    def fetch(self):
        print("Dog is fetching a ball")

a = animal()

d = dog()

