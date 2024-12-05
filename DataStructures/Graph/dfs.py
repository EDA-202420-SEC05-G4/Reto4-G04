from DataStructures.Map import map_linear_probing as map
from DataStructures.Graph import adj_list_graph as graph
from DataStructures.Graph import graph_search as gs
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack as stk


def depth_first_search(my_graph, source):

    search = gs.new_graph_search(source)
    search["visited"] = map.new_map(graph.num_vertices(my_graph),load_factor=0.5,)
    
    map.put(search["visited"], source, {"marked": True, "edge_to": None})
    dfs_vertex(search, my_graph, source)
    
    return search

def dfs_vertex(search, my_graph, vertex):
    
    adj_list = graph.adjacents(my_graph, vertex)
    for i in range(lt.size(adj_list)):
        w = lt.get_element(adj_list, i)
        visited = map.get(search["visited"], w)
        if visited is None:
            map.put(search["visited"], w, {"marked": True, "edge_to": vertex})
            dfs_vertex(search, my_graph, w)
    return search

def has_path_to(search, vertex):
    
    element = map.get(search["visited"], vertex)
    if element and element["marked"] is True:
        return True
    
    return False

def path_to(search, vertex):
    
    if has_path_to(search, vertex) is False:
        return None
    path = stk.new_stack()
    while vertex != search["source"]:
        stk.push(path, vertex)
        vertex = map.get(search["visited"], vertex)["edge_to"]
    stk.push(path, search["source"])
    
    return path



