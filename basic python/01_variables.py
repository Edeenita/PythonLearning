# Definición y uso de variables #

my_string_variable = "My String variable" # Asignación de una cadena a una variable
print(my_string_variable)

my_int_variable = 5 # Asignación de un entero a una variable
print(my_int_variable)

# Convertir un entero a cadena y luego imprimirlo
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) # Comprobación del tipo de la variable después de la conversión

my_bool_variable = False # Asignación de un booleano a una variable
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Uso de la función 'len' para determinar la longitud de una cadena
print(len(my_string_variable))

#  Variables en una sola línea, asignando múltiples valores a múltiples variables
# Cuidado con abusar de esta sintaxis, 
# facil de cometer errores, ejemplo que demuestra que puedes mezclar tipos de datos
name, surname, alias, age = "Ann", "Toxic", 'Toxiiic', 20
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs para obtener datos del usuario
# Las variables pueden varirar su valor,
# 'name' y 'age' ya tienen un valor asignado, 
# por lo que las variables pueden cambiar su valor según la entrada del usuario
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print("Tu nombre es:", name)
print("Tu edad es:", age)

# Cambio de tipo de dato de variables
name = 20 # Cambiando el valor de 'name' a un entero
age = "Ann" # Cambiando el valor de 'age' a una cadena
print(name) # Imprimiendo el nuevo valor de 'name'
print(age) # Imprimiendo el nuevo valor de 'age'

# La variable 'address' toma el tipo de dato de la última asignación realizada
# En este caso, la última asignación es un float, por lo que 'address' se convierte en un float
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))  # Imprime el tipo de dato de 'address'

