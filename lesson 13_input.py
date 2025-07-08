#name = input("please enter your name:")
#print("privet " + name)

#num1 = input("Enter X: ")
#num2 = input("Enter Y: ")

#summa = int(num1) + int(num2)
#print(summa)

#while True:
#   message = input("Enter Password")
#    if message == 'secret':
#        break
#    print (message + " pass is not correct")
#print ("correct pass " + message)

mylist = []
msg = ""

while msg != 'stop'.upper():
    msg = input ("enter new item, and STOP to finish")
    mylist.append(msg)

print(mylist)