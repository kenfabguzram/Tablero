from string import printable
from Ficha import *
from random import *
class Tablero:

    #Defina aquí los atributos de Tablero
    espacios=0
    fichas=[]
    numeroTurno=0
    jugando=True
    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno




    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self,espacios):
        self.fichas.append(Ficha("verde"))
        self.fichas.append(Ficha("amarilla"))
        self.fichas.append(Ficha("azul"))
        self.fichas.append(Ficha("roja"))
        shuffle(self.fichas)
        self.espacios=espacios
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase
    

    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
    def turno(self):
        self.numeroTurno+=1
        print("----------------------------------------------------------------------------------")
        print("Turno #",self.numeroTurno)
        for i in range(len(self.fichas)):
            self.fichas[i].avanzar()
            if self.fichas[i].posicion>=self.espacios:
                self.jugando=False
                print("La ficha ",self.fichas[i].color," es la ganadora")
                print("----------------------------------------------------------------------------------")
                break

    def partida(self):
        self.jugando=True
        while self.jugando:
            self.numeroTurno+=1
            print("----------------------------------------------------------------------------------")
            print("Turno #",self.numeroTurno)
            for i in range(len(self.fichas)):
                self.fichas[i].avanzar()
                if self.fichas[i].posicion>=self.espacios:
                    self.jugando=False
                    print("La ficha ",self.fichas[i].color," es la ganadora")
                    print("----------------------------------------------------------------------------------")
                    break
            if not self.jugando:
                break