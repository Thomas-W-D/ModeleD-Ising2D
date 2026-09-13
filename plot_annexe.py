"""
Programme pour les graphes des annexes 1 et 2.
"""

import pickle as pk
import numpy as np
import matplotlib.pyplot as plt


# chemin des trois fichiers à comparer
file_4 = "./Dernière version/L4,n1000,l900,50r.pkl"
file_4_nonperiodique = "./Dernière version/L4,n1000,l900,50r,non_periodique.pkl"
file_4_nonaleat = "./Dernière version/L4,n1000,l900,50r,spin_nonaleat.pkl"

with open(file_4, "rb") as f:
    T_tot4, M_T4, binders_T4, Sus_T4, C_T4, E_T4 = pk.load(f)
with open(file_4_nonperiodique, "rb") as f:
    T_tot4_nonperiodique, M_T4_nonperiodique, binders_T4_nonperiodique, Sus_T4_nonperiodique, C_T4_nonperiodique, E_T4_nonperiodique = pk.load(f)
with open(file_4_nonaleat, "rb") as f:
    T_tot4_nonaleat, M_T4_nonaleat, binders_T4_nonaleat, Sus_T4_nonaleat, C_T4_nonaleat, E_T4_nonaleat = pk.load(f)


# pour l'annexe 1
plt.subplot(2,3,1)
plt.plot(T_tot4, E_T4, "bx")
plt.plot(T_tot4_nonperiodique, E_T4_nonperiodique, "r+")
plt.title("Energie (unités de $k_B$, par spin)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()


plt.subplot(2,3,2)
plt.plot(T_tot4, M_T4, "bx")
plt.plot(T_tot4_nonperiodique, M_T4_nonperiodique, "r+")
plt.title("Aimantation absolue (unités de spin, par spin)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()


plt.subplot(2,3,3)
plt.plot(T_tot4, binders_T4, "bx")
plt.plot(T_tot4_nonperiodique, binders_T4_nonperiodique, "r+")
plt.title("Cumulant de Binder (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()


plt.subplot(2,2,3)
plt.plot(T_tot4, Sus_T4, "bx")
plt.plot(T_tot4_nonperiodique, Sus_T4_nonperiodique, "r+")
plt.title("$\chi$ (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.xlabel("Température (unités de $k_B$)")
plt.grid()


plt.subplot(2,2,4)
plt.plot(T_tot4, C_T4, "bx")
plt.plot(T_tot4_nonperiodique, C_T4_nonperiodique, "r+")
plt.title("$C_v$ (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()



plt.show()





# pour l'annexe 2
plt.subplot(2,3,1)
plt.plot(T_tot4, E_T4, "bx")
plt.plot(T_tot4_nonaleat, E_T4_nonaleat, "r+")
plt.title("Energie (unités de $k_B$, par spin)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()


plt.subplot(2,3,2)
plt.plot(T_tot4, M_T4, "bx")
plt.plot(T_tot4_nonaleat, M_T4_nonaleat, "r+")
plt.title("Aimantation absolue (unités de spin, par spin)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()


plt.subplot(2,3,3)
plt.plot(T_tot4, binders_T4, "bx")
plt.plot(T_tot4_nonaleat, binders_T4_nonaleat, "r+")
plt.title("Cumulant de Binder (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()


plt.subplot(2,2,3)
plt.plot(T_tot4, Sus_T4, "bx")
plt.plot(T_tot4_nonaleat, Sus_T4_nonaleat, "r+")
plt.title("$\chi$ (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.xlabel("Température (unités de $k_B$)")
plt.grid()


plt.subplot(2,2,4)
plt.plot(T_tot4, C_T4, "bx")
plt.plot(T_tot4_nonaleat, C_T4_nonaleat, "r+")
plt.title("$C_v$ (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()



plt.show()