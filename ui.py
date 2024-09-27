import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from data import ceos, companies

st.title("Web of companies")

nodes = []
edges = []

topTen = 0
for company in companies:
    if topTen == 10: break

    topTen += 1
    if company["id"] == "":
        nodes.append(Node(id=company["label"],
                          color="red",
                          label=company["label"]))
    else:   
        nodes.append(Node(id=company["id"],
                          color="red",
                          label=company["label"]))

topTen = 0
for ceo in ceos:
    if topTen == 10: break

    topTen += 1
    if ceo["companyTicker"] == "":
        nodes.append(Node(id=ceo["label"],
                  label=ceo["label"]))
    else:
        nodes.append(Node(id=ceo["id"],
                  label=ceo["label"]))
        edges.append(Edge(source=ceo["companyTicker"],
                          label="ceo",
                          target=ceo["id"]))

config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=True,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)