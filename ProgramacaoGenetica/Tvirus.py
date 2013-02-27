# -*- coding: utf-8 -*-

import random
import time

class comando():

  '''
  Gera mutações diferentes do mesmo vírus, baseado em uma função randômica.
  '''
  def mutacao(self):
    time.sleep(1);
    r = random.randint(0,10)
    mutacao = []
    if (r == 0):
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.apagar.__name__)
    elif (r == 1):
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.apagar.__name__)
    elif (r == 2):
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.apagar.__name__)
    elif (r == 3):
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.propagar.__name__)
    elif (r == 4):
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.transferir.__name__)
      mutacao.append(self.apagar.__name__)
      mutacao.append(self.hospedar.__name__)
    elif (r == 5):
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.executar.__name__)
      mutacao.append(self.transferir.__name__)
      mutacao.append(self.apagar.__name__)
    else:
      #continuar até o 10...
      mutacao.append(self.desligar.__name__)
    return mutacao

  def apagar(self):
    # print 'apagar'
    return True

  def copiar(self):
    # print 'copiar'
    return True

  def transferir(self):
    # print 'copiar'
    return True
    
  def atacar(self):
    # print 'atacar'
    return False

  def hospedar(self):
    # print 'hospedar'
    return True

  def propagar(self):
    # print 'propagar'
    return False
    
  def desligar(self):
    # print 'desligar'
    return False
    
  def executar(self):
    # print 'executar'
    return False
    
  def hibernar(self):
    # print 'hibernar'
    return False      