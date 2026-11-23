from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as V
from DataStructures.Graph import edge as E


def new_graph(order):
    """
    Crea un grafo dirigido vacio.

    - vertices: mapa (linear probing) con llave = key del vertice y valor = vertice
    - num_edges: numero de arcos del grafo

    :param order: numero esperado de vertices
    :returns: grafo recien creado
    """
    graph = {
        "vertices": mp.new_map(order, 0.5),
        "num_edges": 0,
    }
    return graph


def insert_vertex(my_graph, key_u, info_u):
    """
    Inserta el vertice con llave key_u e informacion info_u.
    Si el vertice ya existe, se reemplaza por uno nuevo con la nueva informacion.

    :returns: el grafo con el vertice insertado
    """
    vertex = V.new_vertex(key_u, info_u)
    mp.put(my_graph["vertices"], key_u, vertex)
    return my_graph


def add_edge(my_graph, key_u, key_v, weight=1.0):
    """
    Agrega un arco dirigido de key_u a key_v con peso weight.
    Si el arco ya existe, se actualiza su peso.

    :raises Exception: si alguno de los vertices no existe
    :returns: el grafo con el arco agregado
    """
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    if mp.get(my_graph["vertices"], key_v) is None:
        raise Exception("El vertice v no existe")

    existing = V.get_edge(vertex_u, key_v)
    if existing is not None:
        E.set_weight(existing, weight)
    else:
        V.add_adjacent(vertex_u, key_v, weight)
        my_graph["num_edges"] += 1
    return my_graph


def contains_vertex(my_graph, key_u):
    """
    Retorna True si el vertice con llave key_u existe en el grafo.
    """
    return mp.contains(my_graph["vertices"], key_u)


def order(my_graph):
    """
    Retorna el numero de vertices del grafo.
    """
    return mp.size(my_graph["vertices"])


def size(my_graph):
    """
    Retorna el numero de arcos del grafo.
    """
    return my_graph["num_edges"]

def update_vertex_info(my_graph, key_u, new_info_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is not None:
        V.set_value(vertex, new_info_u)
    return my_graph


def vertices(my_graph):
    return mp.key_set(my_graph["vertices"])


def degree(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return V.degree(vertex)


def get_edge(my_graph, key_u, key_v):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return V.get_edge(vertex, key_v)


def get_vertex_information(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return V.get_value(vertex)


def adjacents(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return mp.key_set(V.get_adjacents(vertex))


def edges_vertex(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is None:
        raise Exception("El vertice no existe")
    return mp.value_set(V.get_adjacents(vertex))


def get_vertex(my_graph, key_u):
    return mp.get(my_graph["vertices"], key_u)
