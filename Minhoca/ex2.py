def substituir_palavra(frase: str, palavra_antiga: str, palavra_nova: str) -> str:
    """
    Substitui todas as ocorrências de uma palavra específica por outra em uma frase.

    param frase: A frase original onde a palavra será substituída
    param palavra_antiga: A palavra a ser substituída
    param palavra_nova: A nova palavra que substituirá a antiga
    return A frase com as palavras substituídas
    """
    return frase.replace(palavra_antiga, palavra_nova)

def solicitar_frase_substituicao() -> str:
    """
    Solicita uma frase e duas palavras do usuário e retorna a frase 
    com a palavra substituída.

    return: A frase com a substituição aplicada
    """
    frase = input("Digite uma frase: ").strip()
    palavra_antiga = input("Digite a palavra que deseja substituir: ").strip()
    palavra_nova = input("Digite a nova palavra: ").strip()

    return substituir_palavra(frase, palavra_antiga, palavra_nova)

print(solicitar_frase_substituicao())
