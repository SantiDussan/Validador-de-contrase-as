from analyzer import Revisor
## GETPASS PARA ENMASCARAR LA CONTRASEÑA
from getpass import getpass

contraseña= ' '
 ## REVISAMOS QUE LA CONTRASEÑA NO TENGA ESPACIOS EN BLANCO
while ' ' in contraseña:
    contraseña=getpass("POR FAVOR INTRODUZCA UNA CONTRASEÑA SIN ESPACIOS ")

contraseña="HolaMundo"
analizador= Revisor(contraseña)
print(analizador.largo())
print(analizador.mayusculas())
print(analizador.minusculas())
print(analizador.numeros())
print(analizador.caracteres())
analizador.evaluacion()
print(analizador.calificacion())
print(analizador.consejos())