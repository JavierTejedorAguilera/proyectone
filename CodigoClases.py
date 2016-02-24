# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:34:48 2016

@author: JavierTejedorAguilera
"""

import os
import operaciones as op
op.suma(1,2)

def devuelve_doble():
    while True:
        try:
            x=int(input("Introduce un numero:"))
            return 2*x
        except:
            print("Error. El valor introducido no es un número")

devuelve_doble()

def divide():
    while True:
        try:
            x=int(input("Dividendo:"))
            y=int(input("Divisor:"))
            return x/y
        except ValueError:
            print("Valor no admitido, debe ser un número")
        except ZeroDivisionError:
            print("División por 0")
        except: #Error por defecto (va al final)
            print("Error desconocido")          
divide()

os.getcwd()
op.suma(3,4)

#Definimos y llamamos la función lambda
(lambda x,y: x*y+1)(5,6)

#Definimos la funcion lambda
f=(lambda x,y: x*y+1)
#Llamamos a la función lambda
f(3,4)

def aplica(funcion, lista):
    return [funcion(x) for x in lista]
    
def doble(x):
    return x*2
    
aplica(doble,[1,2,3,4,5])
    
file_path = '/Users/JavierTejedorAguilera/Documents/Cursos/DataScience&BigData(US)/Python/'

#Leemos el fichero al completo
f = open(file_path,'r')
texto = f.read()
f.close()

lineas = texto.split('\n')

#Leemos el fichero linea a linea
f = open(file_path,'r')
linea = f.readline()
f.close()

#Con with nos aseguramos que el fichero se cierra automaticamente
with open(file_path,'r') as f:
    print(f.read())


with open(file_path+'ejemplo.txt','r') as f:
    print(f.read())
    

with open(file_path+'ejemplo.txt','r', encoding='utf-8') as fr, open(file_path+'salida.txt','w', encoding='utf-8') as fs:
    texto = fr.read()    
    fs.write(texto)

with open(file_path+'ejemplo.txt','r', encoding='utf-8') as fr, open(file_path+'salida.txt','w', encoding='utf-8') as fs:
    for line in fr:
        fs.write(line)
        
        
    
import math
class Punto(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distancia_al_origen(self):
        return math.hypot(self.x, self.y)
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)
        
p1 = Punto(1,2)
p2 = Punto(3,5)

isinstance(p1,object)
isinstance(p1,Punto)

d = p1.distancia_al_origen()

print(p1)

p1.x
p1.y

p1 == p2

math.hypot(1,2)


class Circulo(Punto):
    
    def __init__(self, radio, x=0, y=0):
        super().__init__(x, y)
        self.radio = radio
    def distancia_del_borde_al_origen(self):
        return abs(self.distancia_al_origen() - self.radio)
    def area(self):
        return math.pi * (self.radio**2)
    def circunferencia(self):
        return 2 * math.pi * self.radio
    def __eq__(self, otro):
        return self.radio == (otro.radio and super().__eq__(otro,self))
    def __str__(self):
        return "Círculo({0.radio!r}, {0.x!r}, {0.y!r})".format(self)
        
import random
random.randrange(1,10)

import scipy

import numpy as np

data = np.array([1,2,3,4])
data*10
data+data

data = np.array([1,2,3,4])
data.shape

data = np.array([[1,2,3,4]])
data.shape

data = np.array([[1],[2],[3],[4]])
data.shape

np.arange(10)

np.ones(5)

np.ones_like(data)

np.zeros(10)

np.zeros_like(data)

np.eye(5,5)

np.empty([2,3])

np.array([1,2,5], dtype='float64')
np.array([1,2,5], dtype='int')

a = np.array([1,2,3,4])
b = np.array([2,7,3,5])
np.max(a)

np.maximum(a,b)

np.in1d(a,b)

names = np.array(['a','b','c','d','b'])
data = np.array([1,2,3,4,5])

data[names=='b']

import random
random.randint(1,5)

a = np.array((8,4))
for i in range(8):
    for j in range(4):
        a[i][j]=j
        
        
a= np.arange(15).reshape((3,5))

a[[1,2],[1]]

a[1,1]
a[2,1]

np.random.choice(range(100))


import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas','Oregon'])
np.abs(frame)

f = lambda x: x.max() - x.min()
frame.apply(f) # By default, it applies the function to the rows
frame.apply(f, axis=1)

