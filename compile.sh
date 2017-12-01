ocamlc graph.ml
ocamlc graph.cmo flow_network.ml
ocamlc str.cma graph.cmo flow_network.cmo main.ml -o flow
