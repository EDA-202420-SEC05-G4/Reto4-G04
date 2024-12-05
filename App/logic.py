import time
import os
import csv
import datetime
from tabulate import tabulate
import ast
import sys
import json
import ast 

from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rbn
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as lt
from DataStructures.Map import map_linear_probing as map
from DataStructures.Map import map_functions as mf
from DataStructures.Graph import adj_list_graph as gr

data_dir = os.path.dirname(os.path.realpath('__file')) + '/Data/'


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    graph = gr.new_graph(1000,True)
    
    return graph


# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    info = "/users_info_10.csv"
    relations = "/relationships_10.csv"
    info = csv.DictReader(open(data_dir+info, encoding="utf-8"), delimiter=";")
    relations = csv.DictReader(open(data_dir+relations, encoding="utf-8"), delimiter=";")
    #i = 1
    for user in info:
        hobbies = ast.literal_eval(user['HOBBIES'])
        user['HOBBIES'] = hobbies
        user['USER_ID'] = int(float(user['USER_ID']))
        user['AGE'] = int(float(user['AGE']))
        user['LATITUDE'] = float(user['LATITUDE'])
        user['LONGITUDE'] = float(user['LONGITUDE'])
        catalog = gr.insert_vertex(catalog,user['USER_ID'],user)
    print(catalog['vertices']['size'])
    
    for relation in relations:
        key_a = int(relation['FOLLOWER_ID'])
        key_b = int(relation['FOLLOWED_ID'])
        weight = relation['START_DATE']
        catalog = gr.add_edge(catalog,key_a,key_b,weight)
    print(catalog['edges'])
    
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,Id_1,Id_2):
    """
    Retorna el resultado del requerimiento 1
    """
    recorrido=gr.bfs(catalog,Id_1)
    camino=bfs.pathTo(recorrido,Id_2)
    info_usuarios=[]
    for i in camino:
        info_usuarios.append(gr.get_vertex_information(catalog),i)
    return info_usuarios


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
