"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(13)
6227020800
"""

# En ocasiones necesitamos testear con más de una línea

# Declaramos una clase
class Recursivo:
	def factorial(self, number):
		if(number == 0): return 1
		else: return number * self.factorial(number-1)


if __name__ == '__main__':
	import doctest

	# Con esta línea ejecutamos las pruebas del script
	# Ahora sólo es necesario ejecutar el script "python nombre_script.py"
	# Con la bandera -v obtenemos más información del test
	# python nombre_del_script.py -v
	doctest.testmod()

	# Para ejecutar pruebas de un archivo externo lo hacemos como sigue
	doctest.testfile("./test.txt")