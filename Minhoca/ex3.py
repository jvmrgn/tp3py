def encontrar_palavra_mais_longa(texto: str) -> str:
    """
    Encontra e retorna a palavra mais longa em um texto, ignorando pontuação.

    param texto: O texto fornecido pelo usuário
    return: A palavra mais longa no texto
    """
    palavras = texto.split()
    palavra_mais_longa = max(palavras, key=len)
    return palavra_mais_longa

def solicitar_texto_para_palavra_mais_longa() -> str:
    """
    Solicita um texto ao usuário e retorna a palavra mais longa em uma frase formatada.

    return: A frase indicando qual é a palavra mais longa
    """
    texto = input("Digite um texto: ").strip()
    palavra_mais_longa = encontrar_palavra_mais_longa(texto)
    return f"A palavra mais longa é: {palavra_mais_longa}"

print(solicitar_texto_para_palavra_mais_longa())
