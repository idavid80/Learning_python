class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamplet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

class Cerdito:
    edad = 0
    def edadCerdito(self):
        return self.edad * 18

Peppa_Pig = Cerdito()
print(Peppa_Pig.edadCerdito())
Peppa_Pig.edad = 8
print(Peppa_Pig.edadCerdito())