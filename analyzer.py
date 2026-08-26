# IMPORTAMOS LA LIBRERIA STRING
import string

## INCIALIZAMOS LA CLASE DE REVISOR, DONDE REVISAREMOS CADA 
class Revisor:
    def __init__(self,contraseña):
        self.contraseña=contraseña
        self.contador=0
       

    # REVISAMOS EL LARGO
    def largo(self):
        self.longitud=len(self.contraseña)
        #print(f"LA CONTRASEÑA TIENE {self.longitud} CARACTERES")        
        if self.longitud >=8:
            self.contador+=1

    # REVISAMOS SI TIENE MAYÚSCULAS
    def mayusculas(self):
        # LO ALMACENAMOS PARA EL MOMENTO QUE LO REQUIRAMOS MAS ADELANTE
        mayuscula=sum(1 for letra in self.contraseña if letra.isupper())
        #print(f"LA PALABRA TIENE {mayuscula} MAYÚSCULAS")
        if mayuscula>=1:
            self.contador+=1

    # REVISAMOS SI TIENE MINÚSCULAS
    def minusculas(self):
        # LO ALMACENAMOS PARA EL MOMENTO QUE LO REQUIRAMOS MAS ADELANTE
        minusculas=sum(1 for letra in self.contraseña if letra.islower())
        #print(f"LA PALABRA TIENE {minusculas} LETRAS MINÚSCULAS")
        if minusculas>=1:
            self.contador+=1

    def numeros(self):
        # LO ALMACENAMOS PARA EL MOMENTO QUE REQUIRAMOS MAS ADELANTE
        numero=sum(1 for letra in self.contraseña if letra.isdigit())
        #print (f"LA PALABRA TIENE {numero} NUMEROS")
        if numero>=1:
            self.contador+=1

    # REVISAMOS SI TIENE 
    def caracteres(self):
        # LO ALMACENAMOS PARA EL MOMENTO EN EL CUAL SI TIENE CARACTERES ESPECIALES
        especiales=sum(1 for letra in self.contraseña if letra in string.punctuation)
        #print(f"LA CONTRASEÑA TIENE {especiales} CARACTERES ESPECIALES")
        if especiales>=1:
            self.contador+=1

    # REALIZAMOS LA TABLA DE CALIFICACIÓN
    def calificacion(self):
        if self.contador<=1:
            return f"TIENES UNA CONTRASEÑA MUY DÉBIL CON CALIFICACIÓN DE {self.contador}"

        elif 2 <=self.contador <=3:
            return f"TIENES UNA CONTRASEÑA DEBIL CON CALIFICACIÓN DE {self.contador}"

        elif self.contador==4:
            return f"TIENES UNA CONTRASEÑA BUENA CON CALIFICACIÓN DE {self.contador}"

        elif self.contador==5:
            return f"TIENES UNA CONTRASEÑA FUERTE CON CALIFICACIÓN DE {self.contador}"