# Operadores Aritméticos #

# Operaciones con enteros
print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División con decimales (3/4 en Python 3 devuelve un float, si necesitas solo la parte entera, usa '//')
print(10 % 3) # Modulo (Resto de la división)
print(10 // 3) # División entera (solo nos da el numero entero)
print(2 ** 3) # Potencia
print(2 ** 3 + 3 - 7 / 1 // 4) # Expresión aritmética combinada

# Operaciones con cadenas de texto #
print("Hola " + "Python " + "Cuanto te mide?") # Concatenación de cadenas de texto
print("Hola " + str(5)) # Conversión de int a str antes de la concatenación

# Operaciones mixtas
print("String " * 5) # Repetición de cadena (repite el string 5 veces)
print("Hola " * (2 ** 3)) # Repetición de cadena con potencia

my_float = 2.5 * 2 # 2.5 es float por lo que al multiplicarlo por 2 da 5.0 que sigue siendo float.
print("Hola " * int(my_float)) # Transforma el float a int antes de la concatenación

# Operadores Comparativos #

# Operaciones con enteros
print(3 > 4) # Mayor
print(3 < 4) # Menor
print(3 >= 4) # Mayor o igual
print(4 <= 4) # Menor o igual
print(3 == 4) # Igual
print(3 != 4) # Diferente

# Operaciones con cadenas de texto
print("Hola" > "Python") # Comparación lexicográfica de cadenas (ordena alfabéticamente)
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Compara la Ordenación alfabética de las variables (Comparación lexicográfica)
print ("AAAA" >= "aaaa") # Toma en cuenta mayusculas [ASCII])
print(len("aaaa") >= len("abaa"))  #  Comparación de longitud de cadenas
print("Hola" <= "Python")  # Comparación lexicográfica, "Hola" es menor que "Python", por lo tanto, devuelve False
print("Hola" == "Hola")    # Compara si ambas cadenas son iguales, devuelve True
print("Hola" != "Python")  # Compara si ambas cadenas son diferentes, devuelve True

# Operadores Lógicos #
print(3 > 4 and "Hola" > "Python") # False (Ambas condiciones deben ser verdaderas)
print(3 > 4 or "Hola" > "Python") # True (Al menos una condición debe ser verdadera)
print(3 < 4 and "Hola" < "Python") # True
print(3 < 4 or "Hola" > "Python") # True
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True (Evalúa primero el paréntesis interno)
print(not (3 > 4)) # True (Negación de una expresión falsa)