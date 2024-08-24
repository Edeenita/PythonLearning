### Lists ###

# Definición de listas
my_list = list()  # Crea una lista vacía usando el constructor list()
my_other_list = []  # Crea una lista vacía usando la notación de corchetes []

print(len(my_list))  # Imprime la longitud de my_list (0 porque está vacía)

my_list = [35, 24, 62, 52, 30, 30, 17]  # Asigna una lista de enteros a my_list

print(my_list)  # Imprime el contenido de my_list
print(len(my_list))  # Imprime la longitud de my_list (7 elementos)

my_other_list = [35, 1.77, "Brais", "Moure"]  # Asigna una lista con diferentes tipos de datos a my_other_list

print(type(my_list))  # Imprime el tipo de my_list (list)
print(type(my_other_list))  # Imprime el tipo de my_other_list (list)

# Acceso a elementos y búsqueda
print(my_other_list[0])  # Imprime el primer elemento de my_other_list (35)
print(my_other_list[1])  # Imprime el segundo elemento de my_other_list (1.77)
print(my_other_list[-1])  # Imprime el último elemento de my_other_list ("Moure")
print(my_other_list[-4])  # Imprime el cuarto elemento desde el final de my_other_list (35)

print(my_list.count(30))  # Imprime el número de veces que 30 aparece en my_list (2)

# Comentarios sobre errores si se intenta acceder a índices fuera del rango
# print(my_other_list[4])  # Esto causaría un IndexError porque el índice 4 no existe en my_other_list
# print(my_other_list[-5])  # Esto causaría un IndexError porque el índice -5 no existe en my_other_list

print(my_other_list.index("Brais"))  # Imprime el índice del primer elemento "Brais" en my_other_list (2)

# Asignación múltiple
age, height, name, surname = my_other_list  # Desempaqueta los valores de my_other_list en variables
print(name)  # Imprime el valor de name, que es "Brais"

# Reordenamiento de las variables
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)  # Imprime el valor de age, que es 35

# Concatenación de listas
print(my_list + my_other_list)  # Imprime la concatenación de my_list y my_other_list

# La operación de resta no está permitida entre listas, por eso está comentado
# print(my_list - my_other_list)  # Esto causaría un TypeError

# Creación, inserción, actualización y eliminación de elementos
my_other_list.append("MoureDev")  # Agrega "MoureDev" al final de my_other_list
print(my_other_list)  # Imprime la lista después de la inserción

my_other_list.insert(1, "Rojo")  # Inserta "Rojo" en la posición 1 de my_other_list
print(my_other_list)  # Imprime la lista después de la inserción

my_other_list[1] = "Azul"  # Actualiza el valor en la posición 1 de my_other_list a "Azul"
print(my_other_list)  # Imprime la lista después de la actualización

my_other_list.remove("Azul")  # Elimina el primer elemento "Azul" de my_other_list
print(my_other_list)  # Imprime la lista después de la eliminación

my_list.remove(30)  # Elimina la primera ocurrencia de 30 en my_list
print(my_list)  # Imprime la lista después de la eliminación

print(my_list.pop())  # Elimina y devuelve el último elemento de my_list
print(my_list)  # Imprime la lista después de la eliminación

my_pop_element = my_list.pop(2)  # Elimina y devuelve el elemento en la posición 2 de my_list
print(my_pop_element)  # Imprime el elemento eliminado
print(my_list)  # Imprime la lista después de la eliminación

del my_list[2]  # Elimina el elemento en la posición 2 de my_list
print(my_list)  # Imprime la lista después de la eliminación

# Operaciones con listas
my_new_list = my_list.copy()  # Crea una copia de my_list y la asigna a my_new_list

my_list.clear()  # Limpia todos los elementos de my_list
print(my_list)  # Imprime my_list (vacía)
print(my_new_list)  # Imprime my_new_list (copia de la lista original)

my_new_list.reverse()  # Invierte el orden de los elementos en my_new_list
print(my_new_list)  # Imprime my_new_list después de invertir

my_new_list.sort()  # Ordena los elementos de my_new_list en orden ascendente
print(my_new_list)  # Imprime my_new_list después de ordenar

# Sublistas
print(my_new_list[1:3])  # Imprime una sublista de my_new_list desde el índice 1 hasta el 3 (exclusivo)

# Cambio de tipo
my_list = "Hola Python"  # Asigna un string a my_list
print(my_list)  # Imprime el valor de my_list ("Hola Python")
print(type(my_list))  # Imprime el tipo de my_list (str)
