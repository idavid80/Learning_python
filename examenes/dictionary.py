import os
import datetime
import csv

def email_list(domains):
    emails = []
    for domain, users in domains.items():
          for user in users:
              emails.append(user+'@'+domain)
    return(emails)

print("Ejercicio 1", email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], \
"yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

"""Pregunta 2
The groups_per_user function receives a dictionary, which contains group names with
 the list of users. Users can belong to multiple groups. Fill in the blanks to 
 return a dictionary with the users as keys and a list of their groups as values.
"""

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group,users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
        # Now add the group to the the list of
          # groups for this user, creating the entry
          # in the dictionary if necessary
          user_groups[group] = user_groups.get(group,[]) + [user]
    # Now add the group to the the list of
    # groups for this user, creating the entry
    # in the dictionary if necessary

    return (user_groups)
print("groups_per_user", groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


def groups_per_userMal(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user in user_groups:
				user_groups[user].append(group)
			else:
				user_groups[group] = [users]
# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print("groups_per_userMal", groups_per_userMal({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
result = wardrobe.update(new_items)
print("Ejercicio 2", result)

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for items in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += items
	# Limit the return value to 2 decimal places


""" 
The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries are replaced and new entries are added. What is the content of the dictionary “wardrobe“ at the end of the following code?

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

{'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

What’s a major advantage of using dictionaries over lists?

It’s quicker and easier to find a specific element in a dictionary

Correct
Right on! Because of their unordered nature and use of key value pairs, searching a dictionary takes the same amount of time no matter how many elements it contains
"""

"""Pregunta 1
The create_python_script function creates a new python script in the current working directory,
 adds the line of comments to it declared  by the 'comments' variable, and returns the size of
  the new file. Fill in the gaps to create a script called "program.py"."""
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open (filename, "w") as file:
    filesize = file.write(comments)
  return(filesize)

print(create_python_script("program.py"))

"""The new_directory function creates a new directory inside the current working directory, 
then creates a new empty file inside the new directory, and returns the list of files in 
that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".
"""
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(os.getcwd())

print(new_directory("PythonPrograms", "script.py"))

"""The file_date function creates a new file in the current working directory, 
checks the date that the file was modified, and returns just the date portion 
of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a 
file called "newfile.txt" and check the date that it was modified."""

def file_date(filename):
  # Create the file in the current directory
  with open (filename, "w") as file:
    pass

  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  now = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(now.strftime("%Y-%m-%d")))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

"""Pregunta 5
The parent_directory function returns the name of the directory that's located 
just above the current working directory. Remember that '..' is a relative path
 alias that means "go up to the parent directory". Fill in the gaps to complete 
 this function."""


#Reding CSV Files

f = open("csv_files.txt")
csv_f = csv.reader(f)
for row in csv_f:
  name, phone, role = row
  print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

# Generate CSV

def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())

hosts = [["workstattion.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open ("hosts.csv", "w") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)

# En terminal: > cat hosts.csv

# DictReader
with open("software.csv") as software:
  reader = csv.DictReader(software)
  for row in reader:
    print(("{} has {} users").format(row["name"], row["users"]))

# DictWriter The fieldnames parameter of DictWriter() requires a list of keys

users = [{"name": "Pepe", "username": "PP80", "departament": "IT frontend"},
         {"name": "Juan", "username": "Jon", "departament": "IT Backend"}]
keys = ["name", "username", "departament"]

with open("by_departament.csv") as by_departament:
  writer = csv.DictWriter(by_departament, fieldnames=keys)
  writer.writeheader()
  writer.writerows(users)
