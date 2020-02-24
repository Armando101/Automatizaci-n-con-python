from assert_1 import *

# Las pruebas unitarias se hacen mediante funciones
# Las funciones deben empezar con test, esto para que entienda que es de prueba

# Para testear utilizamos el siguiente comando
# pytest nombre_archivo.py 
def test_fibonacci_cinco():
	# Indicamos después de assert la condición, si es True todo salió bien
	assert fibonacci(5) == 5

def test_palindromo_anita():
	# Esta función me devuelve un booleano
	assert palindromo("Anita lava la tina")

def test_factorial_cinco():
	assert factorial(5) == 120

# Assert sólo es útil para pruebas sencillas