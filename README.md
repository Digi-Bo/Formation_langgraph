# Agent de Réflexion avec LangGraph 🦜🕸️

Implémentation d'un agent de réflexion sophistiqué utilisant LangGraph et LangChain, conçu pour générer des réponses de haute qualité grâce à l'auto-réflexion et l'amélioration itérative.
Ce projet démontre les capacités avancées d'un agent d'IA en utilisant les mécanismes de contrôle de flux de pointe de LangGraph pour l'auto-réflexion et le raffinement des réponses.

# Reflexion Agent with LangGraph 🦜🕸️

*Implementation of a sophisticated Reflexion agent using LangGraph and LangChain, designed to generate high-quality responses through self-reflection and iterative improvement.
This project demonstrates advanced AI agent capabilities using LangGraph's state-of-the-art control flow mechanisms for self-reflection and response refinement.*

---

# Fonctionnalités

* **Auto-réflexion** : Implémente des mécanismes sophistiqués de réflexion pour améliorer les réponses
* **Raffinement itératif** : Utilise une approche basée sur les graphes pour améliorer progressivement les réponses
* **Prêt pour la production** : Conçu avec la scalabilité et les applications du monde réel à l'esprit
* **Recherche intégrée** : Exploite la recherche Tavily pour une précision accrue des réponses
* **Sortie structurée** : Utilise des modèles Pydantic pour une gestion fiable des données

# Features

* *__Self-Reflection__*: *Implements sophisticated reflection mechanisms for response improvement*
* *__Iterative Refinement__*: *Uses a graph-based approach to iteratively enhance responses*
* *__Production-Ready__*: *Built with scalability and real-world applications in mind*
* *__Integrated Search__*: *Leverages Tavily search for enhanced response accuracy*
* *__Structured Output__*: *Uses Pydantic models for reliable data handling*

---

# Architecture

L'agent utilise une architecture basée sur les graphes avec les composants suivants :
* **Point d'entrée** : Nœud `draft` pour la génération initiale de la réponse
* **Nœuds de traitement** : `execute_tools` et `revise` pour le raffinement
* **Nombre maximum d'itérations** : 2 (configurable)
* **Composants de la chaîne** : Premier répondeur et réviseur utilisant GPT-4
* **Intégration d'outils** : Recherche Tavily pour la recherche web

# Architecture

*The agent uses a graph-based architecture with the following components:*
* *__Entry Point__*: *`draft` node for initial response generation*
* *__Processing Nodes__*: *`execute_tools` and `revise` for refinement*
* *__Maximum Iterations__*: *2 (configurable)*
* *__Chain Components__*: *First responder and revisor using GPT-4*
* *__Tool Integration__*: *Tavily Search for web research*

---

# Variables d'environnement

Pour exécuter ce projet, vous devrez ajouter les variables d'environnement suivantes à votre fichier .env :

```
OPENAI_API_KEY=votre_clé_api_openai_ici
TAVILY_API_KEY=votre_clé_api_tavily_ici
LANGCHAIN_API_KEY=votre_clé_api_langchain_ici  # Optionnel, pour le traçage
LANGCHAIN_TRACING_V2=true                      # Optionnel
LANGCHAIN_PROJECT=reflexion agent              # Optionnel
```

**Remarque importante** : Si vous activez le traçage en définissant `LANGCHAIN_TRACING_V2=true`, vous devez disposer d'une clé API LangSmith valide définie dans `LANGCHAIN_API_KEY`. Sans une clé API valide, l'application générera une erreur. Si vous n'avez pas besoin de traçage, supprimez simplement ou commentez ces variables d'environnement.

# Environment Variables

*To run this project, you will need to add the following environment variables to your .env file:*

```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here  # Optional, for tracing
LANGCHAIN_TRACING_V2=true                      # Optional
LANGCHAIN_PROJECT=reflexion agent               # Optional
```

*__Important Note__: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error. If you don't need tracing, simply remove or comment out these environment variables.*

---

# Exécution en local

Clonez le projet :

```
git clone <url-du-dépôt>
cd reflexion-agent
```

Installez les dépendances :

```
poetry install
```

Démarrez l'agent :

```
poetry run python main.py
```

# Run Locally

*Clone the project:*

```
git clone <repository-url>
cd reflexion-agent
```

*Install dependencies:*

```
poetry install
```

*Start the agent:*

```
poetry run python main.py
```

---

# Configuration pour le développement

1. Obtenez vos clés API :
   * Plateforme OpenAI pour l'accès à GPT-4
   * Tavily pour les fonctionnalités de recherche
   * LangSmith (optionnel) pour le traçage
   
2. Copiez le fichier d'environnement exemple :

```
cp .env.example .env
```

3. Modifiez `.env` avec vos clés API

# Development Setup

*1. Get your API keys:*
   * *OpenAI Platform for GPT-4 access*
   * *Tavily for search functionality*
   * *LangSmith (optional) for tracing*
   
*2. Copy the example environment file:*

```
cp .env.example .env
```

*3. Edit `.env` with your API keys*

---

# Exécution des tests

Pour exécuter les tests, utilisez la commande suivante :

```
poetry run pytest . -s -v
```

# Running Tests

*To run tests, use the following command:*

```
poetry run pytest . -s -v
```

---

# Remerciements

Ce projet s'appuie sur :
* LangGraph pour le flux de contrôle de l'agent
* LangChain pour les interactions avec les LLM
* API Tavily pour les capacités de recherche web

# Acknowledgements

*This project builds upon:*
* *LangGraph for agent control flow*
* *LangChain for LLM interactions*
* *Tavily API for web search capabilities*

---

# Lexique

| Français | Anglais |
|----------|---------|
| Agent de Réflexion | Reflexion Agent |
| Auto-réflexion | Self-Reflection |
| Raffinement itératif | Iterative Refinement |
| Prêt pour la production | Production-Ready |
| Recherche intégrée | Integrated Search |
| Sortie structurée | Structured Output |
| Point d'entrée | Entry Point |
| Nœuds de traitement | Processing Nodes |
| Nombre maximum d'itérations | Maximum Iterations |
| Composants de la chaîne | Chain Components |
| Intégration d'outils | Tool Integration |
| Variables d'environnement | Environment Variables |
| Exécution en local | Run Locally |
| Configuration pour le développement | Development Setup |
| Exécution des tests | Running Tests |
| Remerciements | Acknowledgements |
| Flux de contrôle | Control flow |
| Interactions avec les LLM | LLM interactions |
| Capacités de recherche web | Web search capabilities |