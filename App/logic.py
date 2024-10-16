import time
import csv
import json
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Map import map_functions as mf

csv.field_size_limit(2147483647)


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"movies":None,
               "ordenado_idioma":None,"ordenado_año":None,"ordenado_product":None}
    
    catalog["movies"] = lt.new_list()
    catalog["ordenado_idioma"] = mp.new_map(89,1)
    catalog["ordenado_año"]=mp.new_map(135,1)
    return catalog
 

# Funciones para la carga de datos
def fecha_str_a_fecha_dias(date):
    año=float(date[:4])
    mes=float(date[5:7])
    dias=float(date[8:])
    return (año*365)+(mes*30)+(dias)

def get_anio(date):
    return date[:4] 

def load_data(catalog, filename):
    movies = csv.DictReader(open(".\\Data\\Challenge-2\\"+filename, encoding='utf-8'))
    
    
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
            lt.add_last(k,genre)
        rta['genres'] = k
        
        production_companies_list = json.loads(elemento['production_companies'])
        x = lt.new_list()
        for production_companies in production_companies_list:
            lt.add_last(x,production_companies)
        
        rta['production_companies'] = x
        lt.add_last(catalog["movies"],rta)
        
        idioma = elemento['original_language']
        
        
        movies_in_language = mp.get(catalog['ordenado_idioma'], idioma)

        if movies_in_language is None:
            lista_peliculas = lt.new_list()
            lt.add_last(lista_peliculas, rta)
            mp.put(catalog['ordenado_idioma'], idioma, lista_peliculas)
        else: 
            lt.add_last(movies_in_language, rta)  
        
        año=get_anio(elemento["release_date"])
        movies_in_anio = mp.get(catalog['ordenado_año'], año)
        if movies_in_anio is None:
            lista_año = lt.new_list()
            lt.add_last(lista_año, rta)
            mp.put(catalog['ordenado_año'], año, lista_año)
        else: 
            lt.add_last(movies_in_anio, rta)
                       
    return catalog
        
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog, idioma, movie_title):
    """
    Retorna el resultado del requerimiento 1
    """
    entry = mp.get(catalog['ordenado_idioma'], idioma)
    
    if entry is None:
        return "Ninguna película fue encontrada"
    
    movies_in_language = entry['elements']
    
    for movie in movies_in_language:
        if movie['title'].lower() == movie_title.lower():
                       
            net_profit = None
            if float(movie["revenue"]) != 0 and float(movie["budget"]) != 0:
                net_profit = float(movie["revenue"]) - float(movie["budget"])
            
            respuesta = {
                "Título original": movie['title'],
                "Duración (minutos)": movie['runtime'],
                "Fecha de publicación": movie['release_date'],
                "Presupuesto": movie['budget'],
                "Dinero recaudado": movie['revenue'],
                "Ganancia": net_profit,
                "Puntaje de calificación": movie['vote_average'],
                "Idioma original": movie['original_language']
            }
            return respuesta

def req_2(catalog, n, idioma):
    """
    Retorna el resultado del requerimiento 2
    """

    movies_in_language_entry = mp.get(catalog['ordenado_idioma'], idioma)

    if movies_in_language_entry is None:
        return {
            "total_movies": 0,
            "movies": []
        }

    movie_list = movies_in_language_entry['elements']

    movie_list_released = [movie for movie in movie_list if movie['status'] == 'Released']
    total_movies = len(movie_list_released)
    
    if total_movies == 0:
        return {
            "total_movies": 0,
            "movies": []
        }
    lo = 0
    hi = total_movies - 1
    stack = [(lo, hi)]

    while stack:
        lo, hi = stack.pop()
        if lo < hi:
            pivot = movie_list_released[hi]
            i = lo - 1
            for j in range(lo, hi):
                if movie_list_released[j]['release_date'] > pivot['release_date']:
                    i += 1
                    movie_list_released[i], movie_list_released[j] = movie_list_released[j], movie_list_released[i]
            i += 1
            movie_list_released[i], movie_list_released[hi] = movie_list_released[hi], movie_list_released[i]
            stack.append((lo, i - 1))
            stack.append((i + 1, hi))
    n = min(n, total_movies)
    resultado = {
        "total_movies": total_movies,
        "movies": []
    }
    
    for i in range(n):
        movie = movie_list_released[i]   
        budget = movie['budget'] if movie['budget'] else "Undefined"
        revenue = movie['revenue'] if movie['revenue'] else "Undefined"
        profit = None
        if budget != "Undefined" and revenue != "Undefined":
            profit = float(revenue) - float(budget)
        
        resultado['movies'].append({
            "release_date": movie['release_date'],
            "original_title": movie['title'],
            "budget": movie['budget'],
            "revenue": movie['revenue'],
            "profit": profit,
            "runtime": movie['runtime'],
            "vote_average": movie['vote_average']
        })
    
    return resultado

