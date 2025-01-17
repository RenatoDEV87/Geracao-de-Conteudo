# Dicionário associando características aos modelos Claude 3 da Anthropic
caracteristicas_modelos = {
  "automatizar tarefas": "Claude 3 Opus",

  "pesquisa e desenvolvimento": "Claude 3 Opus",

  "resposta rápida e capacidade de resposta quase instantânea": "Claude 3 Haiku",

  "motores de chatbots de lojas": "Claude 3 Haiku",

  "moderação de conteúdo": "Claude 3 Haiku",

  "processamento de tarefas mais básicas": "Claude 3 Haiku",

  "raciocínio cuidadoso": "Claude 3 Sonnet",

  "processamento de dados": "Claude 3 Sonnet",

  "aplicações de vendas": "Claude 3 Sonnet",

  "extração de texto de imagens": "Claude 3 Sonnet",

  "equilíbrio ideal entre inteligência e velocidade": "Claude 3 Sonnet",

}

def encontrar_modelo(caracteristica_fornecida):

  modelo_contagem = {}

  for caracteristica, modelo in caracteristicas_modelos.items():

    if caracteristica in caracteristica_fornecida.lower():

      modelo_contagem[modelo] = modelo_contagem.get(modelo, 0) + 1

  if modelo_contagem:

    # Retorna o modelo com a maior contagem de correspondências

    return max(modelo_contagem, key=modelo_contagem.get)

  return "Modelo não encontrado."

# Entrada do usuário
caracteristica_fornecida = input()

# Encontrar e imprimir o modelo correspondente
modelo_correspondente = encontrar_modelo(caracteristica_fornecida)

print(modelo_correspondente)
