def contar_caracteres_palavras_espacos(frase: str) -> dict:
    """
    Conta o número de caracteres, palavras e espaços em branco em uma frase.

    param frase: A frase fornecida pelo usuário
    return: Um dicionário com as contagens de caracteres, palavras e espaços
    """
    num_caracteres = len(frase)
    num_palavras = len(frase.split())
    num_espacos = frase.count(' ')
    return {"caracteres": num_caracteres, "palavras": num_palavras, "espacos": num_espacos}

def solicitar_frase_para_contagem() -> dict:
    """
    Solicita uma frase ao usuário e retorna as contagens de caracteres, palavras e espaços.

    return: Um dicionário com as contagens
    """
    frase = input("Digite uma frase: ").strip()
    return contar_caracteres_palavras_espacos(frase)

contagem = solicitar_frase_para_contagem()
print(f"Caracteres: {contagem['caracteres']}, Palavras: {contagem['palavras']}, Espaços: {contagem['espacos']}")
