
import array



#Definir un arreglo de números enteros
mi_arreglo = array.array('i', [1, 2, 3, 4, 5])
print(mi_arreglo)
 #Modificar un elemento del arreglo
mi_arreglo[2] = 10

print(mi_arreglo)


mi_arreglo[0] = 1456


print("Arreglo después de la modificación:", mi_arreglo)
print("el valor en la posición 4 es: ", mi_arreglo[4])

