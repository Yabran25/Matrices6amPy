import Metodos as mt

matriz1 = mt.MetodosMatrices()
dimensiones1 = matriz1.Solicitardimensionesdematriz()
matriz1 = matriz1.llenarmatrizvaloresrandom()
print(matriz1)
pares1, impares1 = mt.MetodosMatrices.pareseimpares(matriz1)
print(f"Los pares son: {pares1}")
print(f"Los impares son: {impares1}")