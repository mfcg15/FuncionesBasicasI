#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #Imprimira en consola el numero 5

#2
def number_of_military_branches():
    return 5
"""print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) Marcar error por que la primera funcion aun 
no ha sido definida y aunque estuviera definida se necesita colocar los dos argumentos"""


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #Imprimira en consola el numero 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #Imprimira en consola el numero 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) #Imprimira en consola primero el numero 5 y luego el valor None


#6
def add(b,c):
    print(b+c)
#print(add(1,2) + add(2,3))  logra imprimer la suma de los argumentos mandados pero luego marca un error ya que no devuelve ningun valor a sumar


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #Imprimira en consola el numero 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #Imprimira en consola primero 100 luego 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #Imprimira en consola el numero 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #Imprimira en consola el numero 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #Imprimira en consola el numero 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #Imprimira en consola el numero 8


#11
b = 500
print(b) #Imprimira en consola el numero 500
def foobar():
    b = 300
    print(b)
print(b) #Imprimira en consola el numero 500
foobar() #Imprimira en consola el numero 300
print(b) #Imprimira en consola el numero 300


#12
b = 500
print(b) #Imprimira en consola el numero 500
def foobar(): 
    b = 300
    print(b) 
    return b
print(b) #Imprimira en consola el numero 500
foobar() #Imprimira en consola el numero 300
print(b) #Imprimira en consola el numero 500


#13
b = 500
print(b) #Imprimira en consola el numero 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #Imprimira en consola el numero 500
b=foobar() #Imprimira en consola el numero 300
print(b) #Imprimira en consola el numero 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()  #Imprimira en consola primero el numero 1 luego el numero 3 y luego el numero 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y) #Imprimira en consola primero el numero 1 luego el numero 3 y luego el numero 5 y luego el numero 10