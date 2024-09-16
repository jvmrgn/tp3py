from collections import defaultdict

def calcular_valores_vendas(transacoes):
    """
    Calcula e exibe o valor total das vendas para cada produto.
    
    Parâmetros:
    transacoes (list): Lista de transações, onde cada transação é uma string no formato 
                       "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário".
    
    Retorno:
    dict: Dicionário com o nome do produto como chave e o valor total das vendas como valor.
    """
    valores_totais = defaultdict(float)
    quantidades_totais = defaultdict(int)
    
    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_unitario = transacao.split(',')
        quantidade = int(quantidade)
        valor_unitario = float(valor_unitario)
        
        total_venda = quantidade * valor_unitario
        valores_totais[nome_produto] += total_venda
        quantidades_totais[nome_produto] += quantidade
    
    print("Valor total das vendas para cada produto:")
    for produto, total in valores_totais.items():
        print(f"{produto}: R$ {total:.2f}")
    
    return valores_totais, quantidades_totais

def produtos_destaque(valores_totais, quantidades_totais):
    """
    Encontra o produto mais vendido e o produto que gerou a maior receita total.
    
    Parâmetros:
    valores_totais (dict): Dicionário com o nome do produto e o valor total das vendas.
    quantidades_totais (dict): Dicionário com o nome do produto e a quantidade total vendida.
    
    Retorno:
    tuple: Tupla com o produto mais vendido e o produto que gerou a maior receita total.
    """
    produto_mais_vendido = max(quantidades_totais, key=quantidades_totais.get)
    produto_maior_receita = max(valores_totais, key=valores_totais.get)
    
    return produto_mais_vendido, produto_maior_receita

def converter_moeda(valores_totais, fator_conversao):
    """
    Converte os valores totais de vendas para uma nova moeda.
    
    Parâmetros:
    valores_totais (dict): Dicionário com o nome do produto e o valor total das vendas.
    fator_conversao (float): Fator de conversão para a nova moeda.
    
    Retorno:
    dict: Dicionário com o nome do produto e o valor total convertido.
    """
    valores_convertidos = {produto: total * fator_conversao for produto, total in valores_totais.items()}
    
    print("\nValores convertidos para a nova moeda:")
    for produto, valor in valores_convertidos.items():
        print(f"{produto}: R$ {valor:.2f}")
    
    return valores_convertidos

transacoes = [
    "1,Produto A,10,15.00",
    "2,Produto B,5,20.00",
    "1,Produto A,2,15.00",
    "3,Produto C,8,10.00",
    "2,Produto B,3,20.00"
]

valores_totais, quantidades_totais = calcular_valores_vendas(transacoes)
produto_mais_vendido, produto_maior_receita = produtos_destaque(valores_totais, quantidades_totais)

print(f"\nProduto mais vendido: {produto_mais_vendido}")
print(f"Produto que gerou a maior receita total: {produto_maior_receita}")

fator_conversao = float(input("\nDigite o fator de conversão para a nova moeda: "))
valores_convertidos = converter_moeda(valores_totais, fator_conversao)
