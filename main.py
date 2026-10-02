
from noeud import Noeud

exp = Noeud("exp")
add = Noeud("+")
deux = Noeud(2)
y = Noeud("y")

add.ajouter_un_enfant(deux)
add.ajouter_un_enfant(y)

exp.ajouter_un_enfant(add)

exp.afficher()
print(add.evaluer({"y": 3}))
import numpy as np

valeurs = np.linspace(-5, 5, 100)

add.tracer("y", valeurs)