def req_3(catalog,idioma,fecha_ini,fecha_final):
    lista=mp.get(catalog["ordenado_idioma"],idioma)
    
    fecha_i=fecha_str_a_fecha_dias(fecha_ini)
    fecha_f=fecha_str_a_fecha_dias(fecha_final)
    dic={}
    total=0
    tiempo_prom=0
    for j in range(0,lt.size(lista)):
        if fecha_str_a_fecha_dias(lista["elements"][j]["release_date"])>=fecha_i and fecha_str_a_fecha_dias(lista["elements"][j]["release_date"])<= fecha_f:
            total+=1
            tiempo_prom+=float(lista["elements"][j]["runtime"])
            if fecha_str_a_fecha_dias(lista["elements"][j]["release_date"]) not in dic:
                lista["elements"][j]["net_profit"]="undefined"
                if float(lista["elements"][j]["revenue"])!=0 and float(lista["elements"][j]["budget"])!=0:
                    lista["elements"][j]["net_profit"]=float(lista["elements"][j]["revenue"])-float(lista["elements"][j]["budget"])
                dic[fecha_str_a_fecha_dias(lista["elements"][j]["release_date"])]=lista["elements"][j]
    new_dic=dict(sorted(dic.items()))
    new_dic["total"]=total
    if total!=0:
     new_dic["tiempo_prom"]=tiempo_prom/total
    else:
        new_dic["tiempo_prom"]="no hay ninguna pelicula para promediar"
    return new_dic
    
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

def is_name_in_list(name, company_list):
    for company in company_list:
        if company['name'] == name:
            return True
    return False
def req_7(catalog,productora,inicial,final):

    """
    Retorna el resultado del requerimiento 7
    """
    estadistica={}
    for i in range(0,lt.size(catalog["movies"])):
        for j in range(0,lt.size(catalog["movies"]["elements"][i]["production_companies"])):
         if str(catalog["movies"]["elements"][i]["production_companies"]["elements"][j]["name"])==productora and int(catalog["movies"]["elements"][i]["release_date"][:4]) >= int(inicial) and int(catalog["movies"]["elements"][i]["release_date"][:4]) <= int(final): 
                     año = catalog["movies"]["elements"][i]["release_date"][:4]
                     if año not in estadistica:
                        estadistica[año] = {
                        'total': 0,'votacion_prom': 0,'duracion_prom': 0,'net_profit': 0,
                        'mejor_peli': ("", float("-inf")),'peor_peli': ("", float("inf"))}
                     estadistica[año]['total'] += 1
                     estadistica[año]['votacion_prom'] += float(catalog["movies"]["elements"][i]["vote_average"])
                     estadistica[año]['duracion_prom'] += float(catalog["movies"]["elements"][i]["runtime"])
                     if ((catalog["movies"]["elements"][i]["revenue"]) or(catalog["movies"]["elements"][i]["budget"]))=="0":
                      net_profit="undefined"
                     else:
                       net_profit=int(catalog["movies"]["elements"][i]["revenue"])-int(catalog["movies"]["elements"][i]["budget"])
                     if net_profit!="undefined":
                       estadistica[año]["net_profit"]+=net_profit
                     votacion = float(catalog["movies"]["elements"][i]['vote_average'])
                     nombre = catalog["movies"]["elements"][i]["title"]
                     if votacion > estadistica[año]['mejor_peli'][1]:
                       estadistica[año]['mejor_peli'] = (nombre, votacion)
                     if votacion < estadistica[año]['peor_peli'][1]:
                       estadistica[año]['peor_peli'] = (nombre, votacion)
    estadistica_final={}
    i=int(inicial)
    fini=int(final)
    while i < fini+1:
        if str(i) in estadistica:
          estadistica_final[str(i)] = {
                'total': estadistica[str(i)]["total"],
                'votacion_prom': estadistica[str(i)]["votacion_prom"] / estadistica[str(i)]["total"],
                'duracion_prom': estadistica[str(i)]["duracion_prom"] / estadistica[str(i)]["total"],
                'net_profit': estadistica[str(i)]["net_profit"],
                'mejor_peli': estadistica[str(i)]["mejor_peli"],
                'peor_peli': estadistica[str(i)]["peor_peli"]}
        i+=1
    return estadistica_final



 

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
