

#programme de Marie Lyne
import matplotlib.pyplot as plt
class Noeud:
    """Represente un noeud du graphe"""
    def __init__(self,valeur):
        #j'ajoute pas des docstring(commentaires) dans le init
        self.valeur=valeur
        self.enfants=[]
    def ajouter_un_enfant(self,noeud):
        """Ajoute un noeud à la liste des enfants du noeud"""
        self.enfants.append(noeud)
    def afficher(self):
        """Affiche la valeur du noeud puis récursiveent ses enfants"""

        print(self.valeur, end=" ")

        for enfant in self.enfants:
            enfant.afficher()
    def evaluer(self, dico):
       """Evalue l'expression representee par le noeud"""
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