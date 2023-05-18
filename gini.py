# Programa simples para calcular o coeficiente de Gini de um nparray
# Me inspirei neste git https://github.com/oliviaguest/gini/blob/master/gini.py mas otimizei o código
import numpy as np
def gini(nparray):

    # Redimensionando nparray para garantir que ele é unidimensional
    nparray = nparray.flatten()

    # Garantindo que não tenhamos nenhum valor negativo ou igual a zero (para evitar ZeroDivisionErrors)
    nparray = nparray.clip(10**-10)

    # Ordenando 
    nparray = np.sort(nparray)

    # Obtendo os valores que vamos precisar para calcular o coeficiente de Gini
    index = np.arange(1, nparray.shape[0]+1)
    n = nparray.shape[0]

    # Cálculo
    return ((np.sum((2 * index - n  - 1) * nparray)) / (n * np.sum(nparray)))




