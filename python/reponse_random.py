""" Illustration d'une réponse randomnisée
comme présentée en page 11 du Hands-On DP de Cowan et al.
"""

import random
import numpy as np
# import pandas as pd

# Préparation situation
random.seed(13122024)
nb_eleves = 10
notes_all = [random.gauss(mu=85, sigma=10) // 1 for i in range(nb_eleves)]

moy_all = np.mean(notes_all)
note_ele_parti = min(notes_all)
index_note_ele_parti = [i for i in range(nb_eleves) if notes_all[i] == note_ele_parti][0]
index_sans = [i for i in range(nb_eleves) if i != index_note_ele_parti]

notes_sans = [notes_all[i] for i in index_sans]
moy_sans = np.mean(notes_sans)


def retrouver_note(m1: float, m2: float, n: int):
    """
    Trouver la valeur de la note de l'étudaint parti à partir des deux moyennes
    """

    return n*m1 - (n-1)*m2


retrouver_note(moy_all, moy_sans, 10)


def randomiser_reponse(original: list, p=0.5, v=5):
    """
    Calcule une réponse randomisée du vecteur original fourni
    p: probabilité de succès
    v: variance de la loi gaussienne
    """

    reponse_rand = []

    for i in range(len(original)):
        # lancer de piece 1
        c1 = random.uniform(0, 1)
        if c1 > p:
            reponse_rand.append(original[i])
        else:
            # lancer de piece 2
            c2 = random.uniform(0, 1)
            if c2 > p:
                reponse_rand.append(original[i])
            else:
                reponse_rand.append(original[i] + random.gauss(0, v))

    return reponse_rand


notes_rand = randomiser_reponse(notes_all)
print(notes_rand)
np.mean(notes_rand)
notes_rand_sans = [notes_rand[i] for i in index_sans]
np.mean(notes_rand_sans)

retrouver_note(np.mean(notes_rand), np.mean(notes_rand_sans), 10)

# Quelle est la probabilité d'avoir la bonne réponse ?

# Quelle est la variabilité du résultat sur le résultat obtenu ?
