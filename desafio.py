# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

def recomendar_plano(consumo):
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
  if consumo <= 10.0:
    return "Plano Essencial Fibra - 50Mbps"
  elif 10.0 < consumo < 20.0:
    return "Plano Prata Fibra - 100Mbps"
  else:
    return "Plano Premium Fibra - 300Mbps"

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))