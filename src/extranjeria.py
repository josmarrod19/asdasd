# -*- coding: utf-8 -*-
'''
Created on 16 jun. 2019
@author: reinaqu
AUTOR: Toñi Reina
REVISOR: Mariano González, Fermín Cruz
ÚLTIMA MODIFICACIÓN: 16/6/2019

En este ejercicio trabajaremos sobre un fichero en formato CSV que tiene información sobre la
población extranjera empadronada en los distintos distritos y barrios de Sevilla
A continuación se muestran las primeras cinco líneas de dicho fichero. Fíjese que la 
primera línea es la cabecera con los datos de las columnas:

"DISTRITO","SECCION","BARRIO","PAIS_NACIMIENTO","HOMBRES","MUJERES"
" 01"," 001","SANTA CATALINA","ALEMANIA",8,6
" 01"," 001","SANTA CATALINA","ARGELIA",0,1
" 01"," 001","SANTA CATALINA","ARGENTINA",2,4
" 01"," 001","SANTA CATALINA","ARMENIA",0,1


Cada línea se identifica con el número de extranjeros de un pais en un distrito, 
sección y barrio, de forma que: el primer valor se corresponde con el código del distrito;
el segundo es el código de la sección dentro del distrito; el tercero el nombre del barrio;
el cuarto el país de procedencia del extranjero; el quinto el número de hombres de ese país 
empadronados en ese barrio; y, el último, el número de mujeres de ese pais empadronados 
en se barrio.
Siga las instrucciones e implemente las funciones que aparecen a continuación.
   
'''

import csv
from collections import namedtuple

DatosExtranjeros = namedtuple('DatosExtranjeros', 'distrito,seccion,barrio,pais,hombres,mujeres')

# Apartado a - 1 punto ----------------------------------------------------------------------
def lee_datos_extranjeros(fichero):
    '''
    Lee un fichero de entrada y devuelve una lista de tuplas . 
    Tenga en cuenta que los tipos numéricos deben ser de tipo int.
    
    Entrada:
     - fichero: ruta del fichero csv que contiene los datos en codificación utf-8 
         -> str

    Salida:
     - registros: lista de tuplas con la información de los Extranjeros
         -> [DatosExtranjeros(str,str,str,str,int,int)]   
    '''
    pass
# Apartado b - 0,5 puntos ----------------------------------------------------------------------
def numero_nacionalidades_distintas(registros):
    
    '''
    Devuelve el número de nacionalidades distintas presentes en los registros dados como parámetro. 
    Entrada:
     - registros: lista de tuplas con la información de extranjeros -> [DatosExtranjeros(...)]
    Salida:
     - número de nacionalidades distintas -> int
    '''    
    pass
    


# Apartado c - 0,5 puntos ----------------------------------------------------------------------
def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    '''Devuelve una lista de tuplas (distrito, seccion) con las secciones y sus distritos
       en las que hay extranjeros del conjunto de paises dados como parámetros.
       La lista de tuplas estará ordenada por distrito. 
    Entrada:
     - registros: lista de tuplas con la información de extranjeros -> [DatosExtranjeros(...)]
     - paises: conjunto con los nombres de los paises buscados -> set(str)
    Salida:
     - Devuelve una lista de tuplas (distrito, seccion) ordenada por distritos con
       las secciones y sus distrintos en las que hay extrajeros de los paises
       dados como parámetro. La lista de tuplas estará ordenada por distrito -> list((distrito,seccion))
       
    '''
    pass



# Apartado d - 1 punto ----------------------------------------------------------------------
def total_extranjeros_por_pais(registros):
    '''
    Devuelve un diccionario en el que las claves son los países y los valores
    el número total de extranjeros (tanto hombres como mujeres) de ese país. 
    Entrada:
     - registros: lista de tuplas con la información de extranjeros -> [DatosExtranjeros(...)]
    Salida:
     - diccionario[pais:total_extranjeros] con el número total de extranjeros por 
       país -> {str:int}
    '''
    pass


# Apartado e - 1,5 puntos ----------------------------------------------------------------------
def top_n_extranjeria (registros, n=3):
    
    '''
    Devuelve una lista de tuplas (pais, numero_extranjeros) con los n paises
    de los que hay más población extranjera en los registros pasados como parámetro. 
    Entrada:
     - registros: lista de tuplas con la información de extranjeros -> [DatosExtranjeros(...)]
     - n: Número de elementos de la lista resultante
    Salida:
     - lista de tuplas (pais, numero_extranjeros) con los n paises de los que hay
       más población extranjera
   '''
    pass


# Apartado f - 1,5 puntos ----------------------------------------------------------------------
def barrio_mas_multicultural(registros):
    '''
    Devuelve el nombre del barrio en el que hay un mayor número de nacionalidades distintas 
    Entrada:
     - registros: lista de tuplas con la información de extranjeros -> [DatosExtranjeros(...)]
    Salida:
     - El nombre del barrio con más nacionalidades distintas -> str
    '''
    pass

# Apartado g - 2 puntos ----------------------------------------------------------------------
def barrio_con_mas_extranjeros(registros, tipo=None):
    '''
    Devuelve el nombre del barrio en el que hay un mayor número de extranjeros, bien
    sea en total (tanto hombres como mujeres) si tipo tiene el valor None, bien
    sea de hombres si tipo es 'Hombres' o mujeres si el tipo es 'Mujeres'
    Entrada:
     - registros: lista de tuplas con la información de extranjeros -> [DatosExtranjeros(...)]
     - tipo: Cadena que representa el tipo de extranjeros a contar, puede tomar los valores None,
        'Hombres' o 'Mujeres'
    Salida:
     -  nombre del barrio con mayor número de extranjeros, bien hombres, bien mujeres,
        bien total (dependiendo del valor del parámetro tipo)-> str
    '''    
    pass
        

# Apartado h - 2 puntos ----------------------------------------------------------------------   
def pais_mas_representado_por_distrito(registros): 
    '''
    Devuelve un diccionario {distrito:pais} en el que las claves son los distritos y los valores
    el país del que hay más extranjeros en el distrito dado por la clave. 
    Entrada:
     - registros: lista de tuplas con la información de extranjeros -> [DatosExtranjeros(...)]
    Salida:
     - diccionario[distrito:pais] en el que las claves son los distritos y los valores
    el país del que hay más extranjeros en el distrito dado por la clave -> {str:str}
    '''
    pass

