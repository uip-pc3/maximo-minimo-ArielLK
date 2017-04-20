"""
Modulo MAXMIN

permite el analisis o procesado de dos valores el cual serán analizados para determinar cual es el mayor
de ambos valores

"""

# Variables globales que seran como contadores de las llamadas que seran usados dentro de cada funciones
maxCalled = 0
minCalled = 0


def max_val(a: int, b: int):
    """
    Funcion que obtendra 2 argumentos ( numeros ) que seran analizados para determinar el mayor de ambos valores
    
    function(a, b) -> a>b or b>a
    
    :param a: Argumento que será el primer valor númerico.
    :param b: Argumento que sera el segundo valor númerico.
    :return: Devolvera el valor númerico que sea mayor entre ambos valores numericos analizados.
    .. warning:: Estos argumentos deben ser unicamente valores númericos
    """
    global maxCalled
    maxCalled = maxCalled + 1

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


def min_val(a: int, b: int):
    """
    Esta funcion obtendrá 2 argumentos ( números ) que seran analizados para determinar el menor de ambos valores
    
    function(a, b) -> a>b or b>a
    
    :param a: Argumento que será el primer valor númerico.
    :param b: Argumento que será el segundo valor númerico.
    :return: Devolverá el valor númerico que sea el menor entre ambos valores númericos analizados.
    .. warning:: Estos argumentos deben ser unicamente valores númericos
    """
    global minCalled
    minCalled = minCalled + 1

    if a < b:
        return a
    elif b < a:
        return b
    else:
        return a


def print_usage(init_msg, max_val=True, min_val=True):
    """
    Funcion que permite mostrar un mensaje junto a los resultados de valores
    :param init_msg: Obtendra el mensaje a mostrar
    :param max_val: Mostrará el valor maximo
    :param min_val: Mostrará el valor minimo
    :return: 
    """
    global maxCalled, minCalled
    print(init_msg)
    if max_val:
        print('functin max_val was called', maxCalled, ' times')
    if min_val:
        print('function min_val was called', minCalled, ' times')


if __name__ == '__main__':
    print('Calling function max_val')
    # Llamada a la funcion de Valor Maximo
    max_val(1, 4)
    max_val(2, b=1)
    max_val(b=4, a=3)

    print('Calling function min_val')
    # Llamada a lfuncion de Valor minimo
    min_val(1, 4)
    min_val(2, 4)
    min_val(4, b=9)
    # Imprime el mensaje inicial de la funcion PRINT USAGE junto a los valores maximos y minimo
    print_usage('The usage of functions min_val and max_val')
