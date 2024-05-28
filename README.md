Kmu-measures.py computes pairwise (k,\mu)-distances of a set of DAGs in an input file.
kmufunction.py is the set of function required for running kmu-measures.py.
A sample DAG G in the input file is supposed to be represented by [[[v l(v)] for v in V(G)],[(u,v) for (u,v) in E(G)]]
The input file for kmu-measures.py needs to be a json file consisting of a list of DAGs in which each DAG is represented via a list of nodes with their labels and a list of edges.
