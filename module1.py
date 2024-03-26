#VARIANT 2
#1
n=int(input("Sisestage arv vahemikus 1 kuni 9: ")) 
for i in range(n):
    print("(\_/)", end=" ")
    if i<n-1:
        print(" ", end=" ")
print( )
for i in range(n):
        print("(o o)", end=" ")
        if i<n-1:
            print(" ", end=" ")
print( )
for i in range(n):
    print("/ | \*", end="")
    if i<n-1:
        print(" ", end=" ")
 #2
L=int(input("Sisestage number L: ")) 
summ=0 
for i in range(L+1): 
    summ += i 
print("Numnbrite summa 0 kuni L on: ", summ) 
 #3
from random import *
number=randint(1,100)
katsed=10
while katsed>0:
    külaline=int(input("Arva ära arv vahemikus 1 kuni 100: "))
    if külaline==number:
        print("Palju õnne, arvasite numbri ära! ")
        break
    else:
        katsed -=1
        print(f"Vale! Teil on jäänud {katsed} katset. ")
        if katsed==0:
            print(f"Vabandust, olete andnud endast parima. Varjatud number oli {number}. ")
            veelkord=input("Kas sa tahad arvata? ").lower()
            if veelkord.lower()=="ei":
                break
            else:
                katsed=10
 #4
n=int(input("Sisestage number:  ")) #Мы спрашиваем у пользователя номер
vastastikune_arv=0  #Инициализировать обратную переменную
while n>0: 
    ülejäänud=n%10 #Получение остатка при делении числа на 10
    vastastikune_arv=(vastastikune_arv*10)+ülejäänud #Умножьте обратное на 10 и добавьте остаток
    n=n/10 #Разделите исходное число на 10, чтобы перейти к следующему числу
    print("Vastastikune arv:", vastastikune_arv) #Извлечь текущую инверсию
#5
n=int(input("Sisesta number")) #запрос чисел
summa=0 #переменная сумма
korrutis=1 #переменный продукт
while n>0:
    praegune_number=n%10
    summa+=praegune_number  
    korrutis*=praegune_number 
    n=n//10
print("summa:", summa) 
print("korrutis:", korrutis) 

