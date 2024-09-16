import re
from collections import Counter

def extrair_clausulas_valores(texto):
    """
    Extrai cláusulas que mencionam valores monetários do texto do contrato.
    
    Parâmetros:
    texto (str): O texto completo do contrato.
    
    Retorno:
    list: Lista de cláusulas contendo valores monetários.
    """
    padrao_valor = r'\b(?:R\$|US\$|\$|€|£)?[\d,.]+(?:[\s]*[A-Za-z]*)\b'
    
    clausulas = re.split(r'\.\s*|\n+', texto)
    
    clausulas_com_valores = [clausula.strip() for clausula in clausulas if re.search(padrao_valor, clausula)]
    
    return clausulas_com_valores

def contar_termos_legais(texto, termos_legais):
    """
    Conta quantas vezes cada termo legal aparece no texto e exibe as ocorrências em ordem decrescente de frequência.
    
    Parâmetros:
    texto (str): O texto completo do contrato.
    termos_legais (list): Lista de termos legais para contar.
    
    Retorno:
    dict: Dicionário com termos e suas frequências, ordenado em ordem decrescente.
    """
    texto_lower = texto.lower()
    
    contagem_termos = Counter()
    for termo in termos_legais:
        contagem_termos[termo] = texto_lower.count(termo.lower())
    
    termos_ordenados = dict(sorted(contagem_termos.items(), key=lambda item: item[1], reverse=True))
    
    return termos_ordenados

texto_contrato = """
Este contrato é celebrado entre as partes A e B. A parte A pagará R$5000,00 pela prestação de serviços. 
O pagamento será feito em duas parcelas de R$2500,00 cada. Além disso, as partes concordam com os termos 
de confidencialidade e não competição. A parte B receberá um adicional de US$1000 por desempenho excelente.
"""

termos_legais = ['confidencialidade', 'não competição', 'pagamento', 'parcelas', 'adicional']

clausulas_com_valores = extrair_clausulas_valores(texto_contrato)
print("Cláusulas com valores monetários:")
for clausula in clausulas_com_valores:
    print(clausula)

frequencia_termos = contar_termos_legais(texto_contrato, termos_legais)
print("\nFrequência dos termos legais:")
for termo, frequencia in frequencia_termos.items():
    print(f"{termo}: {frequencia}")
