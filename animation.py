"""
Programme pour faire l'animation d'un réseau.
On s'en sert pour obetnir des photos de configurations pour le compte-rendu et
vérifier le fonctionnement du code.
"""

from fonctions import *

L = 100 # taille du réseau
T = 3 # température du système
J = 1 # coefficient d'échange
h = 0 # coefficient du champ magnétique externe
periodique = True # conditions aux limites
nb_pas = 100
res = reseau_rand(L=L)


evolution = [res]
for i in range(nb_pas * L*L):
    evolution.append(pas(evolution[i], T, J, h, periodique=periodique))


# animation du réseau
fig, ax = plt.subplots()
cmap = plt.get_cmap("viridis")
image = ax.imshow(evolution[0], cmap=cmap, vmin=-1, vmax=1)
def update(frame):
    image.set_array(evolution[(L*L) * frame])
    return image,
animation = ani.FuncAnimation(fig, update, frames=nb_pas, interval=100, blit=False)
plt.title(f"L={L}, T={T}, h={h}, limites périodiques : {periodique}")
animation.save("ani.gif")
plt.xticks([])
plt.yticks([])
plt.show()