import random
import math
from collections import Counter
class Pessoa:
  def __init__ (self, idade, sexo, salario, intencao_de_voto):
    self.idade = idade
    self.sexo = sexo
    self.salario = salario
    self.intencao_de_voto = intencao_de_voto
  def __str__ (self):
    return f'idade: {self.idade}, sexo: {self.sexo}, salario: {self.salario}, intencao_de_voto: {self.intencao_de_voto}'
  def __eq__ (self, other):
    return self.intencao_de_voto == other.intencao_de_voto
  def __hash__ (self):
    return 1

def gera_base (n):
  lista = []
  for i in range(n):
    idade = random.randint(18, 35)
    sexo = random.choice(['M', 'F'])
    salario = 1200 + random.random() * 1300
    intencao_de_voto = random.choice(['Haddad', 'Bolsonaro'])
    p = Pessoa (idade, sexo, salario, intencao_de_voto)
    lista.append(p)
  return lista

def rotulo_de_maior_frequencia (pessoas):
    #lista = [1, 2, 1, 4, 5, 1, 2, 2, 2, 5, 3]
    #Counter(lista) = {1: 3, 2: 4, 4: 1, 5: 2, 3: 1}
    frequencias = Counter(pessoas)
    mais_frequentes = frequencias.most_common(1)
    return mais_frequentes[0][0]

def rotulo_de_maior_frequencia_sem_empate(pessoas):
  frequencias = Counter(pessoas)
  rotulo, frequencia = frequencias.most_common(1)[0]
  qtde_de_mais_frequentes = len ([count for count in frequencias.values() if count == frequencia])
  if qtde_de_mais_frequentes == 1:
    return rotulo
  return rotulo_de_maior_frequencia_sem_empate(pessoas[:-1])

def distancia(p1, p2):
  i = math.pow(p1.idade - p2.idade, 2)
  s = math.pow( (1 if p1.sexo == 'M' else 0) - (1 if p2.sexo == 'M' else 0) , 2)
  sal = math.pow(p1.salario - p2.salario , 2)
  return math.sqrt(i + s + sal)

def knn (k, observacoes_rotuladas, nova_observacao):
  ordenados_por_distancia = sorted(observacoes_rotuladas, key=lambda obs: distancia(obs, nova_observacao))
  k_mais_proximos = ordenados_por_distancia[:k]
  resultado = rotulo_de_maior_frequencia_sem_empate(k_mais_proximos)
  return resultado.intencao_de_voto


def main():
  base = gera_base(10)
  for p in base:
    print (p)
  print (knn(3, base, Pessoa(19, 'F', 3500, None)))
  # base = gera_base(10)
  # print (rotulo_de_maior_frequencia_sem_empate(base))

main()


 