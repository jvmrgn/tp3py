import re

def validar_cpf(cpf: str) -> str:
    """
    Valida e formata o CPF.
    
    Parâmetros:
    cpf (str): O CPF inserido pelo usuário.

    Retorno:
    str: CPF formatado como 'xxx.xxx.xxx-xx'.
    """
    cpf = re.sub(r'\D', '', cpf) 
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        return "CPF inválido. Deve conter 11 dígitos."

def validar_email(email: str) -> str:
    """
    Valida e formata o e-mail para minúsculas.
    
    Parâmetros:
    email (str): O e-mail inserido pelo usuário.

    Retorno:
    str: E-mail validado ou mensagem de erro.
    """
    email = email.strip().lower()
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$', email):
        return email
    else:
        return "E-mail inválido."

def validar_telefone(telefone: str) -> tuple:
    """
    Valida, formata e exibe o número de telefone.

    Parâmetros:
    telefone (str): O telefone inserido pelo usuário.

    Retorno:
    tuple: Número inteiro e string formatada ou mensagem de erro.
    """
    telefone = re.sub(r'\D', '', telefone)
    if len(telefone) == 10:
        telefone_formatado = f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
        return int(telefone), telefone_formatado
    elif len(telefone) == 11:
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        return int(telefone), telefone_formatado
    else:
        return "Telefone inválido."

def solicitar_dados():
    """
    Solicita CPF, e-mail e telefone do usuário, valida e formata cada um.
    Caso o dado seja inválido, pede novamente até ser válido.
    """
    while True:
        cpf = input("Digite o CPF: ")
        cpf_formatado = validar_cpf(cpf)
        if "inválido" not in cpf_formatado:
            print(f"CPF formatado: {cpf_formatado}")
            break
        else:
            print(cpf_formatado)
    
    while True:
        email = input("Digite o e-mail: ")
        email_validado = validar_email(email)
        if "inválido" not in email_validado:
            print(f"E-mail validado: {email_validado}")
            break
        else:
            print(email_validado)
    
    while True:
        telefone = input("Digite o telefone: ")
        telefone_validado = validar_telefone(telefone)
        if isinstance(telefone_validado, tuple):
            telefone_inteiro, telefone_formatado = telefone_validado
            print(f"Telefone (inteiro): {telefone_inteiro}")
            print(f"Telefone formatado: {telefone_formatado}")
            break
        else:
            print(telefone_validado)

solicitar_dados()
