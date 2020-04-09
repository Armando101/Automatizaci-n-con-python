import unittest
from programas import *

# Para testear utilizamos el siguiente comando
# pytest nombre_archivo.py 
def test_fibonacci():
	assert fibonacci(5) == 6
	assert fibonacci(8) == 21

def test_palindromo():
	assert palindromo("Anita lava la tina")
	assert palindromo("Radar")

def test_factorial():
	assert factorial(5) == 120
	assert factorial(6) == 720

def test_area_triangulo():
	assert area_triangulo(3, 5) == 7.5
	assert area_triangulo(6, 5) == 15


class TestEstudiante(unittest.TestCase):

	def setUp(self):
		"""
		Esta función se llama automáticamente antes de cada prueba
		"""
		
		# Cursos
		self.htmlCSS = Course("Curso practico de HTML y CSS", 2)
		self.preprocesadores = Course("Curso de Preprocesadores CSS", 6)

		self.growth = Course("Curso de Growth Marketing", 2)
		self.movil = Course("Curso de Marketing Móvil", 6)

		# Learning paths
		self.learning_front = LearningPath("FrontEnd")
		self. learning_mkt = LearningPath("Marketing")

		# Agregamos un curso al learnign path
		self.learning_front.add_course(self.htmlCSS)

	def test_nombre_duration(self):
		"""
		Verificamos que los nombre y duración se hayan guardado correctamente
		"""
		self.assertEqual(self.htmlCSS.name, "Curso practico de HTML y CSS")
		self.assertEqual(self.preprocesadores.name, "Curso de Preprocesadores CSS")

		self.assertEqual(self.growth.duration, 2)
		self.assertEqual(self.movil.duration, 6)

	def test_isEmpty(self):

		self.assertTrue(self.learning_front.isEmpty())
		self.assertFalse(self.learning_mkt.isEmpty())

	def test_estudiante(self):
		estudiante = Estudiante("Armando", 313323371)

		estudiante.agregar_learning_path(self.learning_front)

		if (estudiante.learning_path[0].courses[0].duration != 2):
			self.fail(" La duración del curso es 2")


# Documentación
# https://docs.python.org/3/library/unittest.html