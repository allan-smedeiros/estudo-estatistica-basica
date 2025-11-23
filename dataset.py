import numpy as np

def criar_dataset():
  #Para fixar a sequência e controlar todo o sistema aleatório do numpy:
  np.random.seed(42)

  '''
  visitas: número de vezes que o usuário visitou o site no mês
  tempo_no_site: tempo total em minutos que o usuário passou no site
  itens_carrinho: número de itens que o usuário adicionou ao carrinho
  valor_compra: valor total em R$ da compra realizada no mês
  '''

  #Para criar um dataset de 500 usuários:
  num_usuarios = 500

  #Gerando valores aleatórios, trazendo a quantidade de vezes que o usuário acessou o site.
  visitas = np.random.randint(1,51,num_usuarios)

  #Gerando valores dentro de uma distribuição normal, a fim de trazer dados ficticios próximos da "realidade"
  #Onde existe uma relação entre a quantidade de visitas e o tempo total navegando no site.
  tempo_no_site = np.random.normal(20,5,num_usuarios) + (visitas * 0.5)
  tempo_no_site = np.round(tempo_no_site,2)

  #Aqui estou gerando valores aleatórios, mas também sofrendo uma influência do número de visitas e do tempo gasto navegando no site.
  itens_carrinho = np.random.randint(0,8,num_usuarios) + (visitas // 10)
  itens_carrinho = (itens_carrinho + (tempo_no_site//15)).astype(int)

  #Para valor da compra, estou gerando um array com distribuição normal e coeeigindo possíveis valores negativos ou zerados.
  valor_compra = (itens_carrinho * 35) + np.random.normal(0,10,num_usuarios)
  valor_compra[itens_carrinho == 0] = 0 #Numpy permite utilizar condicionais dentro do índice, aplicando a operação apenas nos valores "True"
  valor_compra[valor_compra < 0] = 0
  valor_compra = np.round(valor_compra,2)

  #Nesta etapa será efetuado a junção de todos os arrays (mesmo tamanho), onde cada linha será os dados do usuário e cada coluna o atributo analisado.
  dados_ecommerce = np.column_stack((visitas, tempo_no_site, itens_carrinho, valor_compra))
  #Obs.: column_stack sempre espera uma lista/tupla de arrays como argumento.
  return dados_ecommerce

if __name__ == "__main__":
  dados = criar_dataset()
  print(dados)
  print(type(dados))