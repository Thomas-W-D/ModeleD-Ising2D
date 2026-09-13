# Evolution du modèle d'Ising 2D

Projet numérique de L3 Physique SPRINT qui a pour objectif la simulation de l'évolution d'un matériau simulé par modèle d'Ising 2D.

**Collaboration avec Skander Bouguessa et Adrian Tello.**

Les résultats du projet sont à trouver dans le fichier *Compte_rendu.pdf* (**quelques erreurs d'unité sont à relever sur les graphes**).

Description rapide des différents fichiers de code :
- fonctions.py    -> pour les fonctions importantes pour le réseau et son évolution.
- Calculs.py      -> effectue les calculs d'évolution des réseaux et de grandeurs
                  thermodynamiques. Peut prendre du temps à faire tourner, notamment
                  pour des réseaux de grande taille.
- animation.py    -> utile pour faire des animations, pour vérifier que le code
                  fonctionne correctement et obtenir des photos de configurations.
- plot.py         -> pour les graphes des fonctions thermodynamiques.
- plot2.py        -> pour les graphes d'ajustement.
- plot_annexe.py  -> pour les graphes des annexes 1 et 2.
- champ_mag.py    -> pour le test d'un champ magnétique variable.
