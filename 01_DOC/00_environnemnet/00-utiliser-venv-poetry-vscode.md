# Guide de configuration de Poetry avec environnement virtuel local

Ce guide détaille la procédure complète pour configurer correctement un environnement Poetry local, particulièrement utile pour résoudre les problèmes de débogage dans VS Code.

## 1. Supprimer l'environnement problématique

Avant de commencer, supprimez tout environnement Poetry existant pour votre projet :

```bash
# Identifiez l'environnement actuel
poetry env list

# Supprimez l'environnement problématique
rm -rf ~/Library/Caches/pypoetry/virtualenvs/[nom-environnement]

# Alternative : suppression avec Poetry
poetry env remove --all
```

Cela permet de repartir sur une base propre sans conflits potentiels.

## 2. Désactiver l'environnement Conda base

Si vous utilisez Conda, désactivez l'environnement base pour éviter les conflits d'environnements :

```bash
conda deactivate
```

Votre invite de commande ne devrait plus afficher le préfixe `(base)`.

## 3. Configurer Poetry pour utiliser un environnement local

Configurez Poetry pour créer les environnements virtuels dans le dossier du projet :

```bash
# Définir la création des environnements dans le projet
poetry config virtualenvs.in-project true
```

## 4. Créer l'environnement virtuel local

Créez manuellement un environnement virtuel et configurez Poetry pour l'utiliser :

```bash
# Créer un environnement virtuel standard
python -m venv .venv

# Dire à Poetry d'utiliser cet environnement
poetry env use .venv/bin/python

# Installer les dépendances du projet
poetry install
```

Cette approche garantit un emplacement cohérent et prévisible pour votre environnement.

## 5. Activer l'environnement

Pour activer l'environnement dans votre terminal :

```bash
# Pour macOS/Linux
source .venv/bin/activate

# Pour Windows
.venv\Scripts\activate
```

Votre invite de commande devrait maintenant afficher le préfixe `(.venv)`.

## 6. Installer des dépendances

Pour ajouter de nouvelles dépendances au projet :

```bash
# Ajouter une dépendance
poetry add nom-package

# Ajouter une dépendance de développement
poetry add nom-package --group dev
```

Poetry mettra automatiquement à jour le fichier `pyproject.toml` et le fichier `poetry.lock`.

## 7. Vérifier les dépendances installées

Pour consulter les dépendances installées :

```bash
# Liste toutes les dépendances
poetry show

# Affiche les détails d'une dépendance spécifique
poetry show nom-package

# Affiche l'arbre des dépendances
poetry show --tree
```

## 8. Vérifier la configuration de Poetry

Pour consulter toutes les configurations actives de Poetry :

```bash
poetry config --list
```

Vérifiez notamment que `virtualenvs.in-project = true` est bien activé.

## 9. Exécuter des scripts

Pour exécuter un script Python dans l'environnement Poetry :

```bash
# Méthode recommandée
poetry run python votre_script.py

# Exécuter un script avec des arguments
poetry run python votre_script.py arg1 arg2
```

## 10. Configuration du débogueur VS Code

Pour que VS Code utilise correctement votre environnement Poetry, configurez le fichier `.vscode/launch.json` :

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": false,
            "python": "${workspaceFolder}/.venv/bin/python",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

N'oubliez pas de sélectionner l'interpréteur Python correct dans VS Code via la palette de commandes :
* `Cmd+Shift+P` > "Python: Select Interpreter" > Sélectionnez l'interpréteur dans `.venv/bin/python`

## Bonnes pratiques

1. Ajoutez `.venv/` à votre fichier `.gitignore` pour éviter de versionner l'environnement
2. Utilisez `poetry export -f requirements.txt > requirements.txt` pour générer un fichier requirements.txt si nécessaire
3. Supprimez régulièrement les environnements inutilisés avec `poetry env remove --all`
4. Vérifiez les mises à jour des dépendances avec `poetry update --dry-run`