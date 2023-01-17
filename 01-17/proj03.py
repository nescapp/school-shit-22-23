"""
Objectif
Créer une calculatrice résolvant des calculs arithmétiques sur les fractions.

Consignes
 Écrire une classe Fraction qui permet d’effectuer les calculs
arithmétiques sur les fractions suivantes :
Formules :

Calculer à l'aide de la méthode ajouter.

Calculer à l'aide de la méthode soustraire.

Calculer à l'aide de la méthode multiplier.

Calculer à l'aide de la méthode diviser.

Calculer à l'aide de la méthode opposer.

 Cette classe devra avoir deux attributs :
 num : numérateur de la fraction
 den : dénominateur de la fraction.

2
 Implémenter la classe Fraction en considérant les méthodes suivantes :
 un constructeur qui initialise par défaut les attributs num et den a` la
valeur 1;

 les getters et les setters nécessaires.

 les méthodes assurant les opérations arithmétiques : ajouter, soustraire,
multiplier, diviser et opposer.
Attention, les résultats des calculs doivent être simplifiés (indication : utiliser
la méthode reduire).
De plus chacune de ces méthodes doit retourner une fraction.
À titre d'exemple, voici l'algorithme de la méthode ajouter :
- On déclare une fraction z (initialisée par défaut);
- On calcule le numérateur et le dénominateur de z par la formule
mathématique;
- On réduit la fraction z;
- On retourne z.

 une méthode réduire permettant de réduire une fraction donnée.
Par exemple, la fraction 6/8 sera réduite à la fraction 3/4.

Cette méthode devra utiliser une fonction nommée pgcd calculant le plus
grand commun diviseur entre deux entiers a et b.

Voici le code de cette fonction :
def pgcd(a, b):
if a < 0:
return pgcd(-a, b)
if a == 0:
return b
if b < a:
return pgcd(b, a)
return pgcd(b % a, a)

3

 une méthode d'affichage qui affiche de manière explicite.

 une méthode __str__ assurant l'affichage d'une fraction sous la
forme a/b.
Attention, si le dénominateur de la fraction est égal à 1, on
affiche simplement la valeur du numérateur (comme étant un
simple entier).
 Écrire une fonction unite (en dehors de la classe) qui prend
comme argument une liste de fractions et qui retourne la valeur
True si et seulement si la somme de toutes les fractions est
égale à 1.
 Commenter le code de manière explicite.
"""

from fractions import Fraction

def pgcd(a, b):
    """fonction calculant le plus grand commun diviseur entre deux entiers a et b"""
    pgcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            pgcd = i
    return pgcd

class Fraction():
    def __init__(self, num1=1, den1=1, num2=1, den2=1):
        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2
    def get_num1(self):
        return self.num1
    def get_den1(self):
        return self.den1
    def get_num2(self):
        return self.num2
    def get_den2(self):
        return self.den2
    def ajouter(self):
        return self.num1 * self.den2 + self.num2 * self.den1, self.den1 * self.den2
    def soustraire(self):
        return self.num1 * self.den2 - self.num2 * self.den1, self.den1 * self.den2
    def multiplier(self):
        return self.num1 * self.num2, self.den1 * self.den2
    def diviser(self):
        return self.num1 * self.den2, self.num2 * self.den1
    def opposer(self):
        return -self.num1, self.den1
    def reduire(a, b):
        return a / pgcd(a, b), b / pgcd(a, b)

    def __str__(self):
        return str(self.num1) + "/" + str(self.den1)

test = Fraction(2, 4, 1, 4)
print(test.ajouter())
print(test.soustraire()())
print(test.multiplier()())
print(test.diviser())
print(test.opposer())
# print(p1.get_num(), p1.get_den())
