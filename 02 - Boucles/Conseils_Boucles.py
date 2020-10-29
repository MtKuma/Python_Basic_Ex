""" 

la boucle for:
      a = 1

      for i in range(0, 3):
            print(a) 

      attention la nomenclature ici est importante a respecter !  (la nomenclature est l'espace crée avec tabulation juste apres le for, 
                                                                  cela indique à python que print est dans la boucle for)
      
      dans notre exemple, i vaux 0 et va jusque 3 à pas de 1      
      ici l'interet n'est pas flagrant, nous auriont pu faire quelque chose comme ca:


      a = 1

      for i in range(0, 3):
            print(a)
            a = a+1

la boucle while:
      la boucle while fera une action de magniere indéfinie..
      il y a donc un probleme -> la bonne facon de faire un while est de mettre une contrainte d'arret,

      voici un exemple de code sans contrainte pour te faire une idée:


      a = 1

      while True:
            print(a)
            a = a+1

      pour arreter une boucle infinie: CTRL + C

      nous pouvons donc faire une condition de plusieurs magniere, je vais donner deux exemple
      pour compter de 1 à 10 par exemple:

      premiere methode:
            a = 1

            while True:
                  print(a)
                  a = a+1
                  if a == 10+1:     # ici 10+1 car il va arreter a 10 et donc il ne va pas le renvoyer dans la console
                        break       # break va arreter la boucle

      deuxieme methode:
            a = 1

            while a < 10+1:   # si a est plus grand que 10+1 la boucle s'arrete
                  print(a)
                  a = a+1
"""


# Pour toute question vous pouvez m'envoyer un mail:  thibaut.fourneaux@outlook.com