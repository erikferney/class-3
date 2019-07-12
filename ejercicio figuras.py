from classFigura import *

p1 = Punto(5, 5)
p2 = Punto(5, 10)
p3 = Punto(1, 10)
cuadrado = Cuadrado(p1, p2)
circulo = Circulo(p1, p2)
trianguloC = TrianguloCuadrado(p1, p3)

cuadrado.calcular_area()
cuadrado.calcular_perimetro()
circulo.calcular_area()
circulo.calcular_perimetro()
trianguloC.calcular_area()

print "Cuadrado area: " + str(cuadrado.area)
print "Cuadrado perimetro: " + str(cuadrado.perimetro)
print "Circulo area: " + str(circulo.area)
print "Circulo perimetro: " + str(circulo.perimetro)
print "Triangulo area: " + str(trianguloC.area)