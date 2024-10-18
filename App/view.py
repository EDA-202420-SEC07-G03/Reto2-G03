import sys
from App import logic as logic
from itertools import islice
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
import time


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
    print("Se han cargado " + str(total_movies2) + " películas en la tabla 2.")
    print("Las primeras 5 peliculas son: ")
    print(control['movies']['elements'][0:5])
    print("Las últimas 5 películas son: ")
    print(control['movies']['elements'][-5:])
    
    

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    id = input("Ingrese el ID de la película que desea consultar: ")
    rta = logic.get_data(control,id)
    print("La pelicula correspondiente es: ")
    print(rta)

def print_req_1(control, idioma, movie_title):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    resultado = logic.req_1(control, idioma, movie_title)
    
    if isinstance(resultado, dict):
        print("\nInformacion de la pelicula encontrada: ")
        for key, value in resultado.items():
            print(f"{key}: {value}")
    else:
        print(resultado)

def print_req_2(control, n , idioma):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    if not n.isnumeric() or int(n) <= 0:
        print("Ingrese el numero de peliculas a listar")
        return

    n = int(n)

    resultado = logic.req_2(control, n, idioma)

    total_movies = resultado['total_movies']
    print(f"\nEl total de películas publicadas en '{idioma}' es de: {total_movies}")

    if total_movies > 0:
        print("\nÚltimas películas publicadas: ")
        for movie in resultado['movies']:
            print(f"Fecha de publicación: {movie['release_date']}")
            print(f"Título original: {movie['original_title']}")
            print(f"Presupuesto: {movie['budget']}")
            print(f"Ingresos: {movie['revenue']}")
            print(f"Ganancia: {movie['profit']}")
            print(f"Duración: {movie['runtime']} minutos")
            print(f"Puntaje de calificación: {movie['vote_average']}")
    else:
        print("No hay películas que cumplan estos requisitos.")

def print_req_3(sol):
    lista=list(sol.items())
    if sol["total"]>=10:
        for i in range(0,11):
            print(lista[i][1])
    else:
        for i in range(0,len(lista)):
            print(lista[i][1])

    print(" el total de peliculas es " + str(sol["total"]))
    print(" el tiempo  promedio de las peliculas es " + str(sol["tiempo_prom"]))

def print_req_4(control, estado, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    resultado = logic.req_4(control, estado, fecha_inicial, fecha_final)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"El total de peliculas encontradas: {resultado['total_peliculas']}")
        print(f"Tiempo promedio de duracion: {resultado['tiempo_promedio_duracion']:.2f} minutos")
        
        print("\nPelículas encontradas en orden cronológico de publicación:")
        for movie in resultado['peliculas']:
            print(f"Fecha de publicación: {movie['release_date']}")
            print(f"Título original: {movie['original_title']}")
            print(f"Presupuesto: {movie['budget']}")
            print(f"Recaudación: {movie['revenue']}")
            print(f"Ganancia: {movie['profit']}")
            print(f"Duración: {movie['runtime']} minutos")
            print(f"Puntaje de calificación: {movie['vote_average']}")
            print(f"Idioma original: {movie['original_language']}")
            print("-" * 40)

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    rango_presupuesto = input("Ingrese el rango de presupuesto que desea consultar: ")
    fecha_inicial = input("Ingrese la fecha inicial (formato YYYY-MM-DD): ") 
    fecha_final = input("Ingrese la fecha inicial (formato YYYY-MM-DD): ")
    rta = logic.req_5(control,rango_presupuesto,fecha_inicial,fecha_final)
    print("La cantidad de peliculas que cumplen el criterio de busqueda son " + str(rta['size']))
    divisor = 0
    presupuesto = 0
    for elemento in rta['elements']:
        presupuesto += int(elemento['budget'])
        divisor += 1
    presupuesto_prom = presupuesto/divisor
    print("El presupuesto promedio de las películas es de: " + str(round(presupuesto_prom,3)))
    
    if rta["size"] > 20:
        print("Las primeras 10 peliculas son: ")
        print(rta["elements"][0:10])
    else:
        print(rta)
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    idioma = input("Ingrese el idioma que desea consultar: ")
    año_inicial = input("Ingrese el año inicial: ") 
    año_final = input("Ingrese el año: ")
    rta = logic.req_6(control,idioma,año_inicial,año_final)
    print(rta)
    


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
            idioma = input('Ingrese el idioma que quiere buscar: ')
            movie_title = input('Ingrese la pelicula que quiere ver: ')
            print_req_1(control, idioma, movie_title)

        elif int(inputs) == 3:
            n = input('Ingrese el total de peliculas que quiere a listar: ')
            idioma = input('Ingrese el idioma que quiere buscar: ')
            print_req_2(control, n, idioma)

        elif int(inputs) == 4:
            fecha_inf=input("Ingrese el limite inferior de fecha: ")
            fecha_sup=input("Ingrese el limite superior de fecha: ")
            idioma= input("Ingrese el idioma de la pelicula: ")
            init_time = logic.get_time()
            sol=logic.req_3(control,idioma,fecha_inf,fecha_sup)
            fisin_time = logic.get_time()
            print(logic.delta_time(init_time, fisin_time))
            print_req_3(sol)
            

        elif int(inputs) == 5:
            estado = input('Ingrese el estado de la pelicula (“Released”, “Rumored”, etc): ')
            fecha_inicial = input('Ingrese la fecha inicial del periodo a consultar (en formato YYYY-MM-DD): ')
            fecha_final = input('Ingrese la fecha final del periodo a consultar (en formato YYYY-MM-DD): ')
            print_req_4(control, estado, fecha_inicial, fecha_final)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            fecha_inf=float(input("ingrese el limite inferior del rango de años: "))
            fecha_sup=float(input("ingrese el limite superior del rango de años: "))
            productora= input("ingrese la productora de la pelicula: ")
            init_time = logic.get_time()
            sol=logic.req_7(control,productora,fecha_inf,fecha_sup)
            fisin_time = logic.get_time()
            print(logic.delta_time(init_time, fisin_time))
            print_req_7(sol)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
