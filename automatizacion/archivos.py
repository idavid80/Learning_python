# Paso 1 crear archivo con lista de clientes.
"""
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()
"""
"""
#Ver nombre por pantalla con o sin splt()
with open("guests.txt") as guests:
    for line in guests:
        print(line)
"""
"""
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "a") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.append(name + "\n")

"""
# comprobar si se han añadido
with open("guests.txt") as guests:
    for line in guests:
        print(line)

"""
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))
"""