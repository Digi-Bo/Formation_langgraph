
1. Pour activer l'environnement virtuel créé par Poetry, utilisez  :
   ```bash
   poetry env use python
   poetry env info
   ```
   Puis (selon votre système d'exploitation) :
   ```bash
   # Sur Unix/Linux/macOS
   source $(poetry env info --path)/bin/activate
   
   # Sur Windows (PowerShell)
   & $(poetry env info --path)/Scripts/Activate.ps1
   ```


# Pour installer un nouveau package
Exemple :  `langchain_core` :
   ```bash
   poetry add langchain_core
   ```

Alternativement, vous pouvez simplement exécuter des commandes dans l'environnement sans l'activer explicitement :
```bash
poetry run python chains.py
```

Ou pour installer le package sans activer l'environnement :
```bash
poetry add langchain_core
```

