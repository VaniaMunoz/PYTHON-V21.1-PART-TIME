num1 = 42 #Declaracion de variables
num2 = 2.3 #Declaracion de variables
boolean = True #Booleano
string = 'Hello World' #cadena, declaracion de variable

#list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

fruit = ('blueberry', 'strawberry', 'banana') #tupla

print(type(fruit)) #print to console

print(pizza_toppings[1]) #list y añadir valor

pizza_toppings.append('Mushrooms') #list y añadir valor

print(person['name']) #print, dictionary

person['name'] = 'George'#dictionary valor de cambio

person['eye_color'] = 'blue' #dictionary valor de cambio


print(fruit[2]) #tuplas, print

#Conditional if, evaluation, print to console, Conditional else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#Conditional if - elif - else, print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


for x in range(5): #For Loop start at 0 and goes up to until 5
    print(x)

for x in range(2,5):#For Loop start at 2 and goes up to until 5
    print(x)

for x in range(2,10,3):#For loop start at 2 goes up to until 10, increments by 3
    print(x)

x = 0  #While Loop, variblae declaration
while(x < 5):

    print(x) #printing to console
    x += 1 # incrementing x


pizza_toppings.pop() #list eliminar valor del indice
pizza_toppings.pop(1) #list  el valor de eliminación en el índice 

print(person) #print

person.pop('eye_color') #dictionary eliminar valor

print(person) #print

for topping in pizza_toppings: #for loop through a list
    if topping == 'Pepperoni':  #Conditional if
        continue
    print('After 1st if statement') #print to console
    if topping == 'Olives': #Conditional if
        break

def print_hello_ten_times(): #declaracion funcion de parametros
    for num in range(10): #For loop up until a given number x
        print('Hello') #print

print_hello_ten_times() #function call

def print_hello_x_times(x): #function Declaration with parameter x
    for num in range(x): #For loop up until a given number x
        print('Hello') #print

print_hello_x_times(4)#function call arguement of 4

def print_hello_x_or_ten_times(x = 10):#function declaration with default parameter
    for num in range(x): #For loop until x
        print('Hello') #print

print_hello_x_or_ten_times() #Function call goes to 10
print_hello_x_or_ten_times(4) #function call goes to 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)