def numero_por_extenso(numero: int) -> str:
    """
    Converte um número inteiro (até 31) para sua forma textual em português. Utilizei IA para gerar os números por extenso

    :param numero: O número a ser convertido (1 a 31 para dias)
    :return: O número por extenso
    """
    numeros = [
        "", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
        "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte",
        "vinte e um", "vinte e dois", "vinte e três", "vinte e quatro", "vinte e cinco", "vinte e seis", 
        "vinte e sete", "vinte e oito", "vinte e nove", "trinta", "trinta e um"
    ]
    return numeros[numero]

def mes_por_extenso(mes: int) -> str:
    """
    Converte o número de um mês para sua forma textual em português. 

    :param mes: O número do mês (1 a 12)
    :return: O nome do mês por extenso
    """
    meses = [
        "", "janeiro", "fevereiro", "março", "abril", "maio", "junho", 
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return meses[mes]

def ano_por_extenso(ano: int) -> str:
    """
    Converte um ano para sua forma textual em português. Utilizei IA para gerar os números por extenso

    :param ano: O número do ano (ex: 2024)
    :return: O ano por extenso
    """
    unidades = [
        "", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"
    ]
    dezenas = [
        "", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"
    ]
    centenas = [
        "", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"
    ]
    milhares = [
        "", "mil", "dois mil", "três mil", "quatro mil", "cinco mil", "seis mil", "sete mil", "oito mil", "nove mil"
    ]
    
    milhar = ano // 1000
    centena = (ano % 1000) // 100
    dezena = (ano % 100) // 10
    unidade = ano % 10
    
    if centena == 1 and dezena == 0 and unidade == 0:
        centena_extenso = "cem"
    else:
        centena_extenso = centenas[centena]
    
    dezena_extenso = dezenas[dezena]
    unidade_extenso = unidades[unidade]
    
    if dezena == 1:
        teens = [
            "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"
        ]
        return f"{milhares[milhar]} e {centena_extenso} e {teens[unidade]}".replace(" e ", " ").strip()

    if unidade_extenso:
        return f"{milhares[milhar]} {centena_extenso} {dezena_extenso} e {unidade_extenso}".replace("  ", " ").strip()
    return f"{milhares[milhar]} {centena_extenso} {dezena_extenso}".replace("  ", " ").strip()

def converter_data_para_texto(data: str) -> str:
    """
    Converte uma data no formato "dd/mm/aaaa" para sua forma textual.

    :param data: A data no formato "dd/mm/aaaa"
    :return: A data por extenso em texto
    """
    try:
        dia, mes, ano = map(int, data.split('/'))
        
        dia_extenso = numero_por_extenso(dia)
        mes_extenso = mes_por_extenso(mes)
        ano_extenso = ano_por_extenso(ano)
        
        return f"{dia_extenso.capitalize()} de {mes_extenso} de {ano_extenso}"
    except ValueError:
        return "Data inválida. Use o formato dd/mm/aaaa."

while True:
    data = input("Digite uma data no formato dd/mm/aaaa: ").strip()
    
    if len(data) == 10 and data[2] == '/' and data[5] == '/':
        resultado = converter_data_para_texto(data)
        if resultado.startswith("Data inválida"):
            print(resultado)
        else:
            print(f"Data por extenso: {resultado}")
            break
    else:
        print("Formato de data incorreto. Tente novamente.")