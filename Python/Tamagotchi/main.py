from persona import Persona
from tamagotchi import Tamagotchi


mi_tamagotchi = Tamagotchi("Pokachu", "Amarillo")

persona1 = Persona("A", "B", mi_tamagotchi)

persona1.darle_comida()
persona1.curarlo()
persona1.jugar_con_tamagotchi()

print("\nEstado final del Tamagotchi")
print("---------------------------")
print("Nombre:", mi_tamagotchi.nombre)
print("Color:", mi_tamagotchi.color)
print("Salud:", mi_tamagotchi.salud)
print("Felicidad:", mi_tamagotchi.felicidad)
print("Energia:", mi_tamagotchi.energia)