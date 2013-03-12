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
      mutacao.append(self.apagar.__name__)
    elif (r == 4):
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.transferir.__name__)
      mutacao.append(self.apagar.__name__)
      mutacao.append(self.hospedar.__name__)
    elif (r == 5):
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.executar.__name__)
      mutacao.append(self.transferir.__name__)
      mutacao.append(self.apagar.__name__)
    elif (r == 6):
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.apagar.__name__)
    elif (r == 7):
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.apagar.__name__)
    elif (r == 8):
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.apagar.__name__)
    elif (r == 9):
      mutacao.append(self.atacar.__name__)
      mutacao.append(self.copiar.__name__)
      mutacao.append(self.hospedar.__name__)
      mutacao.append(self.propagar.__name__)
    return mutacao

  def apagar(self):
    # print 'apagar'
    #return True
    return random.randint(0,1)

  def copiar(self):
    # print 'copiar'
    #return True
    return random.randint(0,1)

  def transferir(self):
    # print 'copiar'
    #return True
    return random.randint(0,1)

  def atacar(self):
    # print 'atacar'
    #return False
    return random.randint(0,1)     

  def hospedar(self):
    # print 'hospedar'
    #return True
    return random.randint(0,1)
  
  def propagar(self):
    # print 'propagar'
    #return False
    return random.randint(0,1)    
    
  def desligar(self):
    # print 'desligar'
    #return False
    return random.randint(0,1)

  def executar(self):
    # print 'executar'
    #return False
    return random.randint(0,1)    
    
  def hibernar(self):
    # print 'hibernar'
    #return False
    return random.randint(0,1)    