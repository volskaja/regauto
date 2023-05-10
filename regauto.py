from MyModule import *

palgad=[1200,1200,1200,1200,1200]
inimesed=["A","B","C","D","E"]
print(Kustutamine(palgad,inimesed))

#1-Добавить еще несколько человек и зарплат(кол-во говорит пользователь),
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
print(uued_palgad(inimesed, palgad))

#10-Keskmine() - Среднюю зарплату и имя человека ее получающего
palgad=[1200,1200,1200,1200,1200]
inimesed=["A","B","C","D","E"]
print(Keskmine(palgad,inimesed))

#Registreerimine ja autoriseerimine
ll=[]
p=[]
while True:
    print("Регистрация - 1")
    print("авторизация - 2")
    print("Выход - 3")
    print("изменить имя пользователя - 4")
    print("изменить пароль - 5")
    print("Если вы хотите указать ваш пароль - 6")
    valik=input("Напишите номер, который сделает вашу деятельность: ")
    if valik=="1":
         print("Регистрация")
         login,psword=kasutajaandmed(ll,p)
         print(f"Ваш логин ({login}) и пароль ({psword})")
    elif valik=="2":
        print("авторизация") 
        logg,pas_=aut(ll,p)
    elif valik=="3":
        print("До свидания")
        break
    elif valik=="4":
        vananimi=input("Напишите ваше старое имя: ")
        uusnimi=input("Напишите новое имя, которое вы хотите: ")
        uss_login(ll,vananimi,uusnimi)
    elif valik=="5":
        login=input("Напишите ваш логин: ")
        vanasalasõna=input("Введите ваш старый пароль: ")
        uussalasõna=input("Введите ваш новый пароль: ")
        uss_salasõna(ll,p,login,vanasalasõna,uussalasõna)
    elif valik=="6":
        nimiii=input("Напишите ваш логин, у которого вы хотите указать пароль: ")
        nimii(ll,p,nimiii)
    print(ll,p)
