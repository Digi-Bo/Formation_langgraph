# Guide d'installation - Agent de réflexion avec LangChain et LangGraph sur Mac

Ce guide vous accompagne étape par étape dans la configuration d'un projet d'agent de réflexion utilisant LangChain et LangGraph sur un Mac. Nous aborderons la création de l'environnement, l'installation des dépendances et la préparation du projet pour éviter les erreurs courantes.

## 1. Création du répertoire de projet

Commençons par créer un espace de travail pour notre projet :

```bash
# Créer un dossier pour notre projet
mkdir -p ~/Documents/ReflectionAgent

# Naviguer dans ce répertoire
cd ~/Documents/ReflectionAgent
```

## 2. Installation et configuration de Poetry

Poetry est un outil de gestion de dépendances moderne pour Python. Voici comment l'installer et le configurer :

```bash
# Installer Poetry via Homebrew (si Homebrew est déjà installé)
brew install poetry

# Si vous n'avez pas Homebrew, vous pouvez installer Poetry avec cette commande
# curl -sSL https://install.python-poetry.org | python3 -

# Vérifier l'installation
poetry --version
```

## 3. Initialisation du projet Poetry avec la version Python appropriée

⚠️ **Important** : Pour éviter les problèmes de compatibilité avec LangChain et LangGraph, nous utiliserons Python 3.11 plutôt que Python 3.12.

```bash
# Installer Python 3.11 si nécessaire
brew install python@3.11

# S'assurer que Python 3.11 est disponible
python3.11 --version

# Initialiser un nouveau projet Poetry
cd ~/Documents/ReflectionAgent
poetry init

# Lors de l'initialisation interactive
# - Acceptez les valeurs par défaut pour le nom, la version et la description
# - Pour la version Python compatible, spécifiez : ">=3.9,<3.12"
# - Pour les dépendances, répondez "no" (nous les ajouterons manuellement)
```


## Installation des packages : 

Maintenant, installons les packages requis pour notre projet :

```python

poetry add python-dotenv
poetry add black isort
poetry add langchain
poetry add langchain-openai
poetry add langgraph
poetry add grandalf



```




## 4. Configuration du fichier pyproject.toml

Pour éviter les erreurs liées à l'installation du package racine, modifiez votre fichier `pyproject.toml` :

```toml
[tool.poetry]
name = "reflectionagent"
version = "0.1.0"
description = "Agent de réflexion utilisant LangChain et LangGraph"
authors = ["Votre Nom <votre.email@exemple.com>"]
readme = "README.md"
package-mode = false  # Ajoutez cette ligne pour éviter l'erreur d'installation du projet racine

[tool.poetry.dependencies]
python = ">=3.9,<3.12"
python-dotenv = ">=1.1.0,<2.0.0"
black = ">=25.1.0,<26.0.0"
isort = ">=6.0.1,<7.0.0"
langchain = ">=0.3.24,<0.4.0"
langchain-openai = ">=0.3.14,<0.4.0"
langgraph = ">=0.3.34,<0.4.0"
grandalf = "^0.8"  # Nécessaire pour visualiser les graphes

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

## 5. Création de l'environnement virtuel et installation des dépendances

```bash
# Spécifier explicitement Python 3.11 pour l'environnement
poetry env use python3.11

# Installer les dépendances définies dans pyproject.toml
poetry install --no-root

# Vérifier que les dépendances sont correctement installées
poetry show
```

## 6. Configuration des variables d'environnement

Créez un fichier `.env` à la racine de votre projet pour stocker les clés API nécessaires :

```bash
# Créer le fichier .env
touch .env
```

Puis ajoutez-y vos clés :

```
OPENAI_API_KEY=votre_clé_api_openai
LANGCHAIN_API_KEY=votre_clé_api_langsmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Reflection Agent
```

## 7. Ajout de .gitignore

Créez un fichier `.gitignore` pour éviter de versionner des fichiers sensibles :

```bash
cat > .gitignore << EOF
__pycache__/
docker-compose.yml
venv/
.venv/
.env
EOF
```

## 8. Configuration de VS Code

### Installation des extensions recommandées

Dans VS Code, installez les extensions suivantes :
- Python (Microsoft)
- Pylance
- Python Indent
- Python Docstring Generator
- Black Formatter

### Configuration des tâches VS Code

1. Créez un dossier `.vscode` à la racine du projet
2. Créez un fichier `tasks.json` dans ce dossier :

```bash
mkdir -p .vscode
```

Contenu du fichier `.vscode/tasks.json` :

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Main",
            "type": "shell",
            "command": "poetry run python main.py",
            "group": {
                "kind": "build",
                "isDefault": true
            }
        },
        {
            "label": "Format Code",
            "type": "shell",
            "command": "poetry run black . && poetry run isort .",
            "problemMatcher": []
        }
    ]
}
```

## Exécution du projet

Une fois tous les fichiers configurés, vous pouvez exécuter le projet :

```bash
# Via le terminal
poetry run python main.py

# Ou via VS Code
# Appuyez sur Cmd+Shift+P puis tapez "Tasks: Run Task" et sélectionnez "Run Main"
```

## 11. Dépannage des problèmes courants

### Erreur liée à l'architecture

Si vous rencontrez une erreur du type:

```
ImportError: dlopen(...): tried: '...' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64'))
```

Cela signifie que le package a été compilé pour une architecture différente de celle de votre Mac. Solutions :

```bash
# Supprimez l'environnement virtuel actuel
poetry env remove python

# Assurez-vous d'avoir Python 3.11 pour votre architecture (Intel ou Apple Silicon)
brew install python@3.11

# Recreez l'environnement
poetry env use python3.11
poetry install --no-root
```

### Erreur "No module named 'grandalf'"

Si vous rencontrez cette erreur lors de la visualisation du graphe :


```bash
# Installez le module manquant
poetry add grandalf
```

### Erreur "No file/folder found for package reflectionagent"

Ajoutez `package-mode = false` dans la section `[tool.poetry]` de votre fichier pyproject.toml ou utilisez l'option `--no-root` lors de l'installation :

```bash
poetry install --no-root
```

## Utilisation avancée - Modification des paramètres de l'agent

Pour ajuster le comportement de l'agent, vous pouvez :

1. Modifier le nombre d'itérations de réflexion (actuellement 6) dans la fonction `should_continue`
2. Personnaliser les prompts de génération et de réflexion dans `chains.py`
3. Changer le modèle utilisé (remplacer "o4-mini" par un autre modèle OpenAI compatible)

---

Ce guide complet devrait vous permettre de configurer et d'exécuter votre agent de réflexion sur Mac sans rencontrer les erreurs courantes. N'hésitez pas à explorer davantage les possibilités offertes par LangChain et LangGraph pour créer des agents plus sophistiqués.