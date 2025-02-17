import Metodos as mt

m = mt.Metodosmatrices()
m.crearmatriz()
m.imprimir()
print("La suma de la matriz es: ", m.sumamatriz())
print("La suma de la matriz sin numpy es: ", m.sumamatrizsinnp())
print("El numero mayor de la matriz es: ", m.numeromayor())
print("La suma de las filas es: ", m.conteofilas())
print("La suma de las columnas es: ", m.conteocolumnas())
print("El numero mayor de las columnas es: ", m.resultadomayorcolummas(m.conteocolumnas()))
print("La matriz almacenada en vector es ", m.matrizenvector())