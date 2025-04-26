# Tutoriel : Installation propre de Homebrew et Poetry sur Mac

Ce guide vous aidera à installer correctement Homebrew et Poetry sur macOS, en vous assurant que tout est configuré pour votre architecture matérielle (Intel ou Apple Silicon).

## Installation de Homebrew

Homebrew est un gestionnaire de paquets pour macOS qui facilite l'installation de logiciels.

### 1. Désinstaller une version existante (si nécessaire)

Si vous avez déjà une version de Homebrew qui pose problème :

```bash
# Exécuter le script de désinstallation
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"

# Si certains fichiers persistent, essayez avec sudo
sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

### 2. Installer Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 3. Configurer l'environnement

Après l'installation, suivez les instructions affichées dans le terminal.

- Pour Mac Intel, généralement :
  ```bash
  eval "$(/usr/local/bin/brew shellenv)"
  echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
  ```

- Pour Mac Apple Silicon (ARM64), généralement :
  ```bash
  eval "$(/opt/homebrew/bin/brew shellenv)"
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
  ```

### 4. Vérifier l'installation

```bash
# Vérifier le chemin d'installation
which brew

# Vérifier l'architecture
brew config | grep CPU
```

## Installation de Poetry

Poetry est un outil de gestion de dépendances et de packaging pour Python.

### 1. Installer Poetry via Homebrew

```bash
brew install poetry
```

### 2. Vérifier l'installation

```bash
which poetry
poetry --version
```

## Configuration d'un projet Python avec Poetry

### 1. Installer la version Python requise

Si votre projet nécessite une version spécifique de Python :

```bash
# Pour Mac Apple Silicon
brew install python@3.11  # Remplacez 3.11 par la version souhaitée

# Pour vérifier les versions Python disponibles
ls /opt/homebrew/bin/python*  # Sur Apple Silicon
ls /usr/local/bin/python*     # Sur Intel
```

Vous pouvez également utiliser une version Python préinstallée :

```bash
# Trouver les chemins des versions Python existantes
which python3.11
find /Library/Frameworks/Python.framework/Versions -name "python*"
```

### 2. Initialiser ou configurer un projet Poetry

Dans votre dossier de projet :

```bash
# Pour un nouveau projet
poetry new nom-du-projet

# Pour un projet existant
cd chemin/vers/projet
```

### 3. Spécifier la version Python à utiliser

```bash
# Utiliser le chemin complet
poetry env use /chemin/vers/python3.x

# Ou si la commande est dans votre PATH
poetry env use python3.x
```

### 4. Installer les dépendances

```bash
poetry install
```

### 5. Vérifier l'environnement

```bash
# Vérifier l'architecture et la version Python
poetry run python -c "import platform; print(f'Architecture: {platform.machine()}, Python: {platform.python_version()}')"
```

## Configuration de VS Code pour déboguer

1. Sélectionner l'interpréteur Python :
   - `Cmd+Shift+P`
   - "Python: Select Interpreter"
   - Choisir l'interpréteur de votre environnement Poetry

2. Configurer le débogueur (`launch.json`) :
   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python: Fichier Courant",
               "type": "python",
               "request": "launch",
               "program": "${file}",
               "console": "integratedTerminal",
               "justMyCode": true
           }
       ]
   }
   ```

## Problèmes courants et solutions

1. **Erreur d'architecture incompatible** : Assurez-vous que Python et les bibliothèques sont installés pour la bonne architecture (ARM64 pour Apple Silicon).

2. **Module introuvable** : Vérifiez que vous exécutez votre code dans l'environnement Poetry avec `poetry run python`.

3. **Erreur de version Python** : Assurez-vous que les contraintes de version dans `pyproject.toml` sont compatibles avec la version Python que vous utilisez.

4. **Problèmes de permissions** : Utilisez `sudo` si nécessaire pour les opérations nécessitant des privilèges d'administrateur.

Ce tutoriel vous permettra d'avoir un environnement de développement propre et fonctionnel avec Homebrew et Poetry sur macOS, quelle que soit votre architecture matérielle.