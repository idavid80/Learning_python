#Ejercicio 1 Busqueda Binaria
print("Ejercicio 1: ")
"""The find_item function uses binary search to recursively locate an item in the list, returning True if found, False otherwise.
Something is missing from this function. Can you spot what it is and fix it? Add debug lines where appropriate, to help narrow down the problem."""
def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  # El ejercicio es tan sencillo como ordenar la lista antes de empezar
  # Por eso hay qye añadir la línea 7
  list.sort()
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list?
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False

#Ejercicio 2 Busqueda Binaria
print("Ejercicio 2")
"""The binary_search function returns the position of key in the list if found, or -1 if not found. We want to make sure that it's working correctly,
so we need to place debugging lines to let us know each time that the list is cut in half, whether we're on the left or the right.
Nothing needs to be printed when the key has been located.   
For example, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) first determines that the key, 3, is in the left half of the list, and prints
"Checking the left side", then determines that it's in the right half of the new list and prints
"Checking the right side", before returning the value of 2, which is the position of the key in the list.  
Add commands to the code, to print out "Checking the left side" or "Checking the right side", in the appropriate places.  """
def binary_search(list, key):
    #Returns the position of key in the list if found, -1 otherwise.

    #List must be sorted:
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2
        if list[middle] == key:
            return middle
        if list[middle] > key:
            # Añadir siguiente print
            print("Checking the left side")
            right = middle - 1
        if list[middle] < key:
            # Añadir siguiente print
            print("Checking the right side")
            left = middle + 1
    return -1

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
"""Should print 2 debug lines and the return value:
Checking the left side
Checking the left side
0
"""

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
"""Should print no debug lines, as it's located immediately:
4
"""

print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the left side
Checking the right side
6
"""

print("Ejercicio 3")

"""The best_search function compares linear_search and binary_search
functions, to locate a key in the list, and returns how many steps each method took,
and which one is the best for that situation.
The list does not need to be sorted, as the binary_search function sorts it before proceeding (and uses one step to do so).
Here, linear_search and binary_search functions both return the number of steps that it took to either locate the key, or determine that it's not in the list.
If the number of steps is the same for both methods (including the extra step for sorting in binary_search), then the result is a tie.
Fill in the blanks to make this work. """
def linear_search(list, key):
    # Returns the number of steps to determine if key is in the list

    # Initialize the counter of steps
    steps = 0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    # return ___
    return steps


def binary_search(list, key):
    # Returns the number of steps to determine if key is in the list

    # List must be sorted:
    list.sort()

    # The Sort was 1 step, so initialize the counter of steps to 1
    steps = 1

    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2

        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    # return ___
    return steps

def best_search(list, key):
    # steps_linear = ___
    steps_linear = linear_search(list, key)
    # steps_binary = ___
    steps_binary = binary_search(list, key)

    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    # if (___):
    if (steps_linear < steps_binary):
        results += "Best Search is Linear."
    # elif (___):
    elif (steps_linear > steps_binary):
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results


print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
# Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
# Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
# Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
# Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
# Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.