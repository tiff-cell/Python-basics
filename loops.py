#Loop- repeating something numerous times

#While loop

number = 40

while number <= 45 :
    print(number)
    number+=1
#Decrementing
count = 105
while count >= 100:
    print(count)
    count-=1

#Break and Continue

a= 20
while a<=25:
    print(a)
    if a == 23:
        break
    a += 1

    counter = 35
    while counter <=40:
        if counter == 37:
            counter+= 1
            continue
       print(counter)
    counter += 1




#For Loop

languages = ["Python","c++","Java","PHP"]
for lang in languages:
    print(lang)

for num in range(5):
    print(num)

for x in range(10, 15):
    print(x)

for z in range(10,20):
    print(z)