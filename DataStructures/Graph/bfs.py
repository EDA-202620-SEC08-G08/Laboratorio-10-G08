from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.Graph import digraph as G


def bfs(my_graph, source):
    """
    Recorre el grafo en anchura (por niveles) desde el vertice source.

    Retorna un mapa con la informacion de cada vertice alcanzado:
    {"marked": True, "edge_from": vertice anterior, "dist_to": numero de arcos desde source}
    """
    visited_map = mp.new_map(G.order(my_graph), 0.5)
    mp.put(visited_map, source, {"marked": True, "edge_from": None, "dist_to": 0})
    bfs_vertex(my_graph, source, visited_map)
    return visited_map


def bfs_vertex(my_graph, source, visited_map):
    """
    Visita los vertices alcanzables desde source usando una cola.
    """
    queue = q.new_queue()
    q.enqueue(queue, source)
    while not q.is_empty(queue):
        vertex = q.dequeue(queue)
        dist = mp.get(visited_map, vertex)["dist_to"]
        adjacents = G.adjacents(my_graph, vertex)
        for i in range(al.size(adjacents)):
            w = al.get_element(adjacents, i)
            if not mp.contains(visited_map, w):
                mp.put(visited_map, w, {"marked": True, "edge_from": vertex, "dist_to": dist + 1})
                q.enqueue(queue, w)
    return visited_map


def has_path_to(key_v, visited_map):
    """
    Retorna True si existe un camino desde source hasta key_v.
    """
    info = mp.get(visited_map, key_v)
    return info is not None and info["marked"]


def path_to(key_v, visited_map):
    """
    Retorna una pila con el camino desde source hasta key_v
    (el tope de la pila es source). Si no hay camino retorna None.
    """
    if not has_path_to(key_v, visited_map):
        return None
    path = st.new_stack()
    current = key_v
    while current is not None:
        st.push(path, current)
        current = mp.get(visited_map, current)["edge_from"]
    return path
