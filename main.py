#x = 25


#def printer():
    #x=50
    #return x


#print(x)
#print(printer())


#name = 'Это глобальная строка'


#def greet():
    #name = 'Влад'

    #def hello():
        #print('Привет, '+name)
    #hello()


#greet()


#name = 'Это глобальная строка'


#def greet():
    #name = 'Влад'

    #def hello():
        #print('Привет, '+name)
    #hello()


#greet()

#global
#name = 'Это глобальная строка'


#def greet():
    #enclosing
    #name = 'Влад'

    #def hello():
        #local
        #name = 'Локальная строка'
        #print('Привет, '+name)
    #hello()


#greet()



#x=50


#def func(x):
    #print(f'x равно {x}')

    #x=200
    #print(f'я поменял значение x на {x}')

#func(x)
#print(x)



#x=50


#def func():
    #global x
    #print(f'x равно {x}')

    #x='новое значение'
    #print(f'я поменял значение x на {x}')

#print(x)
#func()
#print(x)


x=50


def func(x):
    print(f'X равно {x}')

    x = 'новое значение'
    print(f'я поменял глобальное значение x на {x}')

    return x


print(x)
x = func(x)
print(x)

