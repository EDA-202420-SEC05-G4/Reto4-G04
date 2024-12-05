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
from DataStructures.Graph import dfs as dfs
from DataStructures.Graph import bfs as bfs
from DataStructures.Graph import dfo as dfo
from DataStructures.Graph import dijsktra as dijsktra
from DataStructures.Graph import prim as prim


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
    recorrido=bfs.breath_first_search(catalog,Id_1)
    camino=bfs.path_to(recorrido,Id_2)
    info_usuarios=[]
    for i in camino:
        info_usuarios.append(gr.get_vertex_information(catalog),i)
    return info_usuarios


def req_2(catalog,Id_1,Id_2):

    if gr.get_vertex_information(catalog,Id_1)['USER_TYPE']=='basic' and gr.get_vertex_information(catalog,Id_2)['USER_TYPE']=='basic':
        recorrido=bfs.breath_first_search(catalog,Id_1)
        camino=bfs.path_to(recorrido,Id_2)
        info_usuarios=[]
        for i in camino:
            info_usuarios.append(gr.get_vertex_information(catalog,i))
    else:
        info_usuarios='Los usuarios no son de tipo básico'
    return info_usuarios,len(info_usuarios)


def req_3(catalog,Id):
    
    max=0
    max_amigo=()
    for i in map.get(catalog['vertices'],Id):
        if is_friend(catalog,Id,i):
            if al.size(map.get(catalog['vertices'],i))>=max:
                max=(al.size(map.get(catalog['vertices'],i)),i)
                max_amigo=i
    return max,max_amigo

def is_friend(catalog,A_id, B_id):
    if al.is_present(map.get(catalog['vertices'],A_id),B_id):
        if al.is_present(map.get(catalog['vertices'],B_id),A_id):
            return True
    else:
        return False

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
