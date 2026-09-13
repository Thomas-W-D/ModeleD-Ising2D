"""
Programme pour tracer les premiers graphes du compte-rendu.
"""

import pickle as pk
import numpy as np
import matplotlib.pyplot as plt


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


# énergie et aimantation
plt.subplot(1,2,1)
plt.plot(T_tot4, E_T4, "bx", label="L = 4")
plt.plot(T_tot8, E_T8, "r+", label="L = 8")
plt.plot(T_tot16, E_T16, linestyle="", marker="^", markersize=5, markerfacecolor="none", markeredgecolor="green", label="L = 16")
plt.title("Energie (unités de $k_B$, par spin)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()
plt.legend()
plt.xlabel("Température (unités de $k_B$)")


plt.subplot(1,2,2)
plt.plot(T_tot4, M_T4, "bx")
plt.plot(T_tot8, M_T8, "r+")
plt.plot(T_tot16, M_T16, linestyle="", marker="^", markersize=5, markerfacecolor="none", markeredgecolor="green")
plt.title("Aimantation absolue (unités de spin, par spin)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()


plt.show()



# chaleur spécifique et susceptibilité magnétique
plt.subplot(1,2,2)
plt.plot(T_tot4, Sus_T4, "bx")
plt.plot(T_tot8, Sus_T8, "r+")
plt.plot(T_tot16, Sus_T16, linestyle="", marker="^", markersize=5, markerfacecolor="none", markeredgecolor="green")
plt.title("$\chi$ (sans unité)")

T_C_sus4 = T_tot4[np.where(Sus_T4 == np.max(Sus_T4))]
T_C_sus8 = T_tot8[np.where(Sus_T8 == np.max(Sus_T8))]
T_C_sus16 = T_tot16[np.where(Sus_T16 == np.max(Sus_T16))]
print(f"T_C,mesure^Sus4  = {T_C_sus4[0]}")
print(f"T_C,mesure^Sus8  = {T_C_sus8[0]}")
print(f"T_C,mesure^Sus16  = {T_C_sus16[0]}")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()

ylim = plt.ylim()
plt.plot([T_C_sus4, T_C_sus4], ylim, "k--") # plot de Tc_mesure
plt.text(T_C_sus4+0.05, 0.1, r"$T_{C,mesure}^{Sus4}$").set_rotation(90)
plt.plot([T_C_sus8, T_C_sus8], ylim, "k--") # plot de Tc_mesure
plt.text(T_C_sus8+0.008, 0.1, r"$T_{C,mesure}^{Sus8}$").set_rotation(90)
plt.plot([T_C_sus16, T_C_sus16], ylim, "k--") # plot de Tc_mesure
plt.text(T_C_sus16-0.1, 0.1, r"$T_{C,mesure}^{Sus16}$").set_rotation(90)
plt.ylim(ylim)



plt.subplot(1,2,1)
plt.plot(T_tot4, C_T4, "bx", label="L = 4")
plt.plot(T_tot8, C_T8, "r+", label="L = 8")
plt.plot(T_tot8, C_T16, linestyle="", marker="^", markersize=5, markerfacecolor="none", markeredgecolor="green", label="L = 16")
plt.title("$C_v$ (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])

T_C_cha4 = T_tot4[np.where(C_T4 == np.max(C_T4))]
T_C_cha8 = T_tot8[np.where(C_T8 == np.max(C_T8))]
T_C_cha16 = T_tot16[np.where(C_T16 == np.max(C_T16))]
print(f"T_C,mesure^Chaleur4  = {T_C_cha4[0]}")
print(f"T_C,mesure^Chaleur8  = {T_C_cha8[0]}")
print(f"T_C,mesure^Chaleur16  = {T_C_cha16[0]}")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.grid()
plt.legend()
plt.xlabel("Température (unités de $k_B$)")

ylim = plt.ylim()
plt.plot([T_C_cha4, T_C_cha4], ylim, "k--") # plot de Tc_mesure
plt.text(T_C_cha4+0.01, 0.03, r"$T_{C,mesure}^{Chaleur4}$").set_rotation(90)
plt.plot([T_C_cha8, T_C_cha8], ylim, "k--") # plot de Tc_mesure
plt.text(T_C_cha8+0.11, 0.03, r"$T_{C,mesure}^{Chaleur8}$").set_rotation(90)
plt.plot([T_C_cha16, T_C_cha16], ylim, "k--") # plot de Tc_mesure
plt.text(T_C_cha16-0.1, 0.03, r"$T_{C,mesure}^{Chaleur16}$").set_rotation(90)
plt.ylim(ylim)


plt.show()



plt.plot(T_tot4, binders_T4, "bx", label="L = 4")
plt.plot(T_tot8, binders_T8, "r+", label="L = 8")
plt.plot(T_tot16, binders_T16, linestyle="", marker="^", markersize=5, markerfacecolor="none", markeredgecolor="green", label="L = 16")
plt.title("Cumulant de Binder (sans unité)")
plt.xlim(T_tot4[0], T_tot4[-1])
plt.xlabel("Température (unités de $k_B$)")
plt.legend()
plt.grid()

ylim = plt.ylim()
plt.plot([2.23, 2.23], ylim, "k--") # plot de Tc_mesure
plt.text(2.25, 0.32, r"$T_{C,mesure}^{Binder}$")
plt.ylim(ylim)

plt.show()