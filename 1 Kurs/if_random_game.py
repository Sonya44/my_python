import random
a=random.randint(1,4)
b=int(input('Угадайте число\n'))
if a==b:
    print('Молодец')
elif a<b:
    print('попробуй еще раз. попробуй взять число меньше')
elif a>b:
    print('Попробуй взять число больше')
