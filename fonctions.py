"""
Fichier où on définit les fonctions importantes des programmes.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

from numba import njit



def reseau_rand(L):
    """
    Fonction qui génère un réseau 2D de taille L qui prend la forme d'un 
    tableau numpy N=L*L contenant des nombres aléatoires compris dans (-1,1).
    """
    return np.random.choice([-1,1], (L,L))


def reseau_homogene(L, sens=1):
    """
    Fonction qui génère un réseau 2D de taille L qui prend la forme d'un 
    tableau numpy N=L*L contenant des nombres égaux à 'sens'.
    """
    return sens * np.ones((L,L))


def reseau_damier(L):
    """
    Fonction qui génère un réseau 2D de taille L qui prend la forme d'un 
    tableau numpy N=L*L contenant des nombres compris dans (-1,1) en damier.
    'debut' indique l'orientation du spin en haut à gauche.
    """
    res = np.arange(0,L*L)
    res[res%2 != 0] = -1
    res[res%2 == 0] = 1
    res = np.reshape(res,(L,L))
    if L%2 == 0:
        res[np.arange(0,L)%2!=0] = -1*res[np.arange(0,L)%2!=0]
    return res


def H(reseau, J=1, h=0, periodique=True):
    """Hamiltonien du système."""
    voisin_droite = np.roll(reseau,-1,axis=1)
    voisin_bas = np.roll(reseau,-1,axis=0)
    if not(periodique):
        voisin_bas[-1] = np.zeros(reseau.shape[0])
        voisin_droite[:,-1] = np.zeros(reseau.shape[0]).T
    somme = np.sum(reseau * (voisin_droite+voisin_bas))
    return -J*somme + h*np.sum(reseau)

@njit
def dH(reseau, spin, J=1, h=0, periodique=True):
    """
    Calcule la variation d'énergie entre la configuration actuelle et la
    possible future configuration.
    """
    taille_reseau = reseau.shape[0]
    dE = 2*reseau[spin] * (J*reseau[(spin[0]-1)%taille_reseau, spin[1]]
                            + J*reseau[(spin[0]+1)%taille_reseau, spin[1]]
                            + J*reseau[spin[0], (spin[1]-1)%taille_reseau]
                            + J*reseau[spin[0], (spin[1]+1)%taille_reseau]
                            + h)
    # on regarde les effets de bord
    if not(periodique):
        if spin[0] == 0:
            dE -= 2*reseau[spin] * reseau[(spin[0]-1)%taille_reseau, spin[1]]
        if spin[0] == taille_reseau-1:
            dE -= 2*reseau[spin] * reseau[(spin[0]+1)%taille_reseau, spin[1]]
        if spin[1] == 0:
            dE -= 2*reseau[spin] * reseau[spin[0], (spin[1]-1)%taille_reseau]
        if spin[1] == taille_reseau-1:
            dE -= 2*reseau[spin] * reseau[spin[0], (spin[1]+1)%taille_reseau]
    return dE


@njit
def aimantation(reseau):
    """Calcule l'aimantation (somme des spins) du système."""
    return np.sum(reseau)

@njit
def pas(reseau, T, J=1, h=0, periodique=True, spin=None):
    """
    Effectue un 'Monte-Carlo step'.
    Si 'spin'=None, on prend un spin aléatoirement dans le réseau. Sinon, on
    donne un spin choisit au préalable (ça permet de passer par tous les spins).
    """
    # choix aléatoire d'un spin
    if spin is None:
        spin = (np.random.randint(0, reseau.shape[0]), np.random.randint(0, reseau.shape[0]))
    # comparaison entre deux configurations (actuelle et possible suivante)
    dE = dH(reseau, spin, J, h, periodique)
    if dE < 0:
        reseau2 = np.copy(reseau)
        reseau2[spin] = -reseau2[spin]
        return reseau2
    elif np.random.uniform(0,1) < np.exp(-dE/T):
        reseau2 = np.copy(reseau)
        reseau2[spin] = -reseau2[spin]
        return reseau2
    else:
        return reseau


def moy_ensemble(lim, tab_valeurs, param_res, abs=True):
    """
    Calcule une moyenne d'ensemble à partir d'une liste de valeurs d'une grandeur.
    On fait d'abord une moyenne sur quelques valeurs pour un run (à partir de
    'lim' et on espace d'un MC Sweep), puis on moyenne sur les différents run.
    - 'lim' indique à partir de quel pas on prend des valeurs pour les moyenner.
    - 'tab_valeurs' est le tableau contenant la valeur de la grandeur à chaque
    pas, pour différents run.
    - 'param_res' est le tuple contenant tous les paramètres du réseau.
    - 'abs' pour les grandeurs qui doivent être en valeur absolue (ex: aimantation).
    """
    moy = 0
    if abs:
        for i in range(tab_valeurs.shape[0]):
            moy += np.abs(np.sum(tab_valeurs[i][lim*param_res[i][1]*param_res[i][1]::param_res[i][1]*param_res[i][1]]))/(tab_valeurs[i][lim*param_res[i][1]*param_res[i][1]::param_res[i][1]*param_res[i][1]]).size
    else:
        for i in range(tab_valeurs.shape[0]):
            moy += np.sum(tab_valeurs[i][lim*param_res[i][1]*param_res[i][1]::param_res[i][1]*param_res[i][1]])/(tab_valeurs[i][lim*param_res[i][1]*param_res[i][1]::param_res[i][1]*param_res[i][1]]).size
    moy /= tab_valeurs.shape[0]
    return moy