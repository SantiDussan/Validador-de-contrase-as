# IMPORTAMOS LA LIBRERIA STRING
import string

## INCIALIZAMOS LA CLASE DE REVISOR, DONDE REVISAREMOS CADA 
class Revisor:
    def __init__(self,contraseña):
        self.contraseña=contraseña
        self.contador=0 
        self.longitud=0
        self.uppers=0
        self.lowers=0
        self.digits=0
        self.esp=0
       

    # REVISAMOS EL LARGO
    def largo(self):
        self.longitud=len(self.contraseña)

        ## VAMOS DEVOLVER LA CONTRASEÑA CON UN RETURN
        return(f"LA CONTRASEÑA TIENE {self.longitud} CARACTERES") 
        


    # REVISAMOS SI TIENE MAYÚSCULAS
    def mayusculas(self):
        # LO ALMACENAMOS PARA EL MOMENTO QUE LO REQUIRAMOS MAS ADELANTE
        self.uppers=sum(1 for letra in self.contraseña if letra.isupper())

        return(f"LA CONTRASEÑA TIENE {self.uppers} CARACTERES EN MAYÚSCULA")

    # REVISAMOS SI TIENE MINÚSCULAS
    def minusculas(self):
        # LO ALMACENAMOS PARA EL MOMENTO QUE LO REQUIRAMOS MAS ADELANTE
        self.lowers=sum(1 for letra in self.contraseña if letra.islower())

        return(f"LA CONTRASEÑA TIENE {self.lowers} CARACTERES EN MINÚSCULA")
        

    def numeros(self):
        # LO ALMACENAMOS PARA EL MOMENTO QUE REQUIRAMOS MAS ADELANTE
        self.digits=sum(1 for letra in self.contraseña if letra.isdigit())
        return(f"LA CONTRASEÑA TIENE {self.digits} NUMEROS")

    # REVISAMOS SI TIENE 
    def caracteres(self):
        # LO ALMACENAMOS PARA EL MOMENTO EN EL CUAL SI TIENE CARACTERES ESPECIALES
        self.esp=sum(1 for letra in self.contraseña if letra in string.punctuation)
        return(f"LA CONTRASEÑA TIENE {self.esp} CARACTERES ESPECIALES")

    
    ## ----------- EVALUAMOS EL NIVEL DE FUERZA DE LA CONTRASEÑA ---------------
    # EVALUEMOS CADA PARTE LLAMADO EVALUACIÓN
    def evaluacion(self):
        ## EN ESTE CASO ASIGNAMOS EL VALOR A 0 AL CONTADOR PARA QUE SE REINICE POR SI SE HACE VARIAS VECES LA TAREA
        self.contador=0
         ## VAMOS A COMPROBAR QUE TENGA MAYOR UNA CANTIDAD CONSIDERABLE
        if 7 <= self.longitud <= 8:
            self.contador+=1
        elif 9 <=self.longitud <= 10:
            self.contador+=2
        elif self.longitud >=11:
            self.contador+=3

        # HACEMOS EL COMPARATIVO DE LAS MAYÚSCULAS
        if self.uppers == 1:
            self.contador+=1
        elif 2 <= self.uppers <= 3:
            self.contador+=2
        elif self.uppers>=4:
            self.contador+=3

        ## CONTEO DE MINUSCULAS
        if 2 <=self.lowers <= 3:
            self.contador+=1
        elif self.lowers>= 4:
            self.contador+=2

        ## CONTEO DE DIGITOS
        elif 2<=self.digits<=3:
            self.contador+=1
        elif self.digits>=4:
            self.contador+=2

        ## CONTEO DE CARACTERES ESPECIALES
        if self.esp==1:
            self.contador+=1
        elif 2<=self.esp<=4:
            self.contador+=2
        elif self.esp>=5:
            self.contador+=3

        return self.contador

    # PASAMOS POR LA CALIFICACIÓN
    def calificacion(self):
        if self.contador <=3:
            return(f"TU CALIFICACIÓN ES DE {self.contador} PUNTOS, TIENES UNA CONTRASEÑA MUY DEBIL")
        elif 4 <= self.contador <= 7:
            return(f"TU CALIFICACIÓN ES DE {self.contador} PUNTOS, TIENES UNA CONTRASEÑA NORMAL")
        elif self.contador>= 8:
            return(f"TU CALIFICACIÓN ES DE {self.contador} PUNTOS, TIENES UNA CONTRASEÑA MUY FUERTE")

    # PASAMOS POR EL NIVEL DE CONSEJOS QUE TENGA CADA CONTRASEÑA
    def consejos(self):

        ## REVISAMOS LA LONGITUD
        if self.longitud <=5:
            result1="TIENES UNA CONTRASEÑA DEMASIADA CORTA"
        elif 6 <= self.longitud <= 8:
            result1="TIENES UNA CONTRASEÑA NORMAL DE LONGITUD"
        elif self.longitud >= 9:
            result1="TIENES UNA CONTRASEÑA CON EXCELENTE LONGITUD"

        ## REVISAMOS LAS MASYÚSCULAS
        if self.uppers <= 1:
            result2="TIENES UNA CONTRASEÑA CON MUY POCAS MAYÚSCULAS, DEBES AUMENTARLA AL MENOS A 4"
        elif 2 <= self.uppers <= 3:
            result2="TIENES UNA CONTRASEÑA CONTRASEÑA CON UNA CANTIDAD NORMAL DE MAYÚSUCLAS"
        elif self.uppers>=4:
            result2="TIENES UNA CONTRASEÑA CON UNA CANTIDAD CONSIDERABLE DE MAYÚSCULAS, MUY BIEN!!!"

        ## REVISAMOS LAS MINÚSUCLAS
        if self.lowers <=2:
            result3="TIENES MUY POCAS MINÚSUCLAS EN LA CONTRASEÑA, DEBES AUMENTARLAS AL MENOS A 12"
        elif 3 <=self.lowers <= 4:
            result3="TIENES UNA CANTIDAD NORMAL DE MINÚSCULAS"
        elif self.lowers>= 5:
            result3="TIENES UNA MUY BUENA CANTIDAD DE LETRAS MINÚSCULAS"

        ## REVISAMOS LA CANTIDAD DE DIGITOS
        if self.digits<= 2:
            result4="TIENES MUY POCOS NÚMEROS, DEBES AGREGAR MÁS"
        elif 3<=self.digits<=4:
            result4="TIENES UNA CANTIDAD DE NÚMEROS NORMAL"
        elif self.digits>=5:
            result4="TIENES MUY BUENA CANTIDAD DE NÚMEROS, MUY BIEN!!!"


        if self.esp<=1:
            result5="TIENES MUY POCOS CARACTERES ESPECIALES"
        elif 2<=self.esp<=3:
            result5="TIENES UNA CANTIDAD BUENA DE CARACTERES ESPECIALES"
        elif self.esp>=4:
            result5="TIENES EXCELENTE CANTIDAD DE CARACTERES ESPECIALES, MUY BIEN!!!"

        ### DAMOS LOS RESULTADOS
        return(f"LOS RESULTADOS SON: \n"
        f"{result1}\n"
        f"{result2}\n"
        f"{result3}\n"
        f"{result4}\n"
        f"{result5}\n")