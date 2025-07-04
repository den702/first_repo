age = 10

if (age <= 4):
    print ("you baby")
elif (age > 4) and (age < 12):
    print ("you kid")
elif (age >= 12) and (age < 19):
    print ("you teenager")
else:
    print ("you old")
print ("_________________________________________________")

all_cars = ['crysler' , 'dacia' , 'bmw' , 'kia' , 'vw' , 'seat' , 'skoda' , 'lada' , 'audi' , 'ford' , 'chevrolet']
german_cars = ['bmw' , 'vw' , 'audi']

for x in all_cars:
    if x in german_cars:
        print (x + " is german car")
    else:
        print (x + "is not german car")