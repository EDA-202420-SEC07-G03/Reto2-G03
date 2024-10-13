import sys
from App import logic as logic
from itertools import islice
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control
 
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

def load_data(control):
    """
    Carga los datos
    """
    filename = input("Ingrese el nombre del archivo (con el .csv): ")
    movies = logic.load_data(control,filename)
    total_movies = 0
    total_no =0
    for i in range(0, movies['ordenado_idioma']['capacity']):
        entry = movies['ordenado_idioma']['table']['elements'][i]
        
        if entry['key'] is not None:  
            total_movies += lt.size(entry['value']) 
            total_no+=1 
    total_movies2 = 0
    total_años =0
    for i in range(0, movies['ordenado_año']['capacity']):
        entry = movies['ordenado_año']['table']['elements'][i]
        
        if entry['key'] is not None:  
            total_movies2 += lt.size(entry['value']) 
            total_años+=1 
    

    
    print("Se han cargado " + str(movies['movies']['size']) + " películas en la lista.")
    print("Se han cargado " + str(total_movies) + " películas en la tabla.")
    print(lt.size(movies['ordenado_idioma']["table"]))
    print(str(total_no))
    print("Se han cargado " + str(total_movies2) + " películas en la tabla 2.")
    print(lt.size(movies['ordenado_año']["table"]))
    print(str(total_años))
    
    list=[]
    for i in range(0,lt.size(movies["movies"])):
       if movies["movies"]["elements"][i]["release_date"][:4] not in list:
           list.append(movies["movies"]["elements"][i]["release_date"][:4])
    print(len(list))
    """"
    d=[]
    for i in range(0,lt.size(movies["movies"])):
       for j in range(0,lt.size(movies["movies"]["elements"][i]["production_companies"])):
        if movies["movies"]["elements"][i]["production_companies"]["elements"][j]["name"] not in d:
           d.append(movies["movies"]["elements"][i]["production_companies"]["elements"][j]["name"])
    print(len(d))
    """




def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(sol):
    print(sol)
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
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            fecha_inf=float(input("ingrese el limite inferior del rango de años: "))
            fecha_sup=float(input("ingrese el limite superior del rango de años: "))
            productora= input("ingrese la productora de la pelicula: ")
            sol=logic.req_7(control,productora,fecha_inf,fecha_sup)
            print_req_7(sol)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
