print('Подсчет стоимости билета в кино')
film=input("на какой фильм хотите?\n")
data=input('Когда пойдем?\n (Подсказка: бронирование билетов за день дает вам скидку 5%\n)')
time=input('Выберете время\n')
count=input('Cколько билетов?\n (Подсказка: если кол-во билетов больше 20, то для вас действует скидка 20%\n) ')	
if film:
   f=='Пятница':
    if data=='Завтра':
        if time==12:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(250*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(250*count*0.95,' рублей')
        elif time==16:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(350*count*0.95,' рублей')
        elif time==20:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(450*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(450*count*0.95,' рублей')
    elif data=="Сегодня":
        if time==12:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(250*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' получается \n')
                 print(250*count*0.95,' рублей')
        elif time==16:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' получается \n')
                 print(350*count*0.95,' рублей')
        elif time==20:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(450*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,'  получается \n')
                 print(450*count*0.95,' рублей')
elif film=="Чемпион":
    if data=='Завтра':
        if time==10:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(250*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(250*count*0.95,' рублей')
        elif time==13:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(350*count*0.95,' рублей')
        elif time==16:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(350*count*0.95,' рублей')
    elif data=="Сегодня":
        if time==10:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(250*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' получается \n')
                 print(250*count*0.95,' рублей')
        elif time==13:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' получается \n')
                 print(350*count*0.95,' рублей')
        elif time==16:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,'  получается \n')
                 print(350*count*0.95,' рублей')
elif film=="Пернатая банда":
    if data=='Завтра':
        if time==10:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(350*count*0.95,' рублей')
        elif time==14:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(450*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(450*count*0.95,' рублей')
        elif time==18:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% и 20% получается \n')
                print(450*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 5% получается \n')
                 print(450*count*0.95,' рублей')
    elif data=="Сегодня":
        if time==10:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(350*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' получается \n')
                 print(350*count*0.95,' рублей')
        elif time==14:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(450*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,' получается \n')
                 print(450*count*0.95,' рублей')
        elif time==18:
            if count>=20:
                print("Стоимость на фильм ",film,'',data,'в ',time,' c четом скидки 20% получается \n')
                print(450*count*0.95*0.80,' рублей')
            else:
                 print("Стоимость на фильм ",film,'',data,'в ',time,'  получается \n')
                 print(450*count*0.95,' рублей')
    
        
        

    
