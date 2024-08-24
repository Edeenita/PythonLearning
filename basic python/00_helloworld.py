# Haciendo un hola mundo tipico de la primer lección de la programación
print("hello world!👍") # Imprime por consola
print('Esto tambien es un string, independientemente si usas comillas dobles o simples 👍') # Otro ejemplo de string

# Cómo consultar el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
# La función 'print' devuelve un tipo especial de dato llamado 'NoneType'
# Así que aquí estamos consultando el tipo de dato devuelto por 'print'
print(type(print("Mi cadena de texto")))  # Tipo 'Nontype'