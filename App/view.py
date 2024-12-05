import sys
from App import logic
from tabulate import tabulate
import json
import ast
from DataStructures.Map import map_linear_probing as map
from DataStructures.List import array_list as al
from DataStructures.Graph import adj_list_graph as gr
from DataStructures.Graph import adj_list_graph as gr


def new_logic():
    """
        Se crea una instancia del controlador
    """
    return logic.new_logic()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")


def sort_criteria(element1, element2):
    is_sorted = False
    if element1[1] < element2[1]:
        is_sorted = True
    return is_sorted


def load_data(control):
    """
    Carga los datos
    """
    control = logic.load_data(control)
    headers = ['Usuarios','Conexiones','Basic','Premium','Promedio Seguidores','Cuidad con más seguidores']
    keys = map.key_set(control['in_degree'])
    promedio = 0
    for key in keys['elements']:
        promedio += map.get(control['in_degree'],key)
    users = control['vertices']['size']
    #print(users)
    #print(control['edges'])
    #print(control['basic'])
    #print(control['premium'])
    promedio = promedio/users
    #print(promedio)
    citys_list = list(control['citys'].keys())
    #print(citys_list)
    citys = al.new_list()
    for city in citys_list:
        al.add_last(citys,[city,control['citys'][city]])
    #print(citys['elements'])
    citys = al.quick_sort(citys,sort_criteria)
    #print(citys['elements'])
    city = citys['elements'][-1]
    #print(city)
    table = [[str(users),str(control['edges']),str(control['basic']),str(control['premium']),str(round(promedio,2)),city[0]+': '+str(city[1])]]
    print(tabulate(table, headers, tablefmt="simple"))
    print('\n')
    return control


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass


def print_req_1(control,id_1,id_2):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    respuesta, time = logic.req_1(control,id_1,id_2)
    headers = ['ID','Alias','Tipo de usuario']
    table = []
    check = True
    
    if len(respuesta) == 0:
        check = False
        
    else:
        for user in respuesta:
            id = user['USER_ID']
            nombre = user['USER_NAME']
            tipo = user['USER_TYPE']
            table.append([id,nombre,tipo])
            
    if check:
        print('El requerimiento duró:'+str(time))
        print('Hay '+str(len(respuesta))+' personas en el camino\n')
        print(tabulate(table, headers, tablefmt="simple"))
        
    else:
        print('No se encontraron relaciones')


def print_req_2(control,Id_1,Id_2):
    list,cantidad,time=logic.req_1(control,Id_1,Id_2)
    headers = ['ID','Nombre']
    table = []
    check = True
    
    if al.size(list) == 0:
        check = False
    else:
        for i in list:
            Id = i
            info = gr.get_vertex_information(control,Id)
            nombre = info['USER_NAME']
            table.append([Id,nombre])
            
    if check:
        print(tabulate(table, headers, tablefmt="simple"))
        print('Hubo ',cantidad,' personas en el camino')
        print('El requerimiento duró:',time)
        
    else:
        print('No se encontraron relaciones')


def print_req_3(control,Id):
    max,max_amigo,time=logic.req_3(control,Id)
    print('El amigo fue:',max_amigo)
    print('Sus seguidores son: ', max)
    print('El requerimiento duró: ', time)


def print_req_4(control, ID_A, ID_B):
def print_req_4(control, ID_A, ID_B):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    ac, time = logic.req_4(control,ID_A,ID_B)
    
    headers = ['ID', 'Nombre', 'Tipo de usuario']
    table = []
    check = True
    
    if len(ac)  == 0:
        check = False
    else:
        for i in ac:
            id = i['USER_ID']
            Nombre = i['USER_NAME']
            Tipo = i['USER_TYPE']
            
            table.append([id,Nombre,Tipo])
    
    if check:
        print(tabulate(table, headers, tablefmt="simple"))
        print('El requerimiento duró:',time)
    else:
        print('No se necontraron amigos en común\n')


def print_req_5(control, Id, N):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    list, time = logic.req_5(control,Id,N)
    
    headers = ['ID','Nombre']
    table = []
    check = True
    
    if list == None:
        check = False
    else:
        for i in list:
            Id = i
            info = gr.get_vertex_information(control,Id)
            nombre = info['USER_NAME']
            table.append([Id,nombre])
            
    if check:
        print(tabulate(table, headers, tablefmt="simple"))
        print('El requerimiento duró:',time)
    else:
        print('No se encontraron relaciones')


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            
        elif int(inputs) == 2:
            id_1 = input('\nCuenta origen: ')
            id_2 = input('\nCuenta destino: ')
            print_req_1(data,int(id_1),int(id_2))

        elif int(inputs) == 3:
            Id_1=int(input('Id del usuario A '))
            Id_2=int(input('Id del usuario B '))
            print_req_2(control,Id_1,Id_2)

        elif int(inputs) == 4:
            Id=int(input('Id del usuario: '))
            print_req_3(control,Id)
            Id=int(input('Id del usuario: '))
            print_req_3(control,Id)

        elif int(inputs) == 5:
            ida = int(input('ID del usuario A: '))
            idb = int(input('ID del usuario B: '))
            print_req_4(control,ida,idb)
            ida = int(input('ID del usuario A: '))
            idb = int(input('ID del usuario B: '))
            print_req_4(control,ida,idb)

        elif int(inputs) == 6:
            N = int(input('Numero de amigos a consultar: '))
            Id = int(input('Id a consultar: '))
            print_req_5(control,Id,N)
            N = int(input('Numero de amigos a consultar: '))
            Id = int(input('Id a consultar: '))
            print_req_5(control,Id,N)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
