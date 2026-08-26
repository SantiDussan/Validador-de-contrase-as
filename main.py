from analyzer import Revisor

contraseña= ' '
 ## REVISAMOS QUE LA CONTRASEÑA NO TENGA ESPACIOS EN BLANCO
while ' ' in contraseña:
    contraseña=input("POR FAVOR INTRODUZCA UNA CONTRASEÑA SIN ESPACIOS ")

analizador= Revisor(contraseña)
analizador.largo()
analizador.mayusculas()
analizador.minusculas()
analizador.numeros()
analizador.caracteres()
print(analizador.calificacion())