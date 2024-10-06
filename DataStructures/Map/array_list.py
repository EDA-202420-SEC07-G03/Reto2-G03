from DataStructures.Utils import error as error
def cmp_fnc(a,b):
    if a ==b:
        return 0

def new_list():
    """Crea una lista implementada con un Array List vacío. 

        Define una lista vacía y con un tamaño de cero

        :returns: Lista creada
        :rtype: array_list
    """
    newlist = {
        'elements': [],
        'size': 0,
    }

    # raise error.FunctionNotImplemented("new_list()")
    return newlist


def add_first(my_list, element):
    """Agrega un elemento al ArryList en la primera posición.

        Al agregar un elemento en la primera posición de la lista, se incrementa el tamaño de la lista en uno.

        :param my_list: ArrayList en la que se va a insertar el elemento
        :type my_list: array_list
        :param element: Elemento a insertar
        :type element: any

        :returns: ArrayList con el elemento insertado en la primera posición
        :rtype: array_list
    """

    try:
        my_list['elements'].insert(0, element)
        my_list['size'] += 1
        # raise error.FunctionNotImplemented("add_first()")
    except Exception as exp:
        error.reraise(exp, 'arraylist->addFirst: ')


def add_last(my_list, element):
    """ Agrega un elemento en la última posición de la lista.

        Al agregar un elemento en la última posición de la lista y se incrementa el tamaño de la lista en uno.

        :param my_list: ArrayList en la que se va a insertar el elemento
        :type my_list: array_list
        :param element: Elemento a insertar
        :type element: any

        :returns: ArrayList con el elemento insertado en la última posición
        :rtype: array_list
    """
    try:
        my_list['elements'].append(element)
        my_list['size'] += 1
        # raise error.FunctionNotImplemented("add_last()")
    except Exception as exp:
        error.reraise(exp, 'arraylist->addLast: ')


def is_empty(my_list):
    """ Indica si la lista está vacía

        :param my_list: Lista a examinar
        :type my_list: array_list

        :returns: ``True`` si la lista está vacía, ``False`` en caso contrario
        :rtype: bool
    """
    try:
        # raise error.FunctionNotImplemented("is_empty()")
        return my_list['size'] == 0
    except Exception as exp:
        error.reraise(exp, 'arraylist->isEmpty: ')


def size(my_list):
    """ Retorna el número de elementos de la lista.

        :param my_list: La lista a examinar
        :type my_list: array_list

        :returns: Número de elementos de la lista
        :rtype: int
    """
    try:
        # raise error.FunctionNotImplemented("size()")
        return my_list['size']
    except Exception as exp:
        error.reraise(exp, 'arraylist->size: ')


def first_element(my_list):
    """ Retorna el primer elemento de una lista no vacía.
        Esta funcion NO elimina el elemento de la lista.

        :param my_list: La lista a examinar
        :type my_list: array_list

        :returns: Primer elemento de la lista
        :rtype: any
    """
    try:
        # raise error.FunctionNotImplemented("first_element()")
        return my_list['elements'][0]
    except Exception as exp:
        error.reraise(exp, 'arraylist->firstElement: ')


def last_element(my_list):
    """ Retorna el último elemento de una  lista no vacía.
        Esta funcion NO elimina el elemento de la lista.

        :param my_list: La lista a examinar
        :type my_list: array_list

        :returns: Último elemento de la lista
        :rtype: any
    """
    try:
        # raise error.FunctionNotImplemented("last_element()")
        return my_list['elements'][my_list['size']-1]
    except Exception as exp:
        error.reraise(exp, 'arraylist->lastElement: ')


def get_element(my_list, pos):
    """ Retorna el elemento en la posición ``pos`` de la lista.

        Se recorre la lista hasta el elemento ``pos``, el cual debe ser igual o mayor
        que cero y menor al tamaño de la lista.
        Se retorna el elemento en dicha posición sin eliminarlo.
        La lista no puede ser vacía.

        :param my_list: La lista a examinar
        :type my_list: array_list
        :param pos: Posición del elemento a retornar
        :type pos: int

        :returns: Elemento en la posición ``pos``
        :rtype: any
    """

    try:
        # raise error.FunctionNotImplemented("get_element()")
        return my_list["elements"][pos]
    except Exception as exp:
        error.reraise(exp, 'arraylist->getElement: ')


def delete_element(my_list, pos):
    """ Elimina el elemento en la posición ``pos`` de la lista.

        Elimina el elemento que se encuentra en la posición ``pos`` de la lista.
        ``Pos`` debe ser igual o mayor que cero y menor al tamaño de la lista.
        Se decrementa en un uno el tamaño de la lista.
        La lista no puede estar vacía.

        :param my_list: La lista a examinar
        :type my_list: array_list
        :param pos: Posición del elemento a eliminar
        :type pos: int

        :returns: Lista con el elemento eliminado
        :rtype: array_list
    """
    try:
        # raise error.FunctionNotImplemented("delete_element()")
        my_list['elements'].pop(pos-1)
        my_list['size'] -= 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->deleteElement: ')


def remove_first(my_list):
    """ Remueve el primer elemento de la lista.

        Elimina y retorna el primer elemento de la lista.
        El tamaño de la lista se decrementa en uno.  Si la lista
        es vacía se retorna ``None``.

        :param my_list: La lista a examinar
        :type my_list: array_list

        :returns: Primer elemento de la lista
        :rtype: any
    """
    try:
        # raise error.FunctionNotImplemented("remove_first()")
        element = my_list['elements'].pop(0)
        my_list['size'] -= 1
        return element
    except Exception as exp:
        error.reraise(exp, 'arraylist->removeFirst: ')


def remove_last(my_list):
    """ Remueve el último elemento de la lista.

        Elimina el último elemento de la lista  y lo retorna en caso de existir.
        El tamaño de la lista se decrementa en 1.
        Si la lista es vacía retorna ``None``.

        :param my_list: La lista a examinar
        :type my_list: array_list

        :returns: Último elemento de la lista
        :rtype: any
    """
    try:
        # raise error.FunctionNotImplemented("remove_last()")
        element = my_list['elements'].pop(my_list['size']-1)
        my_list['size'] -= 1
        return element
    except Exception as exp:
        error.reraise(exp, 'arraylist->removeLast: ')


def insert_element(my_list, element, pos):
    """ Inserta el elemento element en la posición ``pos`` de la lista.

        Inserta el elemento en la posición ``pos`` de la lista.
        La lista puede ser vacía.
        Se incrementa en 1 el tamaño de la lista.

        :param my_list: La lista en la que se va a insertar el elemento
        :type my_list: array_list
        :param element: El elemento a insertar
        :type element: any
        :param pos: posición en la que se va a insertar el elemento
        :type pos: int

        :returns: Lista con el elemento insertado
        :rtype: array_list
    """
    try:
        # raise error.FunctionNotImplemented("insert_element()")
        my_list['elements'].insert(pos-1, element)
        my_list['size'] += 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->insertElement: ')


def is_present(my_list, element, cmp_function=cmp_fnc):
    """ Informa si el elemento element esta presente en la lista.

        Informa si un elemento está en la lista.
        Si esta presente, retorna la posición en la que se encuentra
        o menos uno (-1) si no esta presente. Se utiliza la función de comparación
        pasada por parámetro para comparar los elementos,
        la cual debe retornan cero si los elementos son iguales.

        :param my_list: La lista a examinar
        :type my_list: array_list
        :param element: El elemento a buscar
        :type element: any
        :param cmp_function: Función de comparación de elementos
        :type cmp_function: function

        :returns: Posición del elemento en la lista
        :rtype: int
    """
    # raise error.FunctionNotImplemented("is_present()")
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if (cmp_function(element, info) == 0):
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def change_info(my_list, pos, new_info):
    """ Cambia la información contenida en el nodo de la lista
        que se encuentra en la posición ``pos``.

        :param my_list: La lista a examinar
        :type my_list: array_list
        :param pos: posición de la lista con la información a cambiar
        :type pos: int
        :param new_info: Nueva información que se debe poner en el nodo de la posición ``pos``
        :type new_info: any

        :returns: Lista con la información cambiada
        :rtype: array_list
    """
    try:
        # raise error.FunctionNotImplemented("change_info()")
        my_list['elements'][pos-1] = new_info
    except Exception as exp:
        error.reraise(exp, 'arraylist->changeInfo: ')


