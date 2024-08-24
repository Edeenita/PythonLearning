# Strings #

# Definición de dos strings utilizando comillas dobles y simples
my_string = "Mi String"
my_other_string = 'Mi otro String'

# Uso de la función len() para obtener la longitud de cada string
print(len(my_string))
print(len(my_other_string))

# Concatenación de strings utilizando el operador '+'
print(my_string + " " + my_other_string)

# Uso de un string con salto de línea ('\n')
my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

# Uso de un string con tabulación ('\t')
my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# Uso de un string con caracteres escapados (escape characters)
# Aquí se utiliza '\\' para representar un backslash ('\') literal
my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)


# Formateo de cadenas
name, surname, age = "Ann", "Toxic", 20
# Utilizando el método format()
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# Utilizando el operador % (formateo estilo printf)
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) 
# %s es un marcador de posición utilizado en el método de formateo de cadenas estilo printf.
# Este marcador de posición se utiliza para el primer texto que se pase formateado a la cadena de texto lo va a meter en la posición
# %d es para enteros 

# Concatenando cadenas manualmente y convirtiendo la edad a string
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
# Utilizando f-strings (formato literal de cadenas)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaqueado de caracteres
language = "python"
# Desempaquetando los caracteres de la cadena 'language' en variables individuales
a, b, c, d, e, f = language
# Imprimiendo cada variable individual
print(a) # P
print(b) # Y
print(c) # T
print(d) # H
print(e) # O
print(f) # N

# Obtener una porción de la cadena desde el índice 1 hasta el índice 3 (no inclusivo)
language_slice = language[1:3]
print(language_slice)  # Imprime 'yt'

# Obtener una porción de la cadena desde el índice 1 hasta el final
language_slice = language[1:]
print(language_slice)  # Imprime 'ython'

# Obtener el caracter en la posición -2 (contando desde el final)
language_slice = language[-2]
print(language_slice)  # Imprime 'o'

# Obtener una porción de la cadena desde el índice 0 hasta el índice 6, con un salto de 2
language_slice = language[0:6:2]
print(language_slice)  # Imprime 'pto'

# Reversa de una cadena
reversed_language = language[::-1]  # Obtener una copia inversa de la cadena
print(reversed_language)  # Imprime 'nohtyp'

# Funciones del lenguaje
# Convertir el primer carácter en mayúscula
print(language.capitalize())  # Imprime 'Python'
# Convertir toda la cadena en mayúsculas
print(language.upper())  # Imprime 'PYTHON'
# Contar la cantidad de ocurrencias del carácter 't' en la cadena
print(language.count("t"))  # Imprime 1
# Verificar si la cadena contiene solo caracteres numéricos
print(language.isnumeric())  # Imprime False
# Verificar si la cadena contiene solo caracteres numéricos
print("1".isnumeric())  # Imprime True
# Convertir toda la cadena en minúsculas
print(language.lower())  # Imprime 'python'
# Verificar si toda la cadena está en mayúsculas (isupper)
print(language.lower().isupper())  # Imprime False
# Verificar si la cadena comienza con "Py"
print(language.startswith("Py"))  # Imprime True
# Comparación de cadenas, teniendo en cuenta que "Py" no es igual a "py"
print("Py" == "py")  # Imprime False

