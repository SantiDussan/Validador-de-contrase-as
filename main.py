# PROYECTO 1 ANÁLIZADOR DE CONTRASEÑAS

# EL USUARIO INTRODUCE UNA CONTRASEÑA Y EL PROGRAMA ANALIZA SUS CARACTERISTICAS

# FASE 1 LO BÁSICO
# PRIMERO ES CONSEGUIR QUE EL PROGRAMAMA:
# 1. PIDA CONTRASEÑA
# 2. CUENTE CUÁNTOS CARACTERES TIENE.
# 3. INDIQUE SI TIENE MAYÚSCULAS.
# 4. INDIQUE SI TIENE MINÚSCULAS.
# 5. INDIQUE SI TIENE NÚMEROS.
# 6. INDIQUE SI TIENE CARACTERES ESPECIALES.

import string

# PRIMERO INGRESAMOS LA CONTRASEÑA
contraseña=input("POR FAVOR INGRESE LA CONTRASEÑA: ")

# REALIZAMOS UNA COMPROBACIÓN PARA QUE INGRESE UNA CONTRASEÑA SIN ESPACIOS
while ' ' in contraseña:
    contraseña=input("POR FAVOR INGRESE LA CONTRASEÑA SIN ESPACIO: ")

## CONTAMOS CUANTOS CARACTERES TIENE PARA ESO PASAMOS CARACTERS
caracteres=len(contraseña)
#print(f"LA CONTRASEÑA TIENE {caracteres} CARACTERES")

## REVISAMOS SI TIENE CARACTERES EN MAYUSCULAS
mayusculas= sum(1 for c in contraseña if c.isupper())
#print(f"LAS MAYUSCULAS QUE TIENE SON: {mayusculas}")

## REVISAMOS SI TIENE CARACTERES EN MINUSCULAS
minusculas= sum(1 for c in contraseña if c.islower())
#print(f"LAS MINUSCULAS QUE TIENE SON: {minusculas}")

## REVISAMOS SI TIENE NÚMEROS
numeros= sum(1 for c in contraseña if c.isdigit())
#print(f"LAS NUMEROS QUE TIENE SON: {numeros}")

## REVISAMOS SI TIENE SIMBOLOS
signos= sum(1 for c in contraseña if c in string.punctuation)
#print(f"LOS SIGNOS QUE TIENE SON: {signos}")

## FASE 2 PUNTAJE
# DESPUÉS CREAR UN SISTEMA SENCILLO:
# 8 CARACTERES O MÁS +1
# MAYÚCULAS +1
# MINÚSCULAS +1
# NÚMEROS +1
# ESPECIALES +1

# DANDO UNA TABLA DE CALIFICACIÓN
#0-1 MUY DÉBIL
#2-3 DÉBIL
#4 BUENA
#5 FUERTE

#INICIALIZAMOS UN CONTADOR
contador=0

if caracteres>=8:
    contador+=1

if mayusculas>=1:
    contador+=1

if minusculas>=1:
    contador+=1

if numeros>=1:
    contador+=1

if signos>=1:
    contador+=1


# REALIZAMOS PARTE DE CALIFICACIÓN
if  contador <=1:
    print("TIENES UNA CONTRASEÑA MUY DEBIL")

if 2 <= contador <=3 :
    print("TIENES UNA CONTRASEÑA DEBIL")

if contador == 4:
    print("TIENES UNA CONTRASEÑA BUENA")

if contador == 5:
    print("TIENES UNA CONTRASEÑA FUERTE")