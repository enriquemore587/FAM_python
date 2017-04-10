import math

def form_gral(a, b, c):
	b_2 = b**2
	_4ac = 4 * a * c
	pre = b_2 - _4ac
	raiz =  math.sqrt(pre)
	_b = b * -1
	_2ac = 2 * a * c

	up1 = _b + raiz
	up2 = _b - raiz

	x1 = up1 / _2ac
	x2 = up2 / _2ac

	print 'x1 =  %f \nx2 = %f' % (x1, x2)

def mi_funcion(x):
	xx = x * x
	return xx

def parent(a,b,c):
	resultado = (a * ( b/c ) * 15) + 100
	return resultado

def tabla_de_mutiplicar(numero, mult):
	return '%d * %d = %d' % (numero, mult, float(numero) * mult)

def imprime_float(a):
	print a
