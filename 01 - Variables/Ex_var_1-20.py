# Exemple d'exercice - Écrire un programme qui, à partir de la saisie d'un chiffre vous donnera le double.

""" 
chiffre = int(input('Veuillez entrer la valeur du rayon '))       #ici je précise int car je récupere la variable que l'utilisateur rentre, par defaut input est considéré comme du text
print(chiffre*2) 
"""


""" deuxiemme facon de résoudre

chiffre = int(input('Veuillez entrer la valeur du rayon '))
double = chiffre*2

print(double)
"""

# Exercice 01
# Créer un programme qui demande à l'utilisateur son prénom et qui salue en retour l'utilisateur (Bonjour ...)



# Exercice 02
# Créer un programme qui demande le prénom et le nom à l'utilisateur et les affiche en retour.



# Exercice 03
# Créer un programme qui demande à l'utilisateur "Comment vous sentez" et qui affiche en retour la phrase "Vous vous sentez : ..." (avec la réponse de l'utilisateur)



# Exercice 04
# Créer un programme qui demande à l'utilisateur comment il se sentait hier et comment il se sent aujourd'hui
# Afficher en retour dans la phrase "Hier, vous vous sentiez ... et aujourd'hui vous vous sentez ...



# Exercice 05
# Créer un programme qui combine les exercices 02 et 03



# Exercice 06
# Créer un programme qui demande deux nombres à l'utilisateur, qui stocke la somme dans une variable et affiche celle-ci.



# Exercice 07
# Créer un programme qui demande deux nombres à l'utilisateur et qui affiche :
# la somme de ces deux nombres
# la soustraction de ces deux nombres
# la multiplication de ces deux nombres
# la divsion de ces deux nombre.



# Exercice 08
# Créer un programme qui demande deux longueurs à l'utilisateur et afficher le périmètre avec une phrase "Le périmètre vaut ...".



# Exercice 09
# Créer un programme qui demande à l'utilisateur combien de fruits il veut acheter. Fixer le prix par unité et afficher la somme totale à payer.



# Exercice 10
# Créer un programme qui demande trois nombres à l'utilisateur et qui permutent ces nombres d'un rang vers la droite et les affiche.
# Ex : a = 5, b = 3, c = 8 => affiche a = 8, b = 5, c = 3



# Exercice 11
# Créer un programme qui demande le prix d'un article, le nombre d'articles achetés et la taux de TVA.
# Afficher le tout à l'utilisateur + le prix total HTVA + le prix total TVAC



# Exercice 12
# Créer un programme qui demande la somme d'argent que l'utilisateur possède.
# On demande ensuite à l'utilisateur quel objet il a acheté et le prix de celui-ci.
# Afficher à l'utilisateur "Après l'achat de "objet", il vous reste ... €"



# Exercice 13
# Créer un programme qui demande le diamètre d'un cercle à l'utilisateur.
# Afficher la circonférence du cercle => formule : circonférence = π x diamètre
# Dans python, il existe une bibliothèque avec des fonctions mathématiques déjà prévues et pouvant être utilisées.
# Pour cela il faut l'importer avant votre script : from math import *
# Et quand vous voulez utiliser par exemple ici, le π : inscrivez math.pi



# Exercice 14
# Créer un programme qui demande la circonférence d'un cercle à l'utilisateur.
# Afficher le rayon du cercle.



# Exercice 15
# Créer un programme qui convertit 203 secondes pour les afficher au format mm:ss dans le message : “203 secondes équivaut à mm:ss”.



# Exercice 16 
# Créer un programme qui demande le nom, le prénom, l'adresse de l'utilisateur.
# Afficher le prénom en premier avec une capitale à la première lettre, puis le nom tout en majuscul sur une première ligne.
# Afficher sur une deuxième ligne le code postal suivi de la ville tout en majuscule.

""" Exemple 
Fourneaux Thibaut
Rue sensure, 16
5000 Namur
"""

# Exercices sur les listes/dictionnaires :

# Exercice 17 
# Créer un programme qui créé une liste d’au moins 5 entiers puis successivement :
#   - afficher la valeur du 4e élément de votre liste
#   - modifier la liste en remplaçant le 2e élément par 17
#   - modifier la liste en remplaçant le 3e élément par la somme des cases voisines
#   - Ré-afficher la liste complète



# Exercice 18 
# Créer un programme qui échange les valeurs du premier et du dernier élément d’une liste quelconque non vide



# Exercice 19
# Voici une chaine de caractère de 10 noms : Marc, Mathieu, ANNE, Jeanne, Sylvain, simon, PIERRE, Hélène, sylvia, Michelle
# Transformer cette chaine en une liste
# Unifier l'affichage des noms pour avoir chaque nom qui débute par une capitale et le reste en miniscule, et afficher
# Compter combien de lettre e contient tous les noms et afficher ce nombre



# Exercice 20 
# Créer un dictionnaire avec les paires clés/valeurs suivantes :
# nom : Dupuis
# prenom : Jacque
# age : 30
# hobby : natation
# Ensuite, corriger l'erreur dans le prénom, la bonne valeur est 'Jacques'.
# Supprimez la clé hobby et sa valeur
# Ecrire la phrase "Jacques Dupuis a 30 ans" en utilisant votre dictionnaire


# Exercice bonus - Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.
# astuce : importer la bibliotheque math pour utiliser pi
