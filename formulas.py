import numpy as np
import matplotlib.pyplot as plt


def calcula_estatistica(dados):
  #essa função irá calcular a estatística geral de um array de elementos declarado como argumento.
  dados = np.array(dados)
  if dados.ndim == 2:
    media = np.mean(dados, axis=0) #necessário colocar axis=0 para indicar que eu quero o cálculo por COLUNA, e o retorno desta função irá me trazer um array contendo os valores de cada coluna.
    mediana = np.median(dados, axis=0)
    desvio = np.std(dados, axis=0)
    val_max = np.max(dados, axis=0)
    val_min = np.min(dados, axis=0)
  elif dados.ndim == 1: 
    media = np.mean(dados) 
    mediana = np.median(dados)
    desvio = np.std(dados)
    val_max = np.max(dados)
    val_min = np.min(dados)
  else:
    print("A função aceita somente arrays vetores ou matrizes.")
  return media, mediana, desvio, val_max, val_min

def criar_histograma(array, media, mediana, desvio, nome_col):
  plt.figure(figsize=(12,5)) #estou definindo o tamanho da área do gráfico larguraXaltura
  plt.hist(array, bins=30, color="skyblue", edgecolor="black", alpha=0.7)
  #array = conjunto de dados, bins intervalo utilizado para agrupar valores (pode deixar "auto"), color é a cor do preenchimento das barras, edgecolor é a cor das bordas das barras, alpha é a transparência das barras sendo (1=opaco, 0=totalmente transparente)
  plt.axvline(media, color="red", linestyle="--",linewidth=2, label= f"Média = R${media:.2f}")
  #axvline desenha uma linha vertigal no gráfico, x/media é a posição no eixo X, color cor da linha, linestyle é o estilo da linha ("--", ":", "-"), linewidth é a espessura da linha, label é o texto para legenda que descreve a linha.
  plt.axvline(media, color="orange", linestyle="--", linewidth=2, label=f"Mediana = R${mediana:.2f}")
  plt.axvline(media + desvio, color="green", linestyle=":", linewidth=2, label= f"+1 DP = R${media+desvio:.2f}")
  plt.axvline(media - desvio, color="green", linestyle=":", linewidth=2, label= f"-1 DP = R${media-desvio:.2f}")
  plt.title(f"Distribuição de {nome_col}")
  plt.xlabel(f"Dados: {nome_col}") #define rótulo do eixo X
  plt.ylabel("Frequência") #define o rótulo do eixo Y
  plt.legend() #habilita a legenda do gráfico, que descreve as linhas ou elementos com labels.
  plt.grid(alpha=0.3) 
  #adiciona uma grade de linhas no fundo do gráfico para facilitar a leitura. Alpha define a transparência das linhas de grade (quanto menos, mais transparente)
  plt.show()

