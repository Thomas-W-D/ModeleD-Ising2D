"""
Fichier principal à faire tourner.

Il permet de calculer des grandeurs intéressantes d'un réseau de spin pour des
paramètres donnés. On calcule notamment la susceptibilité et la chaleur
spécifique.

Toutes les grandeurs calculées sont par spin, ce qui permet de comparer des
résultats obtenus pour différents types de réseaux.
"""

from fonctions import *


# paramètres des réseaux
L = 4
nb_pas = 1000
h = 0
M_T = []
E_T = []
Sus_T = []
C_T = []
binders = []
T_base = 5 # température initiale
T_tot = np.linspace(1,3,25)
reseaulist = []
for T in T_tot :
    """
    Le tuple contenant les paramètres d'un réseau doivent être sous la forme :
    (type_de_reseau, L, T, J, h, booleen__periodicité_aux_limites)
    """
    liste_param = [(reseau_rand, L, T, 1, h, True) for i in range(50)]

    T_t = np.linspace(T_base, T, 250 * L**2)

    # calcul 
    reseaux = []
    print("Calcul réseaux :")
    for i in range(len(liste_param)):
        liste_spins = [(i,j) for i in range(liste_param[i][1]) for j in range(liste_param[i][1])] # pour choix de spin non aléatoire
        reseaux.append([liste_param[i][0](L=liste_param[i][1])])
        for j in range(nb_pas * liste_param[i][1]**2):
            # on part de la température initiale puis on descend jusqu'à la température finale
            if j < len(T_t):
                reseaux[i].append(pas(reseaux[i][j], T=T_t[j], J=liste_param[i][3], h=h, periodique=liste_param[i][5], spin=None))  ## spin=liste_spins[j%len(liste_spins)] pour méthode 2 (voir CR)
            else :
                reseaux[i].append(pas(reseaux[i][j], T=T, J=liste_param[i][3], h=h, periodique=liste_param[i][5], spin=None))  ## spin=liste_spins[j%len(liste_spins)] pour méthode 2 (voir CR)
        print(f"{i+1}/{len(liste_param)}")
    

    # évolution de l'énergie de tous les systèmes
    energies = []
    print("Calcul énergies :")
    for i in range(len(liste_param)):
        energies.append([H(reseau=reseaux[i][0], J=liste_param[i][3], h=liste_param[i][4], periodique=liste_param[i][5])/(liste_param[i][1]*liste_param[i][1])])
        for j in range(nb_pas * liste_param[i][1]**2):
            energies[i].append(H(reseau=reseaux[i][j+1], J=liste_param[i][3], h=liste_param[i][4], periodique=liste_param[i][5])/(liste_param[i][1]*liste_param[i][1]))
        print(f"{i+1}/{len(liste_param)}")

    # moyenne de l'énergie sur tout les systèmes
    E_moy = moy_ensemble(lim=900, tab_valeurs=np.array(energies), param_res=liste_param,abs=False)
    E_T.append(E_moy)

    # moyenne du carré de l'énergie sur tous les sytèmes
    E2_moy = moy_ensemble(lim=900, tab_valeurs=np.array(energies)**2, param_res=liste_param,abs=False)
    # calcul de la chaleur spécifique 
    print("Calcul de la chaleur spécifique")
    C_T.append((E2_moy-E_moy**2)/T**2)


    # évolution de l'aimantation de tous les systèmes
    aimantations = []
    print("Calcul aimantations :")
    for i in range(len(liste_param)):
        aimantations.append([aimantation(reseau=reseaux[i][0])/(liste_param[i][1]*liste_param[i][1])])
        for j in range(nb_pas * liste_param[i][1]**2):
            aimantations[i].append(aimantation(reseau=reseaux[i][j+1])/(liste_param[i][1]*liste_param[i][1]))
        print(f"{i+1}/{len(liste_param)}")

    # moyenne de l'aimantation sur tout les systèmes
    M_moy = moy_ensemble(lim=900, tab_valeurs=np.array(aimantations), param_res=liste_param)
    M_T.append(M_moy)
    
    # moyenne du carré de l'aimantation sur tous les systèmes
    M2_moy = moy_ensemble(lim=900, tab_valeurs=np.array(aimantations)**2, param_res=liste_param)
    # moyenne de la puissance 4 de l'aimantation sur tous les systèmes
    M4_moy = moy_ensemble(lim=900, tab_valeurs=np.array(aimantations)**4, param_res=liste_param)
    # calcul du coefficient de Binder
    binder = 1-M4_moy/(3*M2_moy**2)
    binders.append(binder)

    # calcul de susceptibilité
    print("Calcul de susceptibilité")
    Sus_T.append((M2_moy-M_moy**2 )/T)


# sauvegarde des grandeurs intéressantes
import pickle
with open("test.pkl", "wb") as f:
    pickle.dump((T_tot,M_T,binders,Sus_T,C_T,E_T),f)
print("J'ai fini")