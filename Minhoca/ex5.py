def soma_dos_digitos(numeros: str) -> int:
    """
    Calcula a soma dos dígitos em uma string numérica.

    param numeros: Uma string contendo apenas dígitos
    return: A soma dos dígitos
    """
    return sum(int(digito) for digito in numeros)

def solicitar_string_numerica() -> int:
    """
    Solicita uma string numérica ao usuário e retorna a soma dos dígitos.

    return: A soma dos dígitos
    """
    while True:
        string_numerica = input("Digite uma string numérica: ").strip()
        if string_numerica.isdigit():
            return soma_dos_digitos(string_numerica)
        else:
            print("Entrada inválida. Certifique-se de que o valor contém apenas dígitos.")

print(f"Soma dos dígitos: {solicitar_string_numerica()}")
