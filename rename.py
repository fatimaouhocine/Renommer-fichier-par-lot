import shutil
import re
import sys
from pathlib import Path




# Cherche tous les fichiers dans un dossier et ses sous-dossiers
# qui correspondent à l'expression régulière

def collecter_fichiers(dossier: Path, regex: re.Pattern) -> list[Path]:
    """Retourne la liste des fichiers correspondant à la regex."""
    return [
        f for f in dossier.rglob("*")
        if f.is_file() and regex.match(f.name)
    ]

# Crée un nom unique pour le fichier dans le dossier destination
# si un fichier avec le même nom existe déjà, ajoute _1, _2, etc.

def generer_nom_unique(dossier: Path, nom: str) -> Path:
    """Évite les collisions de noms dans le dossier de destination."""
    chemin = dossier / nom
    compteur = 1

    while chemin.exists():
        stem = Path(nom).stem
        ext = Path(nom).suffix
        chemin = dossier / f"{stem}_{compteur}{ext}"
        compteur += 1

    return chemin

# Prépare les actions de renommage et déplacement
# Retourne une liste de tuples : (fichier_source, nouveau_chemin)

def renommer_deplacer(
    source: Path,
    destination: Path,
    regex: re.Pattern,
    remplacement: str
) -> list[tuple[Path, Path]]:
    """Prépare la liste des actions de renommage + déplacement."""
    actions = []

    for fichier in collecter_fichiers(source, regex):
        nouveau_nom = regex.sub(remplacement, fichier.name)
        nouveau_chemin = generer_nom_unique(destination, nouveau_nom)
        actions.append((fichier, nouveau_chemin))

    return actions



def appliquer_actions(actions: list[tuple[Path, Path]]) -> None:
    """Applique réellement les déplacements."""
    for ancien, nouveau in actions:
        shutil.move(str(ancien), str(nouveau))


# Fonction principale
# Gère les arguments, vérifie les dossiers et applique les actions

def main() -> None:
    if len(sys.argv) != 5:      # Vérifie que 4 arguments sont donnés
        print("Usage : python script.py <source> <pattern> <remplacement> <destination>")
        sys.exit(1)

 # Récupère les arguments
    source = Path(sys.argv[1])
    pattern = sys.argv[2]
    remplacement = sys.argv[3]
    destination = Path(sys.argv[4])


 # Vérifie que le dossier source existe sinon creation avec mkdir
    if not source.exists():
        print("Erreur : dossier source introuvable")
        sys.exit(1)

    destination.mkdir(parents=True, exist_ok=True)

    regex = re.compile(pattern, re.IGNORECASE) # Compile l'expression régulière

    actions = renommer_deplacer(source, destination, regex, remplacement) # Prépare les actions de renommage et déplacement


    print(f"{len(actions)} fichier(s) concerné(s)\n")

    for ancien, nouveau in actions:
        print(f"{ancien.name}  ->  {nouveau.name}")

# Demande confirmation avant de déplacer
    if input("\nAppliquer les modifications ? (o/n) : ").lower() != "o":
        print("Opération annulée")
        return

    appliquer_actions(actions) # Déplace réellement les fichiers
    print("Renommage et déplacement terminés")

# Lancement du programme
if __name__ == "__main__":
    main()