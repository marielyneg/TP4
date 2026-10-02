import matplotlib.pyplot as plt
class Noeud:
    """
    C'est PGM de marielyng.
    Cette classe "Noeud" incule fonctions ceux-dessous:
    "ajouter_un_enfant"
    "afficher"
    "evaluer"
    "tracer
    """
    def __init__(self,valeur):
        self.valeur=valeur
        self.enfants=[]
    def ajouter_un_enfant(self,noeud):
        self.enfants.append(noeud)
    def afficher(self):
        print(self.valeur, end=" ")

        for enfant in self.enfants:
            enfant.afficher()
    def evaluer(self, dico):

     if isinstance(self.valeur, (int, float)):
        return self.valeur

  
     if len(self.enfants) == 0:
        if self.valeur in dico:
            return dico[self.valeur]
        else:
            raise ValueError("Variable manquante")

  
     a = self.enfants[0].evaluer(dico)
     b = self.enfants[1].evaluer(dico)

     if self.valeur == "+":
        return a + b

     if self.valeur == "-":
        return a - b

     if self.valeur == "*":
        return a * b
        
    def tracer(self, variable, valeurs):
     resultats = []

     for valeur in valeurs:
        resultat = self.evaluer({variable: valeur})
        resultats.append(resultat)

     plt.plot(valeurs, resultats)
     plt.show()