"""
Created on Fri Feb 12 2021
@author: María Paula Valdés
Simulación de datos caída libre de objetos con resistencia
Expresiones en: https://www.overleaf.com/read/gzqcgwsrvcsh
"""
import numpy as np
import matplotlib.pyplot as plt
#datos iniciales
v_i=0#m/s
h_i=100#m (distancia de caida)
g=9.81#m/s^2
c=0.5# coeficiente de arrastre
p=1.15
#fuerza de retardo
#W=1/2*c*p*A*v^2
T=np.linspace(0,10,num=1000)

#Valor de S que se relaciona con la fuerza de arrastre
#S^2=2cpA2g/m
def valorS(masa, radio):
    S1 = 2*c*np.pi*p*radio**2*g*(1/masa)
    return((S1)**(1/2))

fig, (ax1,ax2,ax3)= plt.subplots(nrows=1, ncols=3)
#método para calcular la aceleración en función del tiempo de caida.
def tiempoA(N,S,V,I):
    a=g*(1-(S**2)*(V**2)/(4*g**2))
    #Determina cuando debe dejar de gráficar porque ha caido los 100 metros
    #I es el index de cuando eso ocurre
    RealT = np.delete(T,I)
    ax2.plot(RealT,a, label=N)
    ax2.legend()
    ax2.set_title("Tiempo vs aceleración")
    ax2.set_xlabel("Tiempo(s)")
    ax2.set_ylabel("aceleracion(m/s^2)")
    
def lanzamiento(nombre,masa,radio):
    S= valorS(masa,radio)
    v=(2*g/S)*(np.exp(S*T)-1)/(np.exp(S*T)+1)
    y=(2*g/S)*(2/S*np.log((np.exp(S*T)+1)/2)-T)
    ##obtener donde se hace 0 la distancia(ya ha caido los 100m)
    index=np.where(y >h_i)
    #RealX elimina los valores después despues de los 100m de caida
    RealT = np.delete(T,index)
    RealV = np.delete(v, index)
    Realy= np.delete(y, index)
    tiempoA(nombre,S,RealV, index)
    ax1.plot(RealT,-1*(Realy-h_i), label=nombre)
    ax1.legend()
    ax1.set_title("Tiempo vs Altura")
    ax1.set_xlabel("Tiempo(S)")
    ax1.set_ylabel("Distancia (m)")
    ax3.plot(RealT,RealV, label=nombre)
    ax3.legend()
    ax3.set_title("Tiempo vs velocidad")
    ax3.set_xlabel("Tiempo(S)")
    ax3.set_ylabel("velocidad (m/S)")
    
    
#nombre, masa(kg), radio(m)
    """
lanzamiento("baseball",0.145,0.0366)
lanzamiento("ping-pong",0.0024,0.019)
lanzamiento("gota p",1e-5,0.003)
lanzamiento("gota g",0.004,0.002)
"""
lanzamiento("Pelota de poliestireno",0.00862,0.033)
plt.show()
    
    