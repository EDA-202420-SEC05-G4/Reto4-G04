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
from DataStructures.Graph import edge as e


data_dir = os.path.dirname(os.path.realpath('__file')) + '/Data/'


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    graph = gr.new_graph(1000,True)
    graph['basic'] = 0
    graph['premium'] = 0
    graph['citys'] = {}
    
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
 
    for user in info:
        hobbies = ast.literal_eval(user['HOBBIES'])
        user['HOBBIES'] = hobbies
        user['USER_ID'] = int(float(user['USER_ID']))
        user['AGE'] = int(float(user['AGE']))
        user['LATITUDE'] = float(user['LATITUDE'])
        user['LONGITUDE'] = float(user['LONGITUDE'])
        if user['USER_TYPE'] == 'basic':
            catalog['basic'] += 1
        else:
            catalog['premium'] += 1
        if user['CITY'] in catalog['citys']:
            catalog['citys'][user['CITY']] += 1
        else:
            catalog['citys'][user['CITY']] = 1
        catalog = gr.insert_vertex(catalog,user['USER_ID'],user)
    #print(catalog['citys'])
    
    for relation in relations:
        key_a = int(relation['FOLLOWER_ID'])
        key_b = int(relation['FOLLOWED_ID'])
        weight = relation['START_DATE']
        catalog = gr.add_edge(catalog,key_a,key_b,weight)
    #print(catalog['edges'])
    
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,Id_1,Id_2):
    start_time=get_time()
    recorrido=bfs.breath_first_search(catalog,Id_1)
    camino=bfs.path_to(recorrido,Id_2)
    info_usuarios=[]
    for i in camino:
        info_usuarios.append(gr.get_vertex_information(catalog,i))
    end_time=get_time()
    delta_time=end_time-start_time
    return info_usuarios,delta_time


def req_2(catalog,Id_1,Id_2):
    start_time=get_time()
    if gr.get_vertex_information(catalog,Id_1)['USER_TYPE']=='basic' and gr.get_vertex_information(catalog,Id_2)['USER_TYPE']=='basic':
        recorrido=bfs.breath_first_search(catalog,Id_1)
        camino=bfs.path_to(recorrido,Id_2)
        info_usuarios=[]
        for i in camino:
            info_usuarios.append(gr.get_vertex_information(catalog,i))
    else:
        info_usuarios='Los usuarios no son de tipo básico'
    end_time=get_time()
    delta_time=end_time-start_time
    return info_usuarios,len(info_usuarios),delta_time


def req_3(catalog,Id):
    start_time=get_time()
    max=0
    max_amigo=()
    for i in map.get(catalog['vertices'],Id):
        if is_friend(catalog,Id,i):
            if al.size(map.get(catalog['vertices'],i))>=max:
                max=(al.size(map.get(catalog['vertices'],i)),i)
                max_amigo=i
    end_time=get_time()
    delta_time=end_time-start_time
    return max,max_amigo,delta_time


def is_friend(catalog,A_id, B_id):
    if al.is_present(map.get(catalog['vertices'],A_id),B_id):
        if al.is_present(map.get(catalog['vertices'],B_id),A_id):
            return True
    else:
        return False


def req_4(catalog):
    start_time=get_time()
    amigos_comun=[]
    for i in map.get(catalog['vertices'],Id_A)['elements']:
        if al.is_present(map.get(catalog['vertices'],Id_B),i):
            amigos_comun.append(i)
    end_time=get_time()
    delta_time=end_time-start_time
    return amigos_comun,delta_time


def req_5(catalog, Id, N):
    """
    Retorna el resultado del requerimiento 5
    """
    st = get_time()
    adlist = map.get(catalog['vertices'],Id)
    adlist2 = al.new_list()
    for i in adlist['elements']:
        if is_friend(catalog,Id,i):
            al.add_last(adlist2,i)
    
    al.quick_sort(adlist2,sortcrit5)
    list = al.sub_list(adlist,0,N)
    et = get_time()
    return list,delta_time(st,et)

def sortcrit5(catalog,Id1,Id2):
    is_sorted = False
    if gr.out_degree(catalog,Id1) > gr.out_degree(catalog,Id2):
        is_sorted = True
    return is_sorted


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
