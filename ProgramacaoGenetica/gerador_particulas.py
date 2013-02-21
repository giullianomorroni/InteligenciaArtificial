# -*- coding: utf-8 -*-

from Tvirus import comando

genetica = [];

c = comando();
ap = c.apagar();
cp = c.copiar();
at = c.atacar();

if(ap and cp and at):
   genetica.append(c.apagar.__name__)
elif(ap and cp):
   genetica.append(c.apagar.__name__)
elif(ap):
   genetica.append(c.apagar.__name__)

for g in genetica:
  func = getattr(c, g)
  func()