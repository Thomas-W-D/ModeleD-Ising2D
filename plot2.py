"""
Programme pour effectuer l'ajustement de l'expression d'Onsager sur les données.
"""

import numpy as np
import pickle as pk
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d



# chemin des trois fichiers à comparer
file_4 = "./Dernière version/L4,n1000,l900,50r.pkl"
file_8 = "./Dernière version/L8,n1000,l900,50r.pkl"
file_16 = "./Dernière version/L16,n1000,l900,50r.pkl"

with open(file_4, "rb") as f:
    T_tot4, M_T4, binders_T4, Sus_T4, C_T4, E_T4 = pk.load(f)
with open(file_8, "rb") as f:
    T_tot8, M_T8, binders_T8, Sus_T8, C_T8, E_T8 = pk.load(f)
with open(file_16, "rb") as f:
    T_tot16, M_T16, binders_T16, Sus_T16, C_T16, E_T16 = pk.load(f)

def M_th(T, Tc):
    """Fonction à ajuster (expression de L. Onsager)."""
    Tc = float(Tc)
    res = np.concatenate([(1 - 1/(np.sinh(2/T[T < Tc])**4))**(1/8), 0*T[T >= Tc]])
    res[np.isnan(res)] = 0
    return res


def fit(f, x, y):
    """Fonction d'ajustement."""
    Y = interp1d(x, y, kind="linear", fill_value="extrapolate")
    X = np.linspace(np.min(x), np.max(x), 10000)
    Tc_tab = np.linspace(1, 4, 10000)
    err = []
    for Tc in Tc_tab:
        err.append(np.sum((f(X, Tc) - Y(X))**2))
    err = np.array(err)
    return Tc_tab[np.where(err == np.min(err))[0][0]]




# courbe pour L = 4
Tc4 = fit(M_th, T_tot4, np.array(M_T4))
print("Tc (L=4) :", Tc4)
plt.subplot(1,3,1)
plt.plot(T_tot4, M_T4, "bx", label="Données")
plt.plot(np.linspace(np.min(T_tot4),np.max(T_tot4), 100), M_th(np.linspace(np.min(T_tot4),np.max(T_tot4), 100), Tc=Tc4), "k", label="Ajustement")
plt.xlabel("Température (unités de $k_B$)")
plt.title(r"$|m|$ en fonction de $T$ pour $L = 4$")
plt.legend()
plt.grid()


# courbe pour L = 8
Tc8 = fit(M_th, T_tot8, np.array(M_T8))
print("Tc (L=8) :", Tc8)
plt.subplot(1,3,2)
plt.plot(T_tot8, M_T8, "r+", label="Données")
plt.plot(np.linspace(np.min(T_tot8),np.max(T_tot8), 100), M_th(np.linspace(np.min(T_tot8),np.max(T_tot8), 100), Tc=Tc4), "k", label="Ajustement")
plt.xlabel("Température (unités de $k_B$)")
plt.title(r"$|m|$ en fonction de $T$ pour $L = 8$")
plt.legend()
plt.grid()


# courbe pour L = 16
Tc16 = fit(M_th, T_tot16, np.array(M_T16))
print("Tc (L=16) :", Tc16)
plt.subplot(1,3,3)
plt.plot(T_tot16, M_T16, linestyle="", marker="^", markersize=5, markerfacecolor="none", markeredgecolor="green", label="Données")
plt.plot(np.linspace(np.min(T_tot16),np.max(T_tot16), 100), M_th(np.linspace(np.min(T_tot16),np.max(T_tot16), 100), Tc=Tc16), "k", label="Ajustement")
plt.xlabel("Température (unités de $k_B$)")
plt.title(r"$|m|$ en fonction de $T$ pour $L = 16$")
plt.legend()
plt.grid()


plt.show()