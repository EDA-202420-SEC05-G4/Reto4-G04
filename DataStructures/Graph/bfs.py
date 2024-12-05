from DataStructures.Map import map_linear_probing as map
from DataStructures.Graph import adj_list_graph as graph
from DataStructures.Graph import graph_search as gs
from DataStructures.Stack import stack as stack
from DataStructures.Queue import queue as queue
from DataStructures.List import array_list as lt

def breath_first_search(my_graph, source):

    search = gs.new_graph_search(source)
    search["visited"] = map.new_map(graph.num_vertices(my_graph), load_factor=0.5)
    map.put(search["visited"], source, {"marked": True, "edge_to": None, "dist_to": 0})
    bfs_vertex(search, my_graph, source)
    return search


def bfs_vertex(search, my_graph, source):
    
    adjs_queue = queue.new_queue()
    queue.enqueue(adjs_queue, source)
    
    while not (queue.is_empty(adjs_queue)):
        vertex = queue.dequeue(adjs_queue)
        visited_v = map.get(search["visited"], vertex)
        adjs_lst = graph.adjacents(my_graph, vertex)
        
        for i in range(lt.size(adjs_lst)):
            w = lt.get_element(adjs_lst, i)
            visited_w = map.get(search["visited"], w)
            if visited_w is None:
                dist_to_w = visited_v["dist_to"] + 1
                visited_w = {"marked": True, "edge_to": vertex, "dist_to": dist_to_w}
                map.put(search["visited"], w, visited_w)
                queue.enqueue(adjs_queue, w)
                
    return search


def has_path_to(search, vertex):
    
    element = map.get(search["visited"], vertex)
    if element and element["marked"] is True:
        return True
    
    return False


def path_to(search, vertex):

    if has_path_to(search, vertex) is False:
        return None
    
    path = stack.new_stack()
    while vertex != search["source"]:
        stack.push(path, vertex)
        vertex = map.get(search["visited"], vertex)["edge_to"]
    stack.push(path, search["source"])
    
    return path

