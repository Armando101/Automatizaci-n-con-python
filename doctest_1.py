# Doctest es la abreviatura de Document testing
# Esta herramienta nos permitirá testear el código de manera muy sencilla
# Con esta herramienta no tenemos que instalar nada

# Creamos un archivo .txt
# En la terminal ejecutamos el comando "python -m docset nombre_archivo.txt"
# Si no ocurre nada quiere decir que todo salió bien

# También podemos importar módulos

def fibonacci(number):
	if number == 0: return 0
	elif number == 1: return 1
	else: return fibonacci(number-1) + fibonacci(number-2)

# También podemos ocupar doctest con docstrings
def palindromo(sentence):
	"""
	Retorna verdadero si el parámetro es un palíndromo
	en caso contrario retorna falso

	sentence -- String o entero
	
	>>> palindromo("anita lava la tina")
	True

	>>> palindromo(12321)
	True

	>>> palindromo("Armadno")
	False
	"""

	sentence = str(sentence).lower().replace(" ", "")
	return sentence == sentence[::-1]