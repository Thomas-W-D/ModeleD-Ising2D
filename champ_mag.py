"""
Programme pour tester l'influence d'un champ magnétique externe sur le réseau.
"""

from fonctions import *

L = 16 # taille du réseau
J = 1 # coefficient d'échange
periodique = True # conditions aux limites
nb_pas = 100
res = reseau_rand(L=L)

h_liste = np.linspace(-3,3,100*L*L) # évolution en rampe de -3 à 3


# T = 1
evolution = [res]
energies = [H(res, J=J, h=0, periodique=periodique)/(L*L)]
aimantations = [aimantation(res)/(L*L)]
for i in range(nb_pas * L*L):
    evolution.append(pas(evolution[i], T=1, J=J, h=h_liste[i], periodique=periodique))
    energies.append(H(evolution[i+1], J=J, h=h_liste[i], periodique=periodique)/(L*L))
    aimantations.append(aimantation(evolution[i+1])/(L*L))

plt.subplot(1,2,1)
plt.plot(energies[::L*L], label="Énergie")
plt.plot(aimantations[::L*L], label="Aimantation")
plt.grid()
plt.xlim(0,nb_pas)
plt.xlabel("Temps (nombre de MC Sweep)")
plt.legend()
plt.title("T = 1")


# T = 3
evolution = [res]
energies = [H(res, J=J, h=0, periodique=periodique)/(L*L)]
aimantations = [aimantation(res)/(L*L)]
for i in range(nb_pas * L*L):
    evolution.append(pas(evolution[i], T=3, J=J, h=h_liste[i], periodique=periodique))
    energies.append(H(evolution[i+1], J=J, h=h_liste[i], periodique=periodique)/(L*L))
    aimantations.append(aimantation(evolution[i+1])/(L*L))

plt.subplot(1,2,2)
plt.plot(energies[::L*L], label="Énergie")
plt.plot(aimantations[::L*L], label="Aimantation")
plt.grid()
plt.xlim(0,nb_pas)
plt.xlabel("Temps (nombre de MC Sweep)")
plt.legend()
plt.title("T = 3")



plt.show()