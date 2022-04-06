"""
Ejercicio Nro3 - Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos:

* Nombre: Aragorn          | * Nombre: Gandalf   | * Nombre: Legolas
* Clase: Guerrero          | * Clase: Mago       | * Clase: Arquero
* Raza: Dúnadan del Norte  | * Raza : Istar      | * Raza: Elfo Sindar

"""

personajes = []

personaje1 = {"Nombre":"Aragorn", "Clase":"Guerrero", "Raza":"Dúnadan del Norte"}
personaje2 = {"Nombre":"Gandalf", "Clase":"Mago", "Raza":"Istar"}
personaje3 = {"Nombre":"Legolas", "Clase":"Arquero", "Raza":"Elfo Sindar"}

personajes.append(personaje1)
personajes.append(personaje2)
personajes.append(personaje3)

print(personajes)
print(personajes[0])
print(personajes[1])
print(personajes[2])
