import numpy as np

class Metodosmatrices:

    def crearmatriz(self):
        dimension = int(input("Ingrese la dimension de la matriz: "))
        self.dimension = dimension
        matriz = np.random.randint(1, 100, size=(self.dimension, self.dimension))
        self.matriz = matriz
        return self.matriz
    
    def imprimir(self):
        print(self.matriz)

    def sumamatriz(self):
        suma = np.sum(self.matriz)
        return suma
    
    def sumamatrizsinnp(self):
        suma = 0

        for i in range(self.dimension):
            for j in range(self.dimension):
                suma += self.matriz[i][j]
        return suma

    def numeromayor(self):
        nmayor = 0

        for i in range(self.dimension):
            for j in range(self.dimension):
                if nmayor < self.matriz[i][j]:
                    nmayor = self.matriz[i][j]
        return nmayor
    
    def conteofilas(self):
        sumafilas = []
        sumacolumnas = []

        for i in range(self.dimension):
            sumaf = 0
            for j in range(self.dimension):
                sumaf += self.matriz[i][j]
            sumafilas.append(sumaf)
        return sumafilas
    
    def conteocolumnas(self):
        sumafilas = []
        sumacolumnas = []

        for i in range(self.dimension):
            sumac = 0
            for j in range(self.dimension):
                sumac += self.matriz[j][i]
            sumacolumnas.append(sumac)
        return sumacolumnas
    
    def resultadomayorcolummas(self,sumacolumnas):
        nmayor = 0

        for i in range(self.dimension):
                if nmayor < sumacolumnas[i]:
                    nmayor = sumacolumnas[i]
        return nmayor
    
    def matrizenvector(self):
        Mvector = []

        for i in range(self.dimension):
            for j in range(self.dimension):
                Mvector.append(self.matriz[i][j])
        return Mvector