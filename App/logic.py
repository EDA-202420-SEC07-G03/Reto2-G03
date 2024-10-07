import time
import csv
import json
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = mp.new_map()
    
    return catalog
 

# Funciones para la carga de datos

def load_data(catalog, filename):
    movies = csv.DictReader(open(".\\Data\\Challenge-1\\"+filename, encoding='utf-8'))
    
    
    
    for elemento in movies:
        rta = {}
        rta['id'] = elemento['id']
        rta['title'] =  elemento['title']
        rta['original_language'] = elemento['original_language']
        rta['release_date'] = elemento['release_date']
        rta['revenue'] = elemento['revenue']
        rta['runtime'] = elemento['runtime']
        rta['status'] = elemento['status']
        rta['vote_average'] = elemento['vote_average']
        rta['vote_count'] = elemento['vote_count']
        rta['budget'] = elemento['budget']
        genres_list = json.loads(elemento['genres'].replace("'","\""))
        k=lt.new_list()
        for genre in genres_list: 
            lt.add_first(k,genre)
        rta['genres'] = k
        
        production_companies_list = json.loads(elemento['production_companies'])
        x = lt.new_list()
        for production_companies in production_companies_list:
            lt.add_first(x,production_companies)
        
        rta['production_companies'] = x
    
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
