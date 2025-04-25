from typing import List, Sequence

from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph

from chains import generate_chain, reflect_chain



REFLECT = "reflect"
GENERATE = "generate"

# Le nœud de génération :
def generation_node(state: Sequence[BaseMessage]):
    return generate_chain.invoke({"messages": state})


# Implémentons maintenant le nœud de réflexion :
def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflect_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]


# Initialisons maintenant notre graphe :
builder = MessageGraph()
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)


# Conditional Edge : Condition d'arrêt de la réflexion et du passage à l'étape suivante 
# Pourraît être un LLM, mais ici, on se contente de compter le nombre d'itération
def should_continue(state: List[BaseMessage]):
    if len(state) > 6:
        return END
    return REFLECT

# Maintenant, configurons les connexions entre nos nœuds :
builder.add_conditional_edges(GENERATE, should_continue)
builder.add_edge(REFLECT, GENERATE)

# Compilation
graph = builder.compile()


# visualiser notre graphe 
print(graph.get_graph().draw_mermaid())
graph.get_graph().print_ascii()

 

# pour exécuter notre graphe avec un tweet initial :
if __name__ == "__main__":
    print("Hello LangGraph") 
    inputs = HumanMessage(content="""Améliore ce tweet : :"
                                    @LangChainAI
La nouvelle fonctionnalité "Tool Calling" est vraiment super !

Après une longue attente, elle est enfin là, rendant l'implémentation d'agents à travers différents modèles avec appel de fonctions incroyablement facile. 

J'ai réalisé une vidéo à propos de votre dernier article de blog. 

                                  """)
    response = graph.invoke(inputs)
    print(response)