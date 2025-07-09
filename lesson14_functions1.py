

def napechatat_privet():
    """print privetstvie"""
    print("all the best")
    print("hello hello hello")

def aaaa():
    print("AAAA")

print("------------------------------------------------")
napechatat_privet()
napechatat_privet()
aaaa()
print("------------------------------------------------")
def napechatat_privet(name):
    """print privetstvie"""
    print("the best " + name + " of the best")
napechatat_privet("den")
napechatat_privet("vasya")
print("------------------------------------------------")

def summa (x , y):
    print(x+y)
summa(10, 20)
print("+++++++++++++++++++++++++++++++++++++++++")

def summa (x , y):
    return x+y
x = summa (33, 22)
print(x)

print("+++++++++++++++++++++++++++++++++++++++++")

def factorial(x):
    #"""calculate factorial of number X"""
    otvet = 1
    for i in range (1, x + 1):
        otvet = otvet * i
    return otvet
for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))