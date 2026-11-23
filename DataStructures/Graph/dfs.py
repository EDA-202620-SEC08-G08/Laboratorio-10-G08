from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
from DataStructures.Stack import stack as st
from DataStructures.Graph import digraph as G


def dfs(my_graph, source):
    visited_map = mp.new_map(G.order(my_graph), 0.5)
    mp.put(visited_map, source, {"marked": True, "edge_from": None})
    dfs_vertex(my_graph, source, visited_map)
    return visited_map


def dfs_vertex(my_graph, vertex, visited_map):
    adjacents = G.adjacents(my_graph, vertex)
    for i in range(al.size(adjacents)):
        w = al.get_element(adjacents, i)
        if not mp.contains(visited_map, w):
            mp.put(visited_map, w, {"marked": True, "edge_from": vertex})
            dfs_vertex(my_graph, w, visited_map)
    return visited_map


def has_path_to(key_v, visited_map):
    info = mp.get(visited_map, key_v)
    return info is not None and info["marked"]


def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None
    path = st.new_stack()
    current = key_v
    while current is not None:
        st.push(path, current)
        current = mp.get(visited_map, current)["edge_from"]
    return path