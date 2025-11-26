import dataset as ds
import formulas as fm
import numpy as np

#Objetivo: Descobrir qual a quantidade média de visitas no site, qual o tempo de navegação e o valor da compra (ticket médio) feitos no site de e-commerce dentro de 1 mês.

dataset = ds.criar_dataset()
media, mediana, desvio, val_max, val_min = fm.calcula_estatistica(dataset)

colunas = ["Visitas", "Tempo no Site", "Itens no carrinho", "Valor da compra"]
print("----Análise Estatística Geral----")
for i,nome in enumerate(colunas):
  #função enumerate irá retornar uma tupla (índice,elemento) do iterável.
  print(f"\n{nome}")
  print(f"Média: {media[i]:.2f}")
  print(f"Mediana: {mediana[i]:.2f}")
  print(f"Desvio Padrão: {desvio[i]:.2f}")
  print(f"Valor máximo: {val_max[i]:.2f}")
  print(f"Valor mínimo: {val_min[i]:.2f}")

media_valor, mediana_valor, desvio_valor, *_ = fm.calcula_estatistica(dataset[:,3])

fm.criar_histograma(dataset[:,3], media_valor, mediana_valor, desvio_valor, "Valor de Compra")

#-------------RESULTADO-------------
'''
1. Usuário acessa em média 26 vezes por mês e permanece navegando pelo site por em média 33 minutos;
2. O ticketi médio é de aproximadamente R$252,70, ficando próximo da mediana R$248,13;
3. É possível observar que 68% dos valores de compra estão concentrados entre R$145,76 e R$359,13.
'''