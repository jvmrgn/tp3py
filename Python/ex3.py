import random
import string
import re

def gerar_senha(tamanho=12):
    """
    Gera uma senha aleatória segura com o comprimento especificado.

    Args:
        tamanho (int): O comprimento desejado da senha. Deve ser pelo menos 8.

    Returns:
        str: A senha gerada.

    Raises:
        ValueError: Se o tamanho for menor que 8.
    """
    if tamanho < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha

def verificar_senha(senha):
    """
    Verifica se a senha atende aos critérios de segurança.

    Args:
        senha (str): A senha a ser verificada.

    Returns:
        tuple: Um tuplo com dois elementos:
            - bool: Indica se a senha é válida.
            - str: Mensagem sobre a validade da senha.
    """
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    if not re.search(r'[A-Z]', senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search(r'[a-z]', senha):
        return False, "A senha deve conter pelo menos uma letra minúscula."

    if not re.search(r'[0-9]', senha):
        return False, "A senha deve conter pelo menos um número."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False, "A senha deve conter pelo menos um caractere especial."

    return True, "Senha válida."

def sugerir_senha():
    """
    Sugere uma nova senha gerada aleatoriamente.

    Returns:
        str: A senha sugerida.
    """
    return gerar_senha()

def cifra_substituicao(texto, deslocamento):
    """
    Criptografa o texto usando uma cifra de substituição com deslocamento.

    Args:
        texto (str): O texto a ser criptografado.
        deslocamento (int): O número de posições para deslocar os caracteres.

    Returns:
        str: O texto criptografado.
    """
    caracteres = string.printable
    tabela = str.maketrans(caracteres, caracteres[deslocamento:] + caracteres[:deslocamento])
    return texto.translate(tabela)

def descriptografar(texto, deslocamento):
    """
    Descriptografa o texto usando a cifra de substituição inversa.

    Args:
        texto (str): O texto criptografado.
        deslocamento (int): O número de posições para deslocar os caracteres na direção oposta.

    Returns:
        str: O texto descriptografado.
    """
    return cifra_substituicao(texto, -deslocamento)

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    print("\nMenu:")
    print("1. Gerar uma nova senha")
    print("2. Testar uma senha")
    print("3. Mostrar lista padrão de senhas")
    print("4. Sair")
    escolha = input("Escolha uma opção (1/2/3/4): ")
    return escolha

def main():
    """
    Função principal que executa o programa com base na escolha do usuário.
    """
    senhas_padrao = ["sEnha12345789!", "admin!2024pbTSajcxmz", "p@ssw0rdETC123PASS"]
    deslocamento = 4
    
    while True:
        escolha = exibir_menu()
        
        if escolha == "1":
            try:
                tamanho = int(input("Digite o tamanho da senha (mínimo 8): "))
                if tamanho < 8:
                    print("O tamanho da senha deve ser pelo menos 8 caracteres.")
                else:
                    senha_gerada = gerar_senha(tamanho)
                    print(f"Senha gerada: {senha_gerada}")
            except ValueError:
                print("Erro: O tamanho deve ser um número inteiro válido.")

        elif escolha == "2":
            senha = input("Digite a senha para testar: ")
            valido, mensagem = verificar_senha(senha)
            if not valido:
                print(mensagem)
                print("Sugestão de nova senha:", sugerir_senha())
            else:
                print(mensagem)

        elif escolha == "3":
            print("\nSenhas originais:")
            print(senhas_padrao)

            senhas_criptografadas = [cifra_substituicao(s, deslocamento) for s in senhas_padrao]
            print("Senhas criptografadas:", senhas_criptografadas)

            senhas_descriptografadas = [descriptografar(s, deslocamento) for s in senhas_criptografadas]
            print("Senhas descriptografadas:", senhas_descriptografadas)

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
