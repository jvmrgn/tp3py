import re

def realizar_operacao(operador, operando1, operando2):
    """
    Realiza a operação entre dois operandos com base no operador fornecido.

    :param operador: O operador matemático (+, -, *, /)
    :param operando1: O primeiro número
    :param operando2: O segundo número
    :return: O resultado da operação
    """
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        if operando2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return operando1 / operando2

def calcular_expressao_sem_espacos(expressao):
    """
    Calcula o resultado de uma expressão matemática básica (sem espaços) em string.

    :param expressao: A expressão matemática sem espaços
    :return: O resultado da expressão
    """
    numeros = re.findall(r'\d+\.?\d*', expressao)
    operadores = re.findall(r'[+\-*/]', expressao)
    
    numeros = list(map(float, numeros))

    i = 0
    while i < len(operadores):
        if operadores[i] in '*/':
            resultado = realizar_operacao(operadores[i], numeros[i], numeros[i + 1])
            numeros[i] = resultado
            del numeros[i + 1]
            del operadores[i]
        else:
            i += 1

    i = 0
    while i < len(operadores):
        resultado = realizar_operacao(operadores[i], numeros[i], numeros[i + 1])
        numeros[i] = resultado
        del numeros[i + 1]
        del operadores[i]

    return numeros[0]

def calcular_expressao(expressao: str) -> float:
    """
    Calcula o resultado de uma expressão matemática básica fornecida pelo usuário,
    ignorando espaços e verificando se há caracteres inválidos.

    :param expressao: A expressão matemática fornecida como string
    :return: O resultado da expressão ou None se houver erro
    """
    expressao = expressao.replace(" ", "")

    if re.match(r'^[\d+\-*/.]+$', expressao):
        try:
            return calcular_expressao_sem_espacos(expressao)
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
        except Exception as e:
            print(f"Erro: Expressão inválida ({str(e)}).")
    else:
        print("Erro: A expressão contém caracteres inválidos.")
    return None

def solicitar_expressao() -> float:
    """
    Solicita uma expressão matemática ao usuário e retorna o resultado após validação.

    :return: O resultado da expressão calculada ou uma mensagem de erro
    """
    while True:
        expressao = input("Digite uma expressão matemática: ").strip()
        resultado = calcular_expressao(expressao)
        if resultado is not None:
            return resultado

resultado_final = solicitar_expressao()
print(f"Resultado: {resultado_final}")
