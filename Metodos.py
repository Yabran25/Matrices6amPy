
class Metodos:
    
    def Solicitardimensionesdematriz():
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        return filas, columnas

    def llenarmatrizvaloresramdom(filas, columnas):
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = random.randint(1, 100)
                fila.append(valor)
            matriz.append(fila)
        return matriz