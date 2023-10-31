def first_character(string):
    # Complete the return statement using a string operation.
    return string[0]


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K

def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word,word.upper())


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"


def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def even_numbers(first, last):
  return [ n for n in range(first, last, +1) if n%2==0]


print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]


def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for animal in animal_dict.keys():
        # Use a string method to format the required string.
        result += animal + "\n"
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary
    for keys in guest_list: # Iterate over the elements in the list
        result[keys] = 0 # Add each list element to the dictionary as a key with
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))

def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter .isalpha() and letter not in result:
        result[letter] = text.lower().count(letter)
    # Add or increment the value in the dictionary
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


def count_letters_copy(text):
  # Initialize a new dictionary.
  dictionary = {}
  text = text.lower()
  # Complete the for loop to iterate through each "text" character and
  # use a string method to ensure all letters are lowercase.
  for letter in text:
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if letter.isalpha():
      # Complete the if-statement using a logical operator to check if
      # the letter is not already in the dictionary.
      if letter not in dictionary:
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[letter] = text.count(letter)
      # Use a dictionary operation to increment the letter count value
      # for the existing key.
      #___
      #___ # Increment the letter counter.
  return dictionary

print(count_letters_copy("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters_copy("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters_copy("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


genre = "transcendental"
print(genre[:-8])
print(genre[-7:9])

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

print(colors)

teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
teacher_names.values()

print(teacher_names)