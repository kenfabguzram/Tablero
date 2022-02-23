from Tablero import *
            
def main():
        tablero=Tablero(int(input("Indique la cantidad de espacios en el tablero deseados:")),
        int(input("Indique la cantidad de jugadores deseados:")))
        noTermino=True
        turno=0
        while noTermino:
            turno+=1
            print("----------------------------------------------------------------------------------")
            print("Turno #",turno)
            for i in range(len(tablero.fichas)):
                tablero.fichas[i].avanzar()
                if tablero.fichas[i].posicion>=tablero.espacios:
                    noTermino=False
                    print("La ficha ",tablero.fichas[i].color," es la ganadora")
                    print("----------------------------------------------------------------------------------")
                    break
            if not noTermino:
                break

if __name__ == "__main__":
    main()