def exchange(my_list, pos1, pos2):
    """ Intercambia la información en las posiciones ``pos1`` y ``pos2`` de la lista.

        :param my_list: La lista a examinar
        :type my_list: array_list
        :param pos1: Posición del primer elemento
        :type pos1: int
        :param pos2: Posición del segundo elemento
        :type pos2: int

        :returns: Lista con la información intercambiada
        :rtype: array_list
    """
    try:
        # raise error.FunctionNotImplemented("exchange()")
        infopos1 = get_element(my_list, pos1)
        infopos2 = get_element(my_list, pos2)
        change_info(my_list, pos1, infopos2)
        change_info(my_list, pos2, infopos1)
        return my_list
    except Exception as exp:
        error.reraise(exp, 'arraylist->exchange: ')


def sub_list(my_list, pos, num_elem):
    """ Retorna una sub-lista de la lista recibida.

        Retorna una lista que contiene los elementos a partir de la posición ``pos``,
        con una longitud de ``num_elem`` elementos.
        Se crea una copia de dichos elementos y se retorna una lista nueva.

        :param my_list: La lista origen
        :type my_list: single_linked_list
        :param pos: Posición del primer elemento
        :type pos: int
        :param num_elem: Posición del segundo elemento
        :type pos: int

        :returns: Sub-lista de la lista original
        :rtype: single_linked_list
    """
    try:
        # raise error.FunctionNotImplemented("sublist()")
        sublst = {'elements': [],
                  'size': 0,
                  'type': 'ARRAY_LIST'}
        elem = pos-1
        cont = 1
        while cont <= num_elem:
            sublst['elements'].append(my_list['elements'][elem])
            sublst['size'] += 1
            elem += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'arraylist->subList: ')


def compare_elements(my_list, element, info, cmp_function):
    """ Compara el elemento ``element`` de la lista ``my_list`` con el elemento ``info``.

        Se utiliza la función de comparación por defecto si key es None o la función provista por el usuario en caso contrario

        :param my_list: La lista con los elementos
        :type my_list: array_list
        :param element: El elemento que se está buscando en la lista
        :type element: any
        :param info: El elemento de la lista que se está analizando\
        :type info: any
        :param cmp_function: Función de comparación de elementos
        :type cmp_function: function

        :returns: 0 si los elementos son iguales, 1 si element > info, -1 si element < info
        :rtype: array_list
    """
    # raise error.FunctionNotImplemented("compare_elements()")
    if (my_list['key'] is not None):
        return cmp_function(element[my_list['key']], info[my_list['key']])
    else:
        return cmp_function(element, info)


def default_function(id1, id2):
    """ Función de comparación por defecto

        Compara dos elementos

        :param id1: Identificador 1
        :type id1: any
        :param id2: Identificador 2
        :type id2: any

        :retuns: 0 si los elementos son iguales, 1 si id1 > id2, -1 si id1 < id2
        :rtype: int
    """
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0


def selection_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list
    elements = my_list["elements"]
     
    for n in range(len(elements)):
        
        selected_index = n
        
        for i in range(n + 1, len(elements)):
            
            if sort_crit(elements[i], elements[selected_index]):
                selected_index = i
        
        if selected_index != n:
            elements[n], elements[selected_index] = elements[selected_index], elements[n]

    return my_list



def merge_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list

    elements = my_list["elements"]

    def merge(left, right):
        result = []
        i = j = 0

        # Usar sort_crit para determinar el tipo de orden
        while i < len(left) and j < len(right):
            if sort_crit(left[i], right[j]):  # Cambiado para usar sort_crit
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(elements) // 2
    left_half = {"size": mid, "elements": elements[:mid]}
    right_half = {"size": len(elements) - mid, "elements": elements[mid:]}

    sorted_left = merge_sort(left_half, sort_crit)
    sorted_right = merge_sort(right_half, sort_crit)

    my_list["elements"] = merge(sorted_left["elements"], sorted_right["elements"])
    my_list["size"] = len(my_list["elements"])

    return my_list