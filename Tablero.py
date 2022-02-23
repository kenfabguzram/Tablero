from string import printable
from Ficha import *
from random import *
class Tablero:

    #Defina aquí los atributos de Tablero
    espacios=0
    fichas=[]

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno




    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self,espacios,c_jugadores):
        for n in range(c_jugadores):
            self.fichas.append(Ficha(input("Jugador "+str(n+1)+", ingrese el color de ficha deseado:")))
        shuffle(self.fichas)
        self.espacios=espacios
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase
    

    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
