import random

a = int(input("Money = "))
d = int(input("Days = "))

arr=[]
print(f"Цены за {d} дней: ")

for i in range(d):
    price = random.randint(5,15)
    print(price)
    arr.append(price)
print("Можно купить пончиков: ", (a*d)//min(arr))
