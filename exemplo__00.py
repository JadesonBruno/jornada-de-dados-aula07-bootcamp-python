# uma função simples de soma de valores do tipo float que retorna float
def soma(valor_1: float, valor_2: float) -> float:
    resultado_da_soma: float = valor_1 + valor_2
    return resultado_da_soma


valor_1 = 10
valor_2 = 15
valor_3 = 12.5
valor_4 = 15.6

resultado_1 = soma(valor_1=valor_1, valor_2=valor_2)
print(resultado_1)

resultado_2 = soma(valor_1=valor_3, valor_2=valor_4)
print(resultado_2)


# uma função simples de multiplicação com valor padrão
def multiplicacao(valor_1: float, valor_2: float = 10) -> float:
    resultado_da_multiplicacao: float = valor_1 * valor_2
    return resultado_da_multiplicacao


valor_1 = 10
valor_2 = 15
valor_3 = 12.5
valor_4 = 15.6

resultado_3 = multiplicacao(valor_1=valor_1, valor_2=valor_2)
print(resultado_3)

resultado_4 = multiplicacao(valor_1=valor_3, valor_2=valor_4)
print(resultado_4)

resultado_5 = multiplicacao(valor_1=valor_1)
print(resultado_5)
