class Apple:
    def __init__(self, color, flavor):
        #Es un constructor, hay que darle a self.color = color
        self.color = color
        self.flavor = flavor

    # en lugar de print(jonagold) que nos daría la ubicación en memoria del objeto
    # Usamos la funcion __str__ siguiente
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold.color)
print("Jonagold object", jonagold)

# Obtener información sobre las clases
help(Apple)

#Obtener comentarios de funciones
def to_seconds(hour, minutes, seconds):
    """Return the amaunt of seconds in the given hours, minutes and seconds."""
    return hour*3600+minutes+60+seconds
help(to_seconds)