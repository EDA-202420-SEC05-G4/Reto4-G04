RED = 0
BLACK = 1


def new_node(key, value, color=RED):
    """
    Crea un nuevo nodo para un árbol rojo-negro  y lo retorna.
    color:0 - rojo  color:1 - negro
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subarbol que cuelga de este nodo
        color: El color inicial del nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    Raises:
        Exception
    """
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "color": color,
        "type": "RBT",
    }

    return node


def is_red(my_node):
    """
    Informa si un nodo es rojo
    Args:
        my_node: El nodo a revisar

    Returns:
        True si el nodo es rojo, False de lo contrario
    Raises:
        Exception
    """
    if my_node == None:
        return False
    else:
        return my_node["color"] == RED


def get_value(my_node):
    """Retorna el valor asociado a una pareja llave valor
    Args:
        my_node: El nodo con la pareja llave-valor
    Returns:
        El valor almacenado en el nodo
    Raises:
        Exception
    """
    value = None
    if my_node is not None:
        value = my_node["value"]
    return value


def get_key(my_node):
    """Retorna la llave asociado a una pareja llave valor
    Args:
        my_node: El nodo con la pareja llave-valor
    Returns:
        La llave almacenada en el nodo
    Raises:
        Exception
    """
    key = None
    if my_node is not None:
        key = my_node["key"]
    return key


def change_color(my_node, color):
    """Cambia el color de un nodo
    Args:
        my_node: El nodo a cambiar
        color: El nuevo color del nodo
    Returns:
        None
    Raises:
        Exception
    """
    my_node["color"] = color


def size_(root):
    if root == None:
        return 0
    else:
        return root['size']
    

def size(node):
    return size_(node['left']) + size_(node['right']) + 1


"""def rotate_left(node):
    root = node
    node['key'] = root['right']['key']
    node['value'] = root['right']['value']
    node['right'] = root['right']['right']
    node['left'] = root
    node['left']['right'] = root['right']['left']
    node['left']['size'] = size(node['left'])
    node['size'] = root['size']
    root['size'] = size(root)
    #if root['right']['left']['color'] == RED:
    #    node['left']['right']['color'] = BLACK
    node['left']['color'] = RED
    node['color'] = root['right']['left']['color']
        
        
def rotate_right(node):
    root = node
    node['key'] = root['left']['key']
    node['value'] = root['left']['value']
    node['left'] = root['left']['left']
    node['right'] = root
    node['right']['left'] = root['left']['right']
    node['right']['size'] = size(node['right'])
    node['size'] = root['size']
    root['size'] = size(root)
    #if root['color'] == RED:
    #    node['right']['color'] = BLACK
    node['right']['color'] = RED
    node['color'] = root['left']['right']['color']"""
    
    
def rotate_left(node):
    root = node['right']
    node['right'] = root['left']
    root['left'] = node
    root['color'] = root['left']['color']
    root['left']['color'] = RED
    root['size'] = node['size']
    node['size'] = size(node)
    return root
    
    
def rotate_right(node):
    root = node['left']
    node['left'] = root['right']
    root['right'] = node
    root['color'] = root['right']['color']
    root['right']['color'] = RED
    root['size'] = node['size']
    node['size'] = size(node)
    return root


def flip_node_color(node):
    """
    Cambiar el color del nodo: RED pasa a BLACK y 
    BLACK pasa a RED.
    """
    if node != None:
        if is_red(node):
            node['color'] = BLACK
        else:
            node['color'] = RED
        
        
def flip_colors(node):
    """
    Cambiar los colores del nodo y de sus hijos izquierdo 
    y derecho.
    """
    flip_node_color(node)
    flip_node_color(node['right'])
    flip_node_color(node['left'])