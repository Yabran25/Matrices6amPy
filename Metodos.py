import random
class MetodosMatrices:
    
    def Solicitardimensionesdematriz(self):
        dimensiones = int(input("Ingrese las dimensiones de la matriz: "))
        self.dimensiones = dimensiones
        return self.dimensiones

    def llenarmatrizvaloresrandom(self):
        m = []
        for i in range(self.dimensiones):
            fila = []
            for j in range(self.dimensiones):
                valor = random.randint(1, 100)
                fila.append(valor)
            m.append(fila)
        return m

    
    def pareseimpares(m):
        pares = []
        impares = []
        for i in len(m):
            for j in len(m[i]):
                print(f"- {m[i][j]} -")
                if m[i][j] % 2 == 0:
                    pares.append(m[i][j])
                else:
                    impares.append(m[i][j])
        return pares, impares