from DataStructures.Priority_queue import index_priority_queue as ipq
from DataStructures.Graph import dijsktra_search as ds
from DataStructures.Map import map_linear_probing as map
from DataStructures.Graph import adj_list_graph as gr
from DataStructures.Graph import edge as edges
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack as stk
from DataStructures.Queue import queue as que
import math


def dijkstra(my_graph, source):
    search = ds.new_dijsktra_search(source)
    while not ipq.is_empty(search["pq"]):
        v = ipq.remove(search["pq"])
        edges = gr.adjacent_edges(my_graph, v)
        if edges is not None:
            for i in range(lt.size(edges)):
                edge = lt.get_element(edges, i)
                relax(search, edge)
                
    return search

def relax (search, edge) :
    v = edges.either (edge)
    w = edges.other(edge, v)
    visited_v = map.get(search["visited"], v)
    visited_w= map.get(search["visited"], w)
    distw = visited_w["dist_to" ]
    distv = visited_v["dist_to"] + edges.weight(edge)
    if (visited_w is None) or (distw > distv):
        distow = visited_v["dist_to"] + edges.weight(edge)
        map.put(search["visited"], w, {"marked": True,"edge_to": edge,"dist_to": distow})
        
    if ipq.contains(search["pq"], w):
        ipq.decrease_key(search["pq"], w, distow)
    else:
        ipq.insert(search["pa"], w, distow)
    return 

def dist_to(search,vertex):
    visited_v=map.get(search['vistied'],vertex)
    if visited_v is None:
        return math.inf
    return visited_v['dist_to']

def has_path_to(search,vertex):
    visited=map.get(search['visited'],vertex)
    if visited is not None and visited['marked']:
        return True
    return False

def path_to(search,vertex):
    if has_path_to(search,vertex) is False:
        return None
    path=stk.new_stack()
    while vertex != search['source']:
        visited_v=map.get(search['vistied'],vertex)
        edge= visited_v('edge_to')
        stk.push(path,edge)
        vertex=edges.either(edge)
    return path