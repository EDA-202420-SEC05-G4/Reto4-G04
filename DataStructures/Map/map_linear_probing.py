from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random as rd
from DataStructures.List import array_list as al
from DataStructures.Utils import utils as ut
  

def new_map(num_keys, load_factor, prime=109345121):
    try:
        capacity = mf.next_prime(num_keys//load_factor)
        scale = rd.randint(1, prime-1)
        shift = rd.randint(0, prime-1)
        hash_table = {'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': al.new_list(),
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0,
        'type': 'PROBING'}
        for _ in range(capacity):
            entry = me.new_map_entry(None, None)
            al.add_last(hash_table['table'], entry)
        return hash_table
    except Exception as exp:
        ut.error.reraise(exp, 'Probe:newMap')
 
    
def put(my_map,key,value):
    f_s = find_slot(my_map,key,int(mf.hash_value(my_map,key)))
    if not f_s[0]:
        my_map['size'] += 1
    my_map['table']['elements'][f_s[1]] = me.new_map_entry(key,value)
    if my_map['size']/my_map['capacity'] > my_map['limit_factor']:
        rehash(my_map)
    
    
def contains(my_map,key):
    present = False
    if al.is_present(key_set(my_map),key) != -1:
        present = True
    return present


def get(my_map,key):
    f_s = find_slot(my_map,key,int(mf.hash_value(my_map,key)))
    if f_s[0]:
        return my_map['table']['elements'][f_s[1]]['value']
    else:
        return None


def remove(my_map,key):
    f_s = find_slot(my_map,key,int(mf.hash_value(my_map,key)))
    if my_map['table']['elements'][f_s[1]]['key'] != None:
        my_map['size'] -= 1
        my_map['table']['elements'][f_s[1]] = me.new_map_entry(None, None)
    """if my_map['size']/my_map['capacity'] < my_map['limit_factor']:
        my_map['capacity'] = mf.next_prime(my_map['capacity']*(1/2))"""

    
def size(my_map):
    return my_map['size']


def is_empty(my_map):
    empty=False
    if my_map['size']==0:
        empty=True
    return empty


def key_set(my_map):
    lista=al.new_list()
    for i in range (my_map['capacity']):
        if my_map['table']['elements'][i]['key'] != None:
            al.add_last(lista,my_map['table']['elements'][i]['key'])
    return lista         


def value_set(my_map):
    lista=al.new_list()
    for i in range (my_map['capacity']):
        if my_map['table']['elements'][i]['value'] != None:
            al.add_last(lista,my_map['table']['elements'][i]['value'])
    return lista  


def find_slot(my_map, key, hash_value):
    present = False
    pos = hash_value
    if al.is_present(key_set(my_map),key) != -1:
        present = True
    while (my_map['table']['elements'][pos]['key'] != key) and (my_map['table']['elements'][pos]['key'] != None) and (pos < (my_map['capacity'])):
        if (pos == my_map['capacity']-1):
            pos == 0
        else:    
            pos += 1
    return present,pos


def is_available(table,pos):
    if table['elements'][pos]['key'] == None:
        return True
    else:
        return False
    
    
def rehash(my_map):
    keys = key_set(my_map)
    values = value_set(my_map)
    my_map['size'] = 0
    my_map['capacity'] = mf.next_prime(my_map['capacity']*2)
    my_map['table'] = al.new_list()
    for _ in range(my_map['capacity']):
        entry = me.new_map_entry(None, None)
        al.add_last(my_map['table'], entry)
    for i in range(keys['size']):
        f_s = find_slot(my_map,keys['elements'][i],int(mf.hash_value(my_map,keys['elements'][i])))
        if not f_s[0]:
            my_map['size'] += 1
        my_map['table']['elements'][f_s[1]] = me.new_map_entry(keys['elements'][i],values['elements'][i])
    return my_map