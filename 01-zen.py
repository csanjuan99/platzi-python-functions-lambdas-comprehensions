# El zen de python es la filosofia con la
# que creamos instrucciones en este codigo

import this

print(this)  # Imprime el zen de python

""" Bonito es mejor que feo. """
# ejemplo de codigo feo
gatos = 4;
perros = 6;
patas = 34;
assert patas == (gatos * perros * 4), 'Número de patas dispar';

# ejemplo de codigo bonito
gatos = 4
perros = 6
patas = 34
assert patas == (gatos * 4) + (perros * 4), 'Número de patas dispar'

""" Explícito es mejor que implícito. """


# version implicita
def metros_a_pulgadas_dobles(metros):
    return metros * 39.3701 * 2


# version explicita
def metros_a_pulgadas_dobles(metros):
    pulgadas_por_metro = 39.3701
    multi_doble = 2
    return metros * pulgadas_por_metro * multi_doble


""" Simple es mejor que complejo """
""" 
Un sistema complejo se define como un sistema
compuesto de muchas partes independientes conectadas entre sí,
pero que no tienen relaciones ocultas entre los componentes.

Si el sistema está correctamente implementado, 
cada parte independiente será simple si se estudia 
de forma aislada, por lo que, el estudio del sistema 
completo se podría simplificar en el estudio de cada parte simple.
"""

""" Complejo es mejor que complicado """
# version compleja interconectada
LIMITE_SUPERIOR = 32
LIMITE_INFERIOR = 3
POSICION = 1


def evaluar_cambio(valor):
    prev_pos = POSICION
    if valor > (LIMITE_SUPERIOR + LIMITE_INFERIOR * 5 / 4):
        nueva_pos = 1
    elif valor < (LIMITE_INFERIOR + LIMITE_INFERIOR * 2 / 4):
        nueva_pos = 0
    return prev_pos != nueva_pos


# version simple
def evaluar_cambio(valor, valor_actual):
    debe_cambiar = False
    if valor_actual == 1:
        debe_cambiar = debe_apagar(valor)
    elif valor_actual == 0:
        debe_cambiar = debe_encender(valor)
    return debe_cambiar


def debe_encender(valor, valor_superior=LIMITE_SUPERIOR, valor_inferior=LIMITE_INFERIOR):
    limite = valor_superior + valor_inferior * 5 / 4
    return valor > limite


def debe_apagar(valor, valor_superior=LIMITE_SUPERIOR, valor_inferior=LIMITE_INFERIOR):
    limite = valor_superior + valor_inferior * 2 / 4
    return valor < limite


""" Plano es mejor que anidado """
# version anidada
valores_ajustados = []
for s in sistemas:
    sensores = sensores_sistema(s)
    for sensor in sensores:
        valores_s = valores_sensor(sensor)
        for val in valores_s:
            valores_ajustados.append(ajustar_valor(val))

# version aplanada pero densa
valores_ajustados = [ajustar_valor(val) for val in valores_sensor(sensor) for sensor in sensores_sistema(s) for s in
                     sistemas]


# version en funciones simples, testeables y escalables
def valores_del_sistema_ajustados(sistemas):
    for sistema in sistemas:
        yield valores_sistema(sistema)


def valores_sistema(sistema):
    for sensores in sistema:
        yield valores_sensores(sensores)


def valores_sensores(sensores):
    for sensor in sensores:
        yield valores_sensor_ajustados(sensor)


def valores_sensor_ajustados(sensor):
    for valor in valores_sensores(sensor):
        yield ajustar_valor(valor)


""" Espaciado es mejor que denso """
# version densa
print(','.join(map(str, [x ** 2 for x in range(5)])))

# version dispersa
a = [x ** 2 for x in range(5)]
b = map(str, a)
c = ','.join(b)
print(c)

""" La legibilidad cuenta """
# version mas legible
lista_de_cuadrados = [x ** 2 for x in range(5)]
cadenas_de_cuadrados = map(str, lista_de_cuadrados)
cuadrados_formateados = ','.join(cadenas_de_cuadrados)
print(cuadrados_formateados)

""" Los errores nunca deberían pasar silenciosamente """
try:
    codigo_erroneo()
except Exception:
   pass

""" A menos que se silencien explícitamente """
try:
    codigo_erroneo()
except ValueError:
    logger.debug('Error de valor')