from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False
def new_heap(is_min_pq=True):
    heap={
        "elements":al.new_list(),
        "size":0,
        "cmp_function":None,
        
    }
    if is_min_pq:
        heap["cmp_function"]=default_compare_lower_value
    else:
        heap["cmp_function"]=default_compare_higher_value
        
    al.add_last(heap["elements"],None)
    return heap

def size(my_heap):
    return my_heap["size"]


def is_empty(my_heap):
    return size(my_heap) == 0


def priority(my_heap, parent, child):
    cmp = my_heap["cmp_function"]
    return cmp(parent, child)


def exchange(my_heap, i, j):
    al.exchange(my_heap["elements"], i, j)

def swim(my_heap, pos):
    while pos>1:
        parent_pos=pos//2
        parent=al.get_element(my_heap["elements"],parent_pos)
        child=al.get_element(my_heap["elements"],pos)
        if priority(my_heap,parent,child):
            break
        exchange(my_heap,parent_pos,pos)
        pos=parent_pos
def insert(my_heap,priority_value,value):
    entry=pqe.new_pq_entry(priority_value,value)
    al.add_last(my_heap["elements"],entry)
    my_heap["size"]+=1
    swim(my_heap,my_heap["size"])
    return my_heap
           