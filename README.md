Le nom du projet : renommer des fichiers par lot
Nom de groupe : CEZAM.
Membre de groupe :
1.	OUHOCINE Fatima.
2.	HAMADACHE Nada.

Dans le cadre de ce projet nous traitons le sujet de "Renommage de fichiers par lot". L’objectif est de concevoir un programme qui permet de renommer un grand nombre de fichiers en suivant un motif donné par l’utilisateur. 
Le noyau minimal peut comporter les fonctionnalités suivantes :
1.	La recherche ou la sélection des fichiers à renommer: Permettre à l’utilisateur de chercher et de sélectionner l’ensemble de fichiers à renommer que ça soit dans le même dossier ou pas.
2.	La définition des motifs de reconnaissances : Permettre à l’utilisateur de sélectionner les parties importantes dans le nom d’un fichier via les expressions régulières. Cette étape dépend de la partie 1.
3.	Définition d’un schéma de renommage : Permet de spécifier la nouvelle forme de nom, en utilisant les parties extraites de l’étape précédente. Cette étape dépend de la partie 2.
4.	Evitement des collisions : Permet de vérifier qu’il n’existe pas des fichiers qui recevront le même nom de fichier après le renommage. Cette étape dépend de la partie 3.
5.	Prévention des Pertes : Permet de s’assurer qu’aucun fichier ne sera perdu ou bien remplacer par un autre fichier(écraser). Cette étape dépend de la partie 4.
6.	La validation avant le renommage : Permet une correspondance entre les anciens et les nouveaux noms de fichiers afin de permettre à l’utilisateur de vérifier le résultat et de le confirmer avant son exécution réelle. Cette étape dépend des parties 2, 3, 4 et 5.
7.	Exécution du renommage : c’est l’étape où on applique effectivement les modifications (les nouveaux noms aux fichiers). Cette étape dépend de la partie 6.
Avec ces fonctionnalités décrites ci-dessus, on aura déjà un programme fonctionnel. 
Mais on peut encore ajouter quelques fonctionnalités complémentaires :
8.	La génération d’un script d’annulation : Permet de récupérer l’ancien nom pour chaque fichier (avant le renommage). Cette étape dépend de la partie 7.
9.	Déplacement entre volumes : Permet de déplacer les fichiers soit dans le même disque ou bien entre différents disques. Cette étape dépend de la partie 7. 
10.	La portabilité entre Windows, Linux et MacOs : Permet d’assurer le fonctionnement du programme sur Windows, Linux et MacOS. Cette étape dépend de la partie 7.

