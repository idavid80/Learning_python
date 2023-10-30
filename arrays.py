# 1. mostrar por pantalla  una lista con los pares del 1 al 20.
print("1.1", [x*2 for x in range(1, 11)])
# Crear una lista con los pares del 1 al 20.
my_list1 = []
for x in range(1,11):
   my_list1.append(x*2)
print("1.2", my_list1)
# mostrar por pantalla una lista con los pares del 1 al 100.
print("2.1", [ x for x in range(1, 101) if x % 10 == 0 ])
# Crear una lista con los pares del 1 al 100.
my_list2 = []
for x in range(1, 101):
  if x % 10 == 0:
    my_list2.append(x)
print("2.2", my_list2)

# 3. Actualizar fechas, cambiar 2023 por 2024
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = []

for year in years:

   if year.endswith("2023"):
      new = year.replace("2023", "2024")
      updated_years.append(new)
   else:
      updated_years.append(year)

print("3.1", updated_years)

# 3.2 Actualizar fechas, cambiar 2023 por 2024
actualizar_fecha= [year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years]

print("3.2", actualizar_fecha)
# 4. Utiliza una comprensión de lista para crear una lista de números al cuadrado (n*n).
# La función recibe las variables inicio y fin, y devuelve una lista de cuadrados de números consecutivos entre inicio y fin inclusive
def squares(start, end):
   return [n * n for n in range(start, end + 1)]

print("4", squares(2, 3))  # Should print [4, 9]
print("4", squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print("4", squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Crear una función que
def change_string(given_string):

    new_string = ""
    new_list = given_string.split()

    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "
    return new_string


print(change_string("1one 2two 3three 4four 5five"))

def list_elements(list_name, elements):
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))


def pig_latin(text):
    say = []
    # Separate the text into words
    words = text.split(" ")
    for word in words:
        # Create the pig latin word and add it to the list
        say.append(word[1:] + word[0] + 'ay')
        # Turn the list back into a phrase
    return " ".join(x for x in say)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [word.replace("hpp","h") if word.endswith("hpp") else word for word in filenames ]
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def group_list(group, users):
  members = ", ".join(users)
  return " {}: {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""