# Renommage des fichiers par lot 
## Groupe CEZAM
| Nom  |Prénom   | Numéro d'étudiant | 
|:-----|:-------:|------------------:|
|OUHOCINE|Fatima |20245633|
|HAMADACHE|Nada |20246691|

## Dans le cadre de ce projet nous traitons le sujet de "Renommage de fichiers par lot". L’objectif est de concevoir un programme qui permet de renommer un grand nombre de fichiers en suivant un motif donné par l’utilisateur.
 ## Noyeau minimal:
 Le noyeau minimal peut comprter les fonctionnalités suivantes:
 ## #1 La définition des motifs de reconnaissances
 Permettre à l'utilisateur de selectionner et d'extraire les parties importantes dans un nom de fichiers via les éxpressions régulières.
 ## #2 La definition d'un schéma de renommage 
 Permet de spécifier la nouvelle forme de nom, en utilisant les parties extraites de la partie précédente.
 > cette étape dépend de #1.
 ## #3 Evitement des collisions
  Permet de vérifier qu’il n’existe pas des fichiers qui recevront le même nom de fichier après le renommage.
  > cette étape dépend de la partie #2.
  ## #4 La validation avant le renommage 
  Permet une correspondance entre les anciens et les nouveaux noms de fichiers afin de permettre à l’utilisateur de vérifier le résultat et de le confirmer avant son exécution réelle. Cette étape dépend des parties 2, 3, 4 et 5.
  > cette étape dépend des parties #1, #2, #3.
  ## #5 Exécution du renammage 
  c’est l’étape où on applique effectivement les modifications (les nouveaux noms aux fichiers).
  > cette étape dépend de la partie #5.
  # Fonctionnalités suplémentaires:
  ## #6 La génération d’un script d’annulation 
  Permet de récupérer l’ancien nom pour chaque fichier (avant le renommage).  
  >Cette étape dépend de la partie #5.
  ## #7 Déplacement entre volumes
  Permet de déplacer les fichiers soit dans le même disque ou bien entre différents disques.
  >Cette étape dépend de la partie 5. 
  ## #8 La portabilité entre Windows, Linux et MacOs 
  Permet d’assurer le fonctionnement du programme sur Windows, Linux et MacOS. 
  >Cette étape dépend de la partie 5

# La réalisation de ce projet:
##  Bibliothèques utilisées

Dans ce projet, nous avons utilisé uniquement des bibliothèques standards de Python, ce qui permet au script de fonctionner sans installation supplémentaire.

* **`shutil`** : utilisée pour déplacer les fichiers d’un dossier vers un autre.
* **`re`** : permet de travailler avec des expressions régulières afin de filtrer et renommer les fichiers.
* **`sys`** : sert à récupérer les arguments passés lors de l’exécution du script en ligne de commande.
* **`pathlib.Path`** : facilite la gestion des chemins de fichiers et de dossiers de manière plus lisible.

---

##  Structure du code

Nous avons organisé le code en plusieurs fonctions afin de le rendre plus clair et plus facile à comprendre. Chaque fonction a un rôle précis.

### `collecter_fichiers(dossier, regex)`

Cette fonction parcourt le dossier source ainsi que ses sous-dossiers. Elle récupère uniquement les fichiers dont le nom correspond à l’expression régulière donnée par l’utilisateur.

Son objectif principal est de **repérer les fichiers à traiter**.

---

### `generer_nom_unique(dossier, nom)`

Cette fonction permet d’éviter les conflits de noms dans le dossier de destination. Si un fichier avec le même nom existe déjà, un suffixe numérique est ajouté automatiquement.

Elle garantit que **aucun fichier ne sera écrasé**.

---

### `renommer_deplacer(source, destination, regex, remplacement)`

Cette fonction regroupe la logique principale du programme. Elle prépare les opérations à effectuer : renommage des fichiers et définition de leur nouveau chemin.

À ce stade, les fichiers ne sont pas encore déplacés, ce qui permet d’afficher un résumé avant l’exécution.

---

### `appliquer_actions(actions)`

Cette fonction applique réellement les modifications. Elle déplace chaque fichier vers le dossier de destination avec son nouveau nom.

---

### `main()`

La fonction `main` gère l’exécution générale du script. Elle vérifie les arguments fournis, contrôle l’existence des dossiers, affiche les fichiers concernés et demande une confirmation avant d’appliquer les changements.

Le programme est lancé grâce à la condition :

```python
if __name__ == "__main__":
```

---

##  Répartition du travail 

### HAMADACHE Nada

* Renommage et move avec la fonction def renommer_deplacer
* Applique les modifications avec def applique action  
* Gestion des arguments de la ligne de commande
* Vérification des erreurs
* Gère les arguments, vérifie les dossiers et applique les actions

### OUHOCINE Fatima

* Recherche et filtrage des fichiers avec def  collecter_fichier
* Gestion des conflits de noms avec def generer_nom_unique
* Gestion des arguments de la ligne de commande
* Vérification des erreurs
* Gère les arguments, vérifie les dossiers et applique les actions

  
##  Utilisation en ligne de commande

Le script s’exécute depuis un terminal ou une invite de commandes. Il prend quatre arguments :

```bash
python rename.py <dossier_source> <pattern_regex> <remplacement> <dossier_destination>

exemple : python rename.py ( "C:/Users/Hamadache Nada/Pictures/Screenshots" "(.*)\.png" "\1.jpeg" "C:/tmp/photo/")
le dossier source contient des images au format PNG,

l’expression régulière (.*)\.png permet de sélectionner tous les fichiers avec l’extension .png,

le remplacement \1.jpeg conserve le nom du fichier et change uniquement l’extension en .jpeg,

le dossier de destination est C:/tmp/photo/.

Avant d’appliquer les modifications, le script affiche la liste des fichiers concernés et demande une confirmation à l’utilisateur.


---









