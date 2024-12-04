from DataStructures.Map import map_linear_probing as map
from DataStructures.List import array_list as lt
from DataStructures.Graph import edge as e
from DataStructures.Utils import error as error


def new_graph(size=19,directed=False):
    
    g = {'vertices' : map.new_map(size,0.5),
         'information' : map.new_map(size,0.5),
         'in_degree' : None,
         'edges' : 0,
         'directed' : directed,
         'type' : 'ADJ_LIST'
    }
    
    return g


def insert_vertex(graph, key, info):
    """Inserta el vertice vertex en el grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea insertar
    Returns:
        El grafo graph con el nuevo vertice
    Raises:
        Exception"""
    try:
        edges = lt.new_list()
        map.put(graph['vertices'], key, edges)
        map.put(graph['information'], key, info)
        if (graph['directed']):
            map.put(graph['indegree'], key, 0)
        return graph
    except Exception as exp:
        error.reraise(exp, 'ajlist:insertvertex')


def removeVertex(graph, vertex):
    """
    Remueve el vertice vertex del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea remover
    Returns:
        El grafo sin el vertice vertex
    Raises:
        Exception
    """
    # TODO
    pass


def num_vertices(graph):
    """
    Retorna el numero de vertices del  grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices del grafo
    Raises:
        Exception
    """
    try:
        return map.size(graph['vertices'])
    except Exception as exp:
        error.reraise(exp, 'ajlist:numtvertex')


def num_edges(graph):
    """
    Retorna el numero de arcos en el grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices del grafo
    Raises:
        Exception
    """
    try:
        return (graph['edges'])
    except Exception as exp:
        error.reraise(exp, 'ajlist:numedges')


def vertices(graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        La lista con los vertices del grafo
    Raises:
        Exception
    """
    try:
        lstmap = map.key_set(graph['vertices'])
        return lstmap
    except Exception as exp:
        error.reraise(exp, 'ajlist:vertices')


def edges(graph):
    """
    Retorna una lista con todos los arcos del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        Una lista con los arcos del grafo
    Raises:
        Exception
    """
    try:
        lstmap = map.value_set(graph['vertices'])
        lstresp = lt.new_list()
        for lstedge in lstmap['elements']:
            for edge in lstedge['elements']:
                if (graph['directed']):
                    lt.add_last(lstresp, edge)
                elif (lt.is_present(lstresp, edge,e.compare_edges_not_directed) == -1):
                    lt.add_last(lstresp, edge)
        return lstresp
    except Exception as exp:
        error.reraise(exp, 'ajlist:edges')


def degree(graph, key):
    """
    Retorna el numero de arcos asociados al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    try:
        element = map.get(graph['vertices'], key)
        if element is not None:
            return (lt.size(element))
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'ajlist:degree')


def in_degree(graph, key):
    """
    Retorna el numero de arcos que llegan al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    try:
        if (graph['directed']):
            d = map.get(graph['in_degree'], key)
        else:
            d = degree(graph,key)
        return d
            
    except Exception as exp:
        error.reraise(exp, 'ajlist:indegree')


def out_degree(graph, key):
    """
    Retorna el numero de arcos que salen del grafo vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    try:
        return degree(graph,key)
    except Exception as exp:
        error.reraise(exp, 'ajlist:outdegree')


def get_edge(graph, key_a, key_b):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice destino

    Returns:
        El arco que une los verices vertexa y vertexb
    Raises:
        Exception
    """
    try:
        lst = map.get(graph['vertices'], key_a)
        for edge in lst['elements']:
            if (e.either(edge) == key_a and
               (e.other(edge, e.either(edge)) == key_b)):
                return edge
        return None
    except Exception as exp:
        error.reraise(exp, 'ajlist:getedge')


def get_vertex_information(graph, key):
    """Retorna la informacion asociada al vertice con llave key

    Parameters:
    my_graph (adj_list_graph) El grafo sobre el que se ejecuta la operacion
    key_vertex (any) Vertice del que se quiere la informacion

    Returns:
    La informacion asociada al vertice. Retorna None en caso de que el vertice no exista.

    Return type: any"""
    try:
        return map.get(graph['information'],key)
    except Exception as exp:
        error.reraise(exp, 'ajlist:get_vertex_information')
        

def contains_vertex(graph, key):
    """
    Retorna si el vertice vertex esta presente en el grafo

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: Vertice que se busca

    Returns:
       True si el vertice esta presente
    Raises:
        Exception
    """
    try:
        return map.contains(graph['vertices'], key)
    except Exception as exp:
        error.reraise(exp, 'ajlist:containsvertex')


def add_edge(graph, vertexa, vertexb, weight=0):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight.
    Si el grafo es no dirigido se adiciona dos veces el mismo arco,
    en el mismo orden
    Si el grafo es dirigido se adiciona solo el arco vertexa --> vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice de destino
        wight: peso del arco

    Returns:
       El grafo con el nuevo arco
    Raises:
        Exception
    """
    try:
        if contains_vertex(graph,vertexa) and contains_vertex(graph,vertexb):
            edge = get_edge(graph,vertexa,vertexb)
            if edge is not None:
                e.set_weight(edge,weight)
                if (not graph['directed']):
                    edgeb = get_edge(graph,vertexb,vertexa)
                    e.set_weight(edgeb,weight)
            else:
                edge = e.new_edge(vertexa, vertexb, weight)
                entrya = map.get(graph['vertices'], vertexa)
                lt.add_last(entrya, edge)
                if (not graph['directed']):
                    entryb = map.get(graph['vertices'], vertexb)
                    edgeb = e.new_edge(vertexb, vertexa, weight)
                    lt.add_last(entryb, edgeb)
                else:
                    degree = map.get(graph['in_degree'], vertexb)
                    map.put(graph['in_degree'], vertexb, degree+1)
                graph['edges'] += 1
        return graph
    except Exception as exp:
        error.reraise(exp, 'ajlist:addedge')


def adjacents(graph, vertex):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de adyacencias
    Raises:
        Exception
    """
    try:
        lst = map.get(graph['vertices'], vertex)
        lstresp = lt.new_list()
        for edge in lst['elements']:
            v = e.either(edge)
            lt.add_last(lstresp, e.other(edge, v))
        return lstresp
    except Exception as exp:
        error.reraise(exp, 'ajlist:adjacents')


def adjacent_edges(graph, vertex):
    """
    Retorna una lista con todos los arcos asociados a los vértices
    adyacentes de vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de arcos adyacentes
    Raises:
        Exception
    """
    try:
        lst = map.get(graph['vertices'], vertex)
        if lst is not None:
            return lst
        else:
            return lt.new_list()
    except Exception as exp:
        error.reraise(exp, 'ajlist:adjacentEdges')
