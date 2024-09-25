import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.title("Web of companies")

nodes = []
edges = []

nodes.append(Node(id="Amazon",
                  label="Amazon"))
nodes.append(Node(id="Apple",
                  label="Apple"))
nodes.append(Node(id="ceoApple",
                  label="tim cook"))
edges.append(Edge(source="Apple",
                  label="ceo",
                  target="ceoApple"))

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