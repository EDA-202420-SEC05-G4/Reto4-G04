from DataStructures.Tree import bst_node as bsn
from DataStructures.List import array_list as al

def default_function(k1,k2):
    if k1 > k2:
        return 1
    elif k1 < k2:
        return -1
    elif k1 == k2:
        return 0

def new_map(cmp_function=default_function):
    bst = {'root': None, 
        'cmp_function': cmp_function, 
        'type': 'BST'}
    return bst

def insert_node(root,key,value,cmp):
    if root == None:
        root = bsn.new_node(key,value)
    elif cmp(key,root['key']) == 0:
        root['value']  = value
    elif cmp(key,root['key']) == 1:
        if root['right'] == None or cmp(root['right']['key'],key) != 0:
            root['size'] += 1
        root['right'] = insert_node(root['right'],key,value,cmp)
    else:
        if root['left'] == None or cmp(root['left']['key'],key) != 0:
            root['size'] += 1
        root['left'] = insert_node(root['left'],key,value,cmp)
    return root

def put(my_bst,key,value):
    cmp = my_bst['cmp_function']
    my_bst['root'] = insert_node(my_bst['root'],key,value,cmp)
    #print(my_bst['root'])
    return my_bst

def get_node(root,key,cmp):
    if root == None:
        ret = None
    elif cmp(key,root['key']) == 0:
        ret = root['value']
    elif cmp(key,root['key']) == 1:
        ret = get_node(root['right'],key,cmp)
    elif cmp(key,root['key']) == -1:
        ret = get_node(root['left'],key,cmp)
    return ret

def get(my_bst, key):
    cmp = my_bst['cmp_function']
    ret = get_node(my_bst['root'],key,cmp)
    return ret

def contains(my_bst,key):
    ret = False
    if get(my_bst,key) != None:
        ret = True
    return ret

def is_empty(my_bst):
    ret = True
    if my_bst['root'] != None:
        ret = False
    return ret

def size_tree(root):
    return root['size']

def size(my_bst):
    ret = 0
    if is_empty(my_bst):
        ret = 0
    elif not is_empty(my_bst):
        ret = size_tree(my_bst['root'])
    return ret

def in_order_keys(root):
    order = []
    if root == None:
        None
    elif root['right'] == None and root['left'] == None:
        order = [root['key']]
    else:
        order = in_order_keys(root['left']) + [root['key']] + in_order_keys(root['right'])
    return order
    
def in_order_values(root):
    order = []
    if root == None:
        None
    elif root['right'] == None and root['left'] == None:
        order = [root['value']]
    else:
        order = in_order_values(root['left']) + [root['value']] + in_order_values(root['right'])
    return order

def key_set_tree(root):
    order = in_order_keys(root)
    key_set = al.new_list()
    for i in order:
        al.add_last(key_set,i)
    return key_set

def value_set_tree(root):
    order = in_order_values(root)
    value_set = al.new_list()
    for i in order:
        al.add_last(value_set,i)
    return value_set

def key_set(my_bst):
    return key_set_tree(my_bst['root'])

def value_set(my_bst):
    return value_set_tree(my_bst['root'])

def right_key_node(root):
    if root == None:
        return None
    elif root['right']==None:
        return root['key']
    else:
        return right_key_node(root['right'])

def left_key_node(root):
    if root == None:
        return None
    elif root['left']==None:
        return root['key']
    else:
        return left_key_node(root['left'])

def min_key(my_bst):
    return left_key_node(my_bst['root'])

def max_key(my_bst):
    return right_key_node(my_bst['root'])

def delete_left_tree(root):
    if root == None:
        None
    elif root['left']==None:
        None
    elif root['left']['left']==None:
        root['left'] = None
        root['size'] -= 1
    else:
        root['size'] -= 1
        delete_left_tree(root['left'])

def delete_right_tree(root):
    if root == None:
        None
    elif root['right']==None:
        None
    elif root['right']['right'] == None:
        root['right'] = None
        root['size'] -= 1
    else:
        root['size'] -= 1
        delete_right_tree(root['right'])

def delete_min(my_bst):
    delete_left_tree(my_bst['root'])
    
def delete_max(my_bst):
    delete_right_tree(my_bst['root'])
    
