import matplotlib.pyplot as plt

def data_map(data, fn_map):
	aux = []
	for dic in data:
		x = fn_map(dic)
		if x != None:
			aux.append(x)
	return aux

def f(x):
    return x + w

n = 3

w = 0.8 / n

x1 = [1, 2, 3, 4, 5]
x2 = data_map(x1, f)
x3 = data_map(x2, f)

y1 = [10, 20, 30, 40, 50]
y2 = [50, 40, 30, 20, 10]
y3 = [10, 20, 40, 30, 50]

plt.bar(x1, [6,6,6,6,6], w) #
#plt.bar(x2, y2, w) #
#plt.bar(x3, y3, w) #


plt.show()