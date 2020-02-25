# Importo la librería para hacer las pruebas
import unittest

# importamos el script principal
from shoping_cart import Item, ShoppingCart, NotExistsItemError
API_VERSION = 17

# Las pruebas unitarias las debemos hacer dentro de una clase
# Las pruebas serán métodos en lugar de funciones

# Las clases de test deben heredar de unittest.TestCase
class TestShoppingCart(unittest.TestCase):

	# Declaramos los métodos para hacer las prubas
	def test_cinco_mas_cinco_diez(self):
		assert 5 + 5 == 10

	def setUp(self):
		"""
		Se ejecuta antes de cada prueba
		"""
		# print("Método setUp antes de la prueba")
		self.pan = Item("Pan", 7.0)
		self.jugo = Item("Jugo", 5.0)
		self.shoping_cart = ShoppingCart()
		self.shoping_cart.add_item(self.pan)

	def tearDown(self):
		"""
		Se ejecuta después de cada prueba
		"""
		# print("Método setUp después de la prueba")
		pass

	def test_nombre_producto_igual_manzana(self):
		item = Item("Manzana", 12.0)

		# Para hacer el test podemos usar assert o un método de la clase TestCase

		# assertEqual
		# Si los argumentos son iguales la prueba pasa
		self.assertEqual(item.name, "Manzana")

	# Puedo hacer pruebas sin crear la instancia en el método
	# La instancia ya se realizó en el método setUp
	def test_nombre_producto_igual_pan(self):
		# Devuelve True si los valores que recibe como argumento son iguales, esto es ==
		self.assertEqual(self.pan.name, "Pan")

	def test_nombre_producto_igual_pan(self):
		self.assertNotEqual(self.jugo.name, "Manzana")

	def test_nombre_producto_diferente_manzana(self):
		item = Item("Pan blanco", 15.0)
		# assertNotEqual
		# Verifica que los argumentos no sean iguales
		self.assertNotEqual(item.name, "Manzana")

	def test_contiene_productos(self):
		# assertTrue me devuelve true si lo que recibe es true
		self.assertTrue(self.shoping_cart.contains_items())

	def test_no_contiene_productos(self):
		# assertFalse me devuelve true si lo que recibe es false
		self.shoping_cart.remove_item(self.pan)
		self.assertFalse(self.shoping_cart.contains_items())

	def test_obtener_producto_pan(self):
		item = self.shoping_cart.get_item(self.pan)
		# assertIs devuelve true si los dos objetos que recibe como argumento son iguales, esto es is
		self.assertIs(item, self.pan)

		self.assertIsNot(item, self.jugo)

	# La diferencia entre assertIs y assertEqual es que la primera compara objetos y la segunda valores.
	# assertIs 		is 		Compara objetos
	# assertEqual 	== 		Compara valores

	def test_exception_al_obtener_jugo(self):
		"""
		Este método nos permite testear excepciones
		"""
		with self.assertRaises(NotExistsItemError):
		# Colocamos la acción que ocasiona que la excepción sea lanzada
		# Si queremos obtener un objeto que no está, se lanza la excepción
		# Con assertRaises verificamos que se lanzen las excepciones
			self.shoping_cart.get_item(self.jugo)

	def test_total_con_un_producto(self):
		total = self.shoping_cart.total()

		# Con assertGreater indico que total debe ser mayor a 0
		self.assertGreater(total, 0)

		# Con assertLess indico que el primer argumento debe ser menor al segundo
		self.assertLess(total, self.pan.price + 1)

		# Con assertEqual indico que los dos argumentos deben ser iguales
		self.assertEqual(total, self.pan.price)

	def test_codigo_pan(self):
		"""
		Colocamos como primer argumento el string donde se buscará
		El segundo argumento es el string que se va a buscar
		"""
		# Para este caso el primer argumento que recibe es "Pan-123456789"
		# El segundo argumento es Pan
		# Como Pan está dentro de Pan-123456789 retorna True
		self.assertRegex(self.pan.code(), self.pan.name)

	def test_fail(self):
		"""
		Este método nos permite hacer nuestrar propias validaciones
		Si se ejecuta este método lanza un error
		Generalemente se utiliza con una condicional
		"""
		# Este método es útil si los métodos de assert no cumplen con nuestras necesidades y queremos hacer nuestros propios métodos
		if 2 > 3:
			# Entra si queremos que la prueba falle
			self.fail("Dos no es mayor a tres")

	@unittest.skip("Colocamos los motivos de que la prueba se salte")
	def test_prueba_skip(self):
		"""
		Este método es útil cuando queremos saltar una prueba
		Esta prueba no se ejecutará
		Es útil cuando el programador sabe que la prueba no se va a ejecutar
		"""
		# Al ejecutar en consola vemos una "s" esto es de skip
		# Si queremos ver más información agregamos la bandera -v
		pass

	# Si el primer argumento es verdadero la prueba se salta
	# Si es falso se evalua
	# También podemos incluir condicionales
	# El segundo argumento es un string donde colocamos los motivos de salto de la prueba
	@unittest.skipIf(API_VERSION < 18,"La versión es obsoleta")
	def test_prueba_skip_v2(self):
		"""
		Este método es útil cuando el programador desconoce si la prueba puede o no puede ejecutarse
		"""
		pass

	@unittest.skipUnless(False,"Motivos")
	def test_prueba_skip_v3(self):
		"""
		La prueba de este método se salta si el valor booleano es False
		"""
		pass


if __name__ == '__main__':
	# Con esta línea se ejecutan todas las prubeas untiarias
	# Para ejecutarlo desde la consola ejecutamos el comando:
	# python nombre_del_archivo
	unittest.main()