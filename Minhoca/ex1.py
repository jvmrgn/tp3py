def formatar_nome_completo(nome_completo: str) -> str:
    """
    Formata um nome completo, deixando cada palavra com a inicial em maiúscula 
    e o restante das letras em minúsculas.

    param nome_completo: O nome fornecido pelo usuário
    return O nome formatado com a inicial de cada palavra em maiúscula
    """
    return nome_completo.title()

def solicitar_nome_completo() -> str:
    """
    Solicita um nome ao usuário e retorna o nome formatado.
    Garante que o nome seja uma string válida.

    return: O nome completo formatado
    """
    while True:
        nome = input("Digite seu nome completo: ").strip()
        if nome.replace(" ", "").isalpha():
            return formatar_nome_completo(nome)
        else:
            print("Entrada inválida. Digite apenas letras e espaços.")

print(solicitar_nome_completo())
