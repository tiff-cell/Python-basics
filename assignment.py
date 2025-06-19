#A python program that checks whether a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number,"Is an even number")
else:
    print(number,"Is an odd number")

#Apython program that checks whether a letter is a vowel or consonant

letter = input("Enter a single letter: ")

if letter or [ "a","b","c","d","e"]:
    print(letter,"Is a vowel")
else:
    print(letter,"Is a consonant")

#Apython program that returns the perimeter of a rectangle

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
perimeter = 2* (length + width)
print("The perimeter of the rectangle",perimeter)