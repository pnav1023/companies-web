import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from data import ceos, companies

st.title("Web of companies")

nodes = []
edges = []

for company in companies:
    if company["id"] == "":
        nodes.append(Node(id=company["label"],
                  label=company["label"]))
    else:   
        nodes.append(Node(id=company["id"],
                  label=company["label"]))
    
# edges.append(Edge(source="Apple",
#                   label="ceo",
#                   target="ceoApple"))

config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)