from random import *

def Soorteerimine(inimesed,palgad):
    v=int(input("Palk 1-kahened,2-kasvad?"))
    if v==1:
        n=len(palgad) 
        for j in range(0,n-1):
            for k in range(j+1,n):
                if palgad[j] < palgad[k]:
                    abi = palgad[j]
                    palgad[j] = palgad[k]
                    palgad[k] = abi
                    abi = inimesed[j]
                    inimesed[j] = inimesed[k]
                    inimesed[k] = abi
    elif v == 2:
            n = len(palgad)
            for j in range(n - 1):
                for k in range(j + 1, n):
                    if palgad[j] > palgad[k]:
                        abi = palgad[j]
                        palgad[j] = palgad[k]
                        palgad[k] = abi
                        abi = inimesed[j]
                        inimesed[j] = inimesed[k]
                        inimesed[k] = abi  
    print("Имена работников", inimesed)
    print("Зарплаты работников:", palgad) 
    
def Kustutamine(palgad:list,inimesed:list):
    nimi=input("Введите имя: ")
    if nimi in inimesed:
        n=inimesed.count(nimi)
        for j in range(n):
            ind=inimesed.index(nimi)
            inimesed.pop(ind)
            palgad.pop(ind)
    return inimesed,palgad

#1-Добавить еще несколько человек и зарплат(кол-во говорит пользователь),
def uued_palgad(inimesed,palgad):
    nimi=input("Введите имя: ")
    palk=int(input("Напишите зарплату: "))
    palgad.append(palk)
    inimesed.append(nimi)
    return inimesed, palgad

#praktiline töö 10
def Keskmine(palgad,inimesed):
    keskminee=sum(palgad)/len(palgad)
    max_index=palgad.index(keskminee)
    nimi=inimesed[max_index]
    return keskminee, nimi


def keskmine(palgad,inimesed):
    keskminee=sum(palgad)/len(palgad)
    ind=palgad.index(keskminee)
    nimi=inimesed[ind]  
    return keskminee


#Registreerimine ja autoriseerimine
def kasutajaandmed(ll:list,p:list):
    """siin toimub registreerimine
    """
    print("Хотите ли вы свои данные или рандомные")
    a=input("Что вы хотите: ")
    if a=="oma":
        login=input("Напишите ваше имя: ")       
    print("Хотите ли вы свои данные или рандомные")
    a=input("Что вы хотите: ")
    if a=="oma":
        login=input("Напишите ваше имя: ")      
        psword=input("Напишите ваш пароль на максимуме 12 симбволов: ")
        n=len(psword)
        while n<12:
            psword=input("Ваш пароль короткий. Пожалуйста, напишите еще: ")
            n=len(psword)
    elif a=="random":
        login=input("Напишите ваше имя: ")
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0+str1+str2+str3
        #print(str4)
        ls = list(str4)
        #print(ls)
        shuffle(ls)
        #print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([choice(ls) for x in range(12)])
    ll.append(login)
    p.append(psword)
    return login,psword
 
def aut(ll:list,p:list):
    """siin on autoriseerimine 
    """
    print("Напишите ваш логин и пароль")
    logg=input("Логин: ")
    pas_=input("Пароль: ")
    if logg in ll and pas_ in p:
        print("Добро пожаловать!")
    else: 
        print("Неверные данные")
    return logg, pas_

def uss_login(ll:list,vanamini:list,uusnimi:list):
    """Siin saab oma nimi kustutada.
    """
    if vanamini in ll:
        index=ll.index(vanamini)
        ll[index]=uusnimi
        print("Ваше имя изменено.")
    else:
        print("Ошибка!")

def uss_salasõna(ll,p,login,vanasalasõna,uussalasõna):
    """Siin saab oma parooli kustutada.
    """
    if login in ll and vanasalasõna in p:
        index=ll.index(login)
        p[index]=uussalasõna       
        print("пароль изменен")
    else:
        print("Ошибка!")
        
def nimii(ll,p,nimiii):
    """Siin saab vaadata oma vana parooli.
    """
    if nimiii in ll:
        index=ll.index(nimiii)
        print(f"Ваш старый пароль:",p[index])
    else: 
        print("Ошибка!")