def floor_key(root,key,cmp):
    order = in_order_keys(root)
    pre = None
    if len(order) == 0:
        return pre 
    i = 0
    while (i<len(order)) and ((cmp(order[i],key) == -1) or (cmp(order[i],key) == 0)):
        pre = order[i]
        i += 1
    return pre

def floor(my_bst,key):
    cmp = my_bst['cmp_function']
    pre = floor_key(my_bst['root'],key,cmp)
    return pre

def ceiling_key(root,key,cmp):
    order = in_order_keys(root)
    pos = None
    if len(order) == 0:
        return pos
    i = -1
    while (abs(i)<=len(order)) and ((cmp(order[i],key) == 1) or (cmp(order[i],key) == 0)):
        pos = order[i]
        i -= 1
    return pos

def ceiling(my_bst,key):
    cmp = my_bst['cmp_function']
    pos = ceiling_key(my_bst['root'],key,cmp)
    return pos

def select_key(root,pos):
    order = in_order_keys(root)
    key = None
    if pos >= len(order):
        None
    else:
        for i in range(pos+1):
            key = order[i]
    return key

def select(my_bst,pos):
    return select_key(my_bst['root'],pos)

def rank_keys(root,key,cmp):
    order = in_order_keys(root)
    rank = 0
    if len(order) == 0:
        None
    else:
        i = 0
        while (i<len(order)) and (cmp(order[i],key) == -1):
            rank += 1
            i += 1
    return rank

def rank(my_bst,key):
    cmp = my_bst['cmp_function']
    rank = rank_keys(my_bst['root'],key,cmp)
    return rank

def height_tree(root):
    if root == None:
        h = -1
    else:
        h_right = height_tree(root['right'])
        h_left = height_tree(root['left'])
        h =  max(h_left,h_right) + 1
    return h

def height(my_bst):
    return height_tree(my_bst['root'])

def keys_range(root,ki,kf,cmp):
    order = in_order_keys(root)
    rango = al.new_list()
    for i in order:
        if (cmp(i,ki)==1 or cmp(i,ki)==0) and (cmp(i,kf)==-1 or cmp(i,kf)==0):
            al.add_last(rango,i)
    return rango

def keys(my_bst,ki,kf):
    return keys_range(my_bst['root'],ki,kf,my_bst['cmp_function'])

def values_range(root,ki,kf,cmp):
    order = in_order_keys(root)
    order_v = in_order_values(root)
    rango = al.new_list()
    i = 0
    for i in range(len(order)):
        if (cmp(order[i],ki)==1 or cmp(order[i],ki)==0) and (cmp(order[i],kf)==-1 or cmp(order[i],kf)==0):
            al.add_last(rango,order_v[i])
    return rango

def values(my_bst,ki,kf):
    return values_range(my_bst['root'],ki,kf,my_bst['cmp_function'])
"""
def is_empty(my_bst):
    ret = True
    if my_bst['root'] != None:
        ret = False
    return ret

def size_tree(root):
    return root['size']

def size(my_bst):
    ret = 0
    if is_empty(my_bst):
        ret = 0
    elif not is_empty(my_bst):
        ret = size_tree(my_bst['root'])
    return ret

def min_key_node(root):
    if root['left'] == None:
        tr = root['key']
    else:
        tr = min_key_node(root['left'])
    return tr

def min_key(my_bst):
    if is_empty(my_bst):
        tr = None
    else:
        tr = min_key_node(my_bst['root'])
    return tr

def max_key_node(root):
    if root['right'] == None:
        tr = root['key']
    else:
        tr = max_key_node(root['right'])
    return tr

def max_key(my_bst):
    if is_empty(my_bst):
        tr = None
    else:
        tr = max_key_node(my_bst['root'])
    return tr

def delete_left_tree(root):
    next = root['left']
    if next['left'] == None:
        root['left'] = next['right']
        root['size'] -= 1
        tr = root
    else:
        tr = delete_left_tree(next)
    return tr

def delete_min(my_bst):
    if is_empty(my_bst):
        tr = my_bst
    else:
        my_bst['root'] = delete_left_tree(my_bst['root'])
        tr = my_bst
    return tr"""
    