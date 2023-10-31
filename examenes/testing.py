"""import os.path

def read_files(filename):
    if not os.path.exists(filename):
        return ""
    if not os.path.isfile(filename):
        return ""
    if not os.access(filename, os.R_OK):
        return ""
    if is_locked(filename):
        return ""
    if is_not_accesible(filename):
        return ""
    """


# !/usr/bin/env python3

def character_frecuency(filename):
    """Counts the frecuency of each character in the given file"""
    try:
        f = open(filename)
    except OSError:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters


def validate_user(username, minlen):
    assert type(username) == str, "username must be string"
    # assert genera comprueba que la condición sea True, si es False genera un error
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    # raise genera un error en python y Value error indica que hay un problema con un parametro
    if len(username) < minlen:
        return False
    if not username.isalnum():
        # isalum evita que entren array y otros tipos no validos
        return False
    return True
