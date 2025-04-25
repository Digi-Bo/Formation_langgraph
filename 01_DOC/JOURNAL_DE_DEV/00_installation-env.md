# Configuration d'un projet d'agent de réflexion avec LangChain et LangGraph sur VS Code (Mac)

Cet article vous guide à travers les étapes nécessaires pour configurer un projet d'agent de réflexion utilisant LangChain et LangGraph sur VS Code avec un Mac. Nous verrons comment créer l'environnement de développement, installer les dépendances nécessaires et préparer le projet pour l'implémentation de notre agent.

## Création du répertoire de projet

Pour commencer, nous allons créer un nouveau répertoire pour notre projet :

1. Ouvrez le Terminal sur votre Mac
2. Sur le bureau, créez un nouveau dossier nommé "ReflectionAgent" avec la commande `mkdir ~/Desktop/ReflectionAgent`
3. Naviguez dans ce répertoire en utilisant la commande `cd ~/Desktop/ReflectionAgent`

## Installation et configuration de Poetry avec Homebrew

Nous utiliserons Poetry pour gérer notre environnement virtuel et nos dépendances :

1. Si vous n'avez pas encore installé Homebrew, exécutez cette commande :
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Installez Poetry avec Homebrew :
   ```bash
   brew install poetry
   ```

3. Vérifiez que Poetry est correctement installé :
   ```bash
   poetry --version
   ```

## Initialisation du projet Poetry avec la bonne version Python

1. Dans le répertoire de votre projet, initialisez Poetry :
   ```bash
   cd ~/Desktop/ReflectionAgent
   poetry init
   ```

2. Lors de l'initialisation, acceptez les valeurs par défaut, mais quand on vous demande la version Python compatible, spécifiez :
   ```
   Compatible Python versions: >=3.9,<4.0
   ```
   
   > **Important** : Ne spécifiez pas ">=3.12" comme dans l'exemple précédent, car cette version n'est pas compatible avec les bibliothèques que nous allons utiliser.

3. Pour les dépendances et les dépendances de développement, choisissez de ne pas les ajouter interactivement (répondez "no"), nous les ajouterons séparément.

4. Confirmez la génération du fichier `pyproject.toml`

## Installation des dépendances

Maintenant, installons les packages requis pour notre projet :

```bash
poetry add python-dotenv
poetry add black isort
poetry add langchain
poetry add langchain-openai
poetry add langgraph
```

Si vous utilisez Python 3.12 et rencontrez des problèmes de compatibilité, vous pouvez créer un environnement avec Python 3.11 :

```bash
# Installer Python 3.11 si nécessaire
brew install python@3.11

# Indiquer à Poetry d'utiliser Python 3.11
poetry env use python3.11

# Puis installer les dépendances
poetry add python-dotenv black isort langchain langchain-openai langgraph
```

Ces commandes installent :
* `python-dotenv` pour charger les variables d'environnement
* `black` et `isort` pour le formatage du code
* `langchain` pour les fonctionnalités de base
* `langchain-openai` pour utiliser le modèle GPT-3.5
* `langgraph` (LangGraph) pour construire notre agent de réflexion

## Configuration de VS Code

Maintenant, configurons VS Code pour notre projet :

1. Lancez VS Code
2. Sélectionnez "File > Open..." et choisissez le répertoire "ReflectionAgent" créé précédemment
3. Dans VS Code, ouvrez un terminal intégré avec "Terminal > New Terminal"
4. Configurez l'interpréteur Python pour utiliser l'environnement Poetry :
   - Appuyez sur `Cmd+Shift+P` pour ouvrir la palette de commandes
   - Tapez "Python: Select Interpreter" et sélectionnez cette option
   - Choisissez l'interpréteur dans l'environnement virtuel Poetry (généralement indiqué par "(Poetry)")

## Installation des extensions VS Code recommandées

Pour améliorer votre expérience de développement, installez ces extensions VS Code :

1. Python (Microsoft) - Support complet pour Python
2. Pylance - Fonctionnalités avancées pour Python
3. Python Indent - Indentation automatique
4. Python Docstring Generator - Création facilitée de docstrings
5. Black Formatter - Intégration de Black pour le formatage

Pour installer ces extensions :
- Cliquez sur l'icône Extensions dans la barre latérale (ou utilisez `Cmd+Shift+X`)
- Recherchez chaque extension et cliquez sur "Install"

## Création du fichier de variables d'environnement

Créons un fichier `.env` pour stocker nos clés API :

