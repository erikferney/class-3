from puntos import *
from math import pi

class Figura:
	def __init__(self, p1, p2):
		self.origen = p1
		self.fin = p2
		self.area = 0
		self.perimetro = 0

class Cuadrado(Figura):
	def calcular_area(self):
		lado = self.origen.calcular_distancia(self.fin)
		self.area = lado * lado
		#return area
	
	def calcular_perimetro(self):
		lado = self.origen.calcular_distancia(self.fin)
		self.perimetro = 2*(lado + lado)

class Circulo(Figura):
	def calcular_area(self):
		radio = self.origen.calcular_distancia(self.fin)
		self.area = pi * (radio**2)
	
	def calcular_perimetro(self):
		radio = self.origen.calcular_distancia(self.fin)
		self.perimetro = 2 * pi * radio
		#return area

class TrianguloCuadrado(Figura):
	def calcular_area(self):
		p3 = Punto(self.origen.x, self.fin.y)
		ladoA = self.origen.calcular_distancia(p3)
		ladoB = p3.calcular_distancia(self.fin)
		self.area = (ladoA * ladoB) / 2
		