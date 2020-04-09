def fibonacci(number):
	if number == 0: return 0
	elif number == 1: return 1
	else: return fibonacci(number-1) + fibonacci(number-2)

def palindromo(sentence):
	sentence = str(sentence).lower().replace(" ", "")
	return sentence == sentence[::-1]

def factorial(number):
	if(number == 0): return 1
	return number * factorial(number-1)

def area_triangulo(base, altura):
	return (base * altura)/2



class Course:
	def __init__(self, name, duration):
		self.name = name
		self.duration = duration


class LearningPath():
	def __init__(self, name):
		self.name = name
		self.courses = []

	def add_course(self, course):
		self.courses.append(course)

	def remove_course(self, course):
		self.courses.remove(course)

	def isEmpty(self):
		return len(self.courses) > 0

class Estudiante:

	def __init__(self, nombre="", numero_cuenta=""):
		self.numero_cuenta = numero_cuenta
		self.nombre = nombre
		self.learning_path = []

	def saluda(self):
		return "Hola soy " + self.nombre

	def get_numero_de_cuenta(self):
		print(self.numero_cuenta)

	def get_nombre(self):
		print(self.nombre)

	def agregar_learning_path(self, learning):
		self.learning_path.append(learning)