1. Dans VS Code, créez un nouveau fichier en cliquant sur l'icône "New File" dans l'explorateur
2. Nommez-le `.env` et ajoutez les variables d'environnement suivantes :

```plaintext
OPENAI_API_KEY=votre_clé_api_openai
LANGCHAIN_API_KEY=votre_clé_api_langsmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Reflection Agent
```

Ces variables permettent :
* L'authentification auprès d'OpenAI
* L'utilisation de LangSmith pour le traçage (tracing)
* La définition du nom du projet dans LangSmith

## Création du fichier principal

Créons maintenant notre fichier Python principal :

1. Dans VS Code, créez un nouveau fichier Python en cliquant sur l'icône "New File"
2. Nommez-le `main.py` et ajoutez le code de base suivant :

```python
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

if __name__ == "__main__":
    print("Hello LangGraph!")
```

3. Pour exécuter le fichier, cliquez sur le bouton de lecture (▶️) en haut à droite ou utilisez le terminal intégré avec la commande `poetry run python main.py`

## Configuration des tâches VS Code (optionnel)

Pour faciliter l'exécution de commandes fréquentes, configurons des tâches VS Code :

1. Créez un dossier `.vscode` à la racine du projet si ce n'est pas déjà fait
2. Créez un fichier `tasks.json` dans ce dossier avec le contenu suivant :

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

Ces tâches peuvent être exécutées avec `Cmd+Shift+P` puis en tapant "Tasks: Run Task".

## Vérification de la configuration

Pour confirmer que notre configuration est correcte :

1. Dans le terminal intégré de VS Code, exécutez `poetry show` pour afficher les dépendances installées
2. Vérifiez que les versions sont correctes :
   * langchain version 0.3.24 (ou la plus récente disponible)
   * langgraph version 0.3.34 (ou la plus récente disponible)
3. Exécutez le fichier `main.py` pour vérifier que tout fonctionne correctement avec la commande :
   ```bash
   poetry run python main.py
   ```

## Dépannage des problèmes courants

Si vous rencontrez des problèmes de compatibilité, voici quelques astuces :

1. Si le message d'erreur indique un problème de versions Python, modifiez manuellement le fichier `pyproject.toml` :
   ```toml
   requires-python = ">=3.9,<4.0"  # Au lieu de ">=3.12"
   ```

2. Si vous avez déjà un environnement virtuel créé avec une version incompatible, supprimez-le et créez-en un nouveau :
   ```bash
   poetry env remove python
   poetry env use python3.11  # Ou toute autre version compatible entre 3.9 et 3.11
   ```

3. En dernier recours, vous pouvez réinitialiser complètement le projet :
   ```bash
   rm -rf .venv poetry.lock pyproject.toml
   # Puis recommencez l'initialisation avec les bonnes versions
   ```






--- 

# Créer une tâche personnalisée  à partir d'un template

Ces tâches peuvent être crées puis exécutées avec `Cmd+Shift+P` puis en tapant "Tasks: Run Task".


Vous avez ouvert la palette de commandes et vous êtes arrivé à l'étape de sélection d'un type de tâche. Cette liste montre les différents systèmes de tâches disponibles dans VS Code.

Pour configurer la tâche personnalisée que nous voulons utiliser, suivez ces étapes :

1. Sélectionnez "Afficher toutes les tâches..." (ou "Show all tasks..." si votre interface est en anglais) dans cette liste

2. Si aucune tâche n'est encore configurée, VS Code vous proposera de créer un fichier `tasks.json`. Choisissez alors l'option "Create tasks.json file from template" (ou équivalent en français)

3. Ensuite, sélectionnez "Others" ou "Autres" pour créer une tâche personnalisée

4. VS Code créera alors un fichier `tasks.json` dans le dossier `.vscode` avec une configuration de base

5. Remplacez le contenu de ce fichier par notre configuration :

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

6. Sauvegardez le fichier (`Cmd+S`)

7. Maintenant, pour exécuter la tâche, appuyez à nouveau sur `Cmd+Shift+P` et tapez "Tasks: Run Task"

8. Vous devriez voir "Run Main" et "Format Code" dans la liste des tâches disponibles






# La commande directe dans le terminal

1. Ouvrez un terminal dans VS Code avec `Terminal > New Terminal`
2. Exécutez votre programme avec la commande :
   ```bash
   poetry run python main.py
   ```

Cette méthode directe fonctionne toujours et est souvent plus rapide pour les tests simples.