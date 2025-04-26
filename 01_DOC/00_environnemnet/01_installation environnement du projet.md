# Guide complet: Environnement VS Code pour projets LangChain/LangGraph sur Mac M1/M2

Ce guide détaillé vous aidera, même si vous êtes débutant, à configurer correctement un environnement de développement pour vos projets LangChain et LangGraph sur Mac avec puce Apple Silicon (M1, M2, M3), en utilisant Poetry et VS Code.

## 1. Préparation de l'environnement

### Vérifier votre installation Python

Avant de commencer, assurez-vous d'avoir une version récente de Python installée:

```bash
python3 --version
```

Si nécessaire, installez Python via Homebrew:

```bash
brew install python
```

### Désactiver tout environnement Conda actif

Si vous utilisez Conda, assurez-vous de désactiver l'environnement base pour éviter les conflits:

```bash
conda deactivate
```

Votre terminal ne devrait plus afficher le préfixe `(base)`.

## 2. Installation et configuration de Poetry

### Installer Poetry

Installez Poetry si ce n'est pas déjà fait:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Ajoutez Poetry à votre PATH en ajoutant cette ligne à votre fichier `.zshrc` ou `.bash_profile`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Puis rechargez votre shell:

```bash
source ~/.zshrc  # ou source ~/.bash_profile
```

### Configurer Poetry pour utiliser un environnement local

Configurez Poetry pour créer les environnements virtuels directement dans le dossier du projet, ce qui est crucial pour le bon fonctionnement du débogueur VS Code:

```bash
poetry config virtualenvs.in-project true
```

## 3. Création d'un nouveau projet

### Créer le dossier du projet

```bash
mkdir mon-projet-langchain
cd mon-projet-langchain
```

### Initialiser un projet Poetry

```bash
poetry init
```

Suivez les instructions pour configurer votre projet. Pour les débutants, vous pouvez accepter les valeurs par défaut et les modifier plus tard dans le fichier `pyproject.toml`.

## 4. Configuration de l'environnement virtuel

### Créer manuellement un environnement virtuel

Cette étape est **cruciale** pour éviter les problèmes avec le débogueur VS Code sur Mac M1/M2:

```bash
# Créer un environnement virtuel standard
python3 -m venv .venv

# Dire à Poetry d'utiliser cet environnement
poetry env use .venv/bin/python3
```

### Activer l'environnement

```bash
source .venv/bin/activate
```

Votre terminal devrait maintenant afficher le préfixe `(.venv)`.

## 5. Installation des packages pour LangChain et LangGraph

Installez les dépendances nécessaires:

```bash
# Packages principaux
poetry add langchain langchain-openai langgraph grandalf

# Outils supplémentaires
poetry add python-dotenv

# Dépendances de développement
poetry add black isort --group dev
```

Cette commande mettra à jour automatiquement `pyproject.toml` et créera un fichier `poetry.lock` qui verrouille les versions exactes des packages.

## 6. Configuration de VS Code

### Installer les extensions VS Code

Ouvrez VS Code et installez les extensions suivantes:
- Python
- Pylance
- Python Environment Manager
- Python Debugger

### Ouvrir le projet dans VS Code

```bash
code .
```

### Sélectionner l'interpréteur Python

1. Appuyez sur `Cmd+Shift+P`
2. Tapez "Python: Select Interpreter"
3. Sélectionnez l'interpréteur dans `.venv/bin/python`

### Configurer le débogueur VS Code

Créez un dossier `.vscode` et un fichier `launch.json` à l'intérieur:

```bash
mkdir -p .vscode
```

Créez un fichier `.vscode/launch.json` avec le contenu suivant:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Fichier courant",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": false,
            "python": "${workspaceFolder}/.venv/bin/python",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

## 7. Configuration des variables d'environnement

Créez un fichier `.env` à la racine du projet:

```bash
touch .env
```

Ajoutez vos clés API dans ce fichier:

```
OPENAI_API_KEY=votre_clé_api_openai
LANGCHAIN_API_KEY=votre_clé_api_langsmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Mon_Projet_LangChain
```

## 8. Configuration de Git

### Ajouter un fichier .gitignore

```bash
cat > .gitignore << EOF
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.env
.venv/
venv/
ENV/
.idea/
.vscode/*
!.vscode/launch.json
!.vscode/settings.json
.DS_Store
*.log
.pytest_cache/
EOF
```

### Initialiser Git (optionnel)

```bash
git init
git add .
git commit -m "Configuration initiale du projet"
```

## 9. Créer un exemple de code LangChain

Créez un fichier `main.py` à la racine du projet:

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

# Charger les variables d'environnement
load_dotenv()

# Vérifier si la clé API est disponible
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY n'est pas définie dans le fichier .env")

# Configurer le modèle
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Créer une chaîne simple
prompt = ChatPromptTemplate.from_template("Explique {concept} comme si j'avais 5 ans.")
chain = prompt | llm | StrOutputParser()

# Exécuter la chaîne
result = chain.invoke({"concept": "l'intelligence artificielle"})
print(result)
```

## 10. Exécution du projet

### Exécuter via Poetry

```bash
poetry run python main.py
```

### Exécuter via VS Code

1. Ouvrez `main.py` dans VS Code
2. Appuyez sur `F5` ou cliquez sur le bouton "Play" dans le menu de débogage

## 11. Gestion de l'environnement

### Mettre à jour les dépendances

```bash
poetry update
```

### Supprimer l'environnement virtuel (si nécessaire)

Si vous devez recréer l'environnement depuis le début:

```bash
# Désactiver l'environnement actif
deactivate

# Supprimer l'environnement
rm -rf .venv

# Recréer l'environnement
python3 -m venv .venv
poetry env use .venv/bin/python3
poetry install
```

## Résolution des problèmes courants

### Le débogueur VS Code ne fonctionne pas

Vérifiez que:
1. `virtualenvs.in-project` est configuré sur `true` (`poetry config --list`)
2. Vous utilisez un environnement venv créé manuellement (pas uniquement via Poetry)
3. Le chemin de l'interpréteur dans `launch.json` est correct

### Problèmes de dépendances sur M1/M2

Si vous rencontrez des problèmes avec certaines bibliothèques:

```bash
# Forcer l'installation avec pip à l'intérieur de l'environnement Poetry
poetry run pip install --force-reinstall package-problématique
```

