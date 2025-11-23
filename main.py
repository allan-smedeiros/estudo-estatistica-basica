import dataset as ds
import formulas as fm
import numpy as np


dataset = ds.criar_dataset()
media, mediana, desvio, val_max, val_min = fm.calcula_estatistica(dataset)

colunas = ["Visitas", "Tempo no Site", "Itens no carrinho", "Valor da compra"]
print("----Análise Estatística Geral----")
for i,nome in enumerate(colunas):
  #função enumerate irá retornar uma lista com o índice + elemento do iterável.
  print(f"\n{nome}")
  print(f"Média: {media[i]:.2f}")
  print(f"Mediana: {mediana[i]:.2f}")
  print(f"Desvio Padrão: {desvio[i]:.2f}")
  print(f"Valor máximo: {val_max[i]:.2f}")
  print(f"Valor mínimo: {val_min[i]:.2f}")

media_valor, mediana_valor, desvio_valor, *_ = fm.calcula_estatistica(dataset[:,3])

fm.criar_histograma(dataset[:,3], media_valor, mediana_valor, desvio_valor, "Valor de Compra")