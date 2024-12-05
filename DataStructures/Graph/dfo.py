from DataStructures.Map import map_linear_probing as map
from DataStructures.Graph import adj_list_graph as gr
from DataStructures.Graph import dfo_search as ds
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack as stk
from DataStructures.Queue import queue as que


def depth_first_order(graph):
    """
    Iniciar un recorrido Depth FirstOrder(**DFO**) sobre el grafo. 
    Y luego se ejecuta el recorrido con la función dfs_vertex(…) que realiza un recorrido DFS
    """
    search= ds.new_dfo_search()
    search['marked'] = map.new_map(gr.num_vertices(graph), load_factor = 0.75)

    lst_vtcs = gr.vertices(graph)
    for i in range(lt.size(lst_vtcs)):    # recorrer todos los vertices
        vertex = lt.get_element(lst_vtcs, i)
        if not map.contains(search['marked'], vertex):
            dfs_vertex(graph, search, vertex)  # iniciar un nuevo recorrido DFS
    
    
    return search


def dfs_vertex(graph, search, vertex):
    """
    Aplicar el algoritmo DFS desde vertex actualizando los recorridos "pre", "post", "reversepost"
    Solución:
    1. Encolar el vertice vertex en la cola search["pre"]
    2. Marcar el vertice vertex en el mapa search["marked"]
    3. Recorrer los adyacentes v de vertex
    3.1    Si el adyacente v No esta marcado en el mapa search["marked"]
    3.1.1        Aplicar recursión desde el verticev
    4. Encolar el verticevertexen la cola search["post"]
    5. Agregar el verticevertexen el stacksearch["reversepost"]
    6. Retornar search
    """
    
    que.enqueue(search["pre"],vertex)
    
    map.put(search['marked'],vertex,{"marked": True, "edge_to": None})
    
    adj_list = gr.adjacents(graph, vertex)
    for i in range(lt.size(adj_list)):
        w = lt.get_element(adj_list, i)
        if map.get(search['marked'],w) is None:
            map.put(search["marked"], w, {"marked": True, "edge_to": vertex})
            dfs_vertex(graph, search , w)
    
    que.enqueue(search['post'],vertex)
    
    stk.push(search['reversepost'],vertex)
    
    return search
    


def topological_sort(graph):
    """
    Retornar el orden topologicoa partir del resultado del algoritmo DFO sobre el grafo.
    Returns:
    search["reverse_post"]resultado del algoritmo DFO
    Solución:
    1. Ejecutar el algoritmo DFO sobre el grafo obteniendo la estructura searchresultante
    2. Retornar search["reversepost"]
    """
    search = depth_first_order(graph)
    
    return search['reversepost']