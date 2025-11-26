import numpy as np
import matplotlib.pyplot as plt

def calcula_estatistica(dados):
  '''Calcula estatísticas básicas de um array NumPy.
  Parâmetros
  dados: array (vetor 1D ou matriz 2D contendo valores numéricos).
  Retorna
  tupla: (media, mediana, desvio_padrao, valor_maximo, valor_minimo)'''
  
  dados = np.array(dados)
  if dados.ndim == 2:
      # Para matrizes, calcular estatísticas por coluna (axis=0)
      media   = np.mean(dados, axis=0)
      mediana = np.median(dados, axis=0)
      desvio  = np.std(dados, axis=0)
      val_max = np.max(dados, axis=0)
      val_min = np.min(dados, axis=0)
  elif dados.ndim == 1:
      # Para vetores
      media   = np.mean(dados)
      mediana = np.median(dados)
      desvio  = np.std(dados)
      val_max = np.max(dados)
      val_min = np.min(dados)
  else:
      raise ValueError("A função aceita apenas arrays unidimensionais (1D) ou bidimensionais (2D).")
  return media, mediana, desvio, val_max, val_min


def criar_histograma(array, media, mediana, desvio, nome_col="Dados"):
  '''Cria um histograma com marcações da média, mediana e ±1 desvio-padrão.
  Parâmetros:
  array: Conjunto de dados utilizado no histograma.
  media: Valor da média do conjunto de dados.
  mediana: Valor da mediana do conjunto de dados.
  desvio: Desvio-padrão do conjunto de dados.
  nome_col: Nome exibido no título e rótulos do gráfico.'''

  plt.figure(figsize=(12, 5)) #Definindo o tamanho da área do gráfico.
  plt.hist(                   #Cria um histograma
      array, 
      bins=30,                #Intervalo utilizado para agrupar valores
      color="skyblue",        #Cor do preenchimento das barras
      edgecolor="black",      #Cor das boras das barras
      alpha=0.7               #Transparência das barras sendo 1 = opaco, 0 = transparente.
  )
  
  plt.axvline(                          #Desenha uma linha vertical no gráfico
      media,                            #Posição do eixo X
      color="red",                      #Cor da linha
      linestyle="--",                   #Estilo da linha (podendo ser "--", ":", "-")
      linewidth=2,                      #Espessura da linha
      label=f"Média = R${media:.2f}"    #Legenda que descreve a linha
  )
  plt.axvline(mediana, color="orange", linestyle="--", linewidth=2, label=f"Mediana = R${mediana:.2f}")
  plt.axvline(media + desvio, color="green", linestyle=":", linewidth=2,label=f"+1 DP = R${media + desvio:.2f}")
  plt.axvline(media - desvio, color="green", linestyle=":", linewidth=2,label=f"-1 DP = R${media - desvio:.2f}")

  plt.title(f"Distribuição de {nome_col}")  #Título do gráfico
  plt.xlabel(f"{nome_col}")                 #Rótulo do eixo X
  plt.ylabel("Frequência")                  #Rótulo do eixo Y
  plt.legend()                              #Habilita o quadro de legenda no gráfico
  plt.grid(alpha=0.3)                       #Habilita linhas de grade no fundo do gráfico (quanto menor o alpha, mais transparente)
  plt.show()