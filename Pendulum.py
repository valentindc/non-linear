import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


x0 = input("write the initial position ")

# Parametros que intervienen en la resolucion del sistema
g = 9.8
m = 1
l = 1

# en la lista nx almacenamos los puntos correspondientes al espacio fase
def Pendulum( x, t, m, g, l):
	nx = np.zeros[2]
	nx[0] = x0
	nx[1] = m*g*l*np.sin(x[0])
	return n

#ts = linspace( 0.0, 50.0, 1001)
#ys = odeint(Pendulum, x0, ts, args = ( m, g, l))

#f = open('pendulum.txt', w+)
#f.write(ys[:,0], ys[:,1])
#f.close

# esta funcion esta para plotear la trayectoria seguida 
def plot_orbit (x0):
	ts = linspace( 0.0, 50.0, 1001)
	ys = odeint(Pendulum, x0, ts, args = ( m, g, l))
	plt.plot(ys[:,0], ys[:,1])
	
	with open('example.txt','r') as csvfile:
    		plots = csv.reader(csvfile, delimiter=',')
    		for row in plots:
        		x.append(int(row[0]))
	       		y.append(int(row[1]))
		plt.plot(x,y, label='Loaded from file!')
		plt.xlabel('theta')
		plt.ylabel('p_theta')
		plt.title('Interesting Graph\nCheck it out')
		plt.legend()
		plt.show()
