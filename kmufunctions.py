import networkx as nx
import json
from tracemalloc import stop
def getpartitions(DAGs_file, k):
    DAGs=json.load(DAGs_file)
    P_Total=[]
    for i in range(len(DAGs)):
     DAG_vertices_with_labels=DAGs[i][0]
     num_vertices=len(DAG_vertices_with_labels)
     DAG_vertices=[DAG_vertices_with_labels[j][0] for j in range(num_vertices)]
     DAG_edges=DAGs[i][1]
     S0=nx.DiGraph()
     S0.add_nodes_from(DAG_vertices)
     S0.add_edges_from(DAG_edges)
     spl=nx.all_pairs_shortest_path_length(S0)
     dspl={x[0]:x[1] for x in spl}
     P=[]
     for i in range(num_vertices):
        L_D_k=DAG_vertices_with_labels[i][1:]
        for j in range(num_vertices):
          try:
           if dspl[DAG_vertices[i]][DAG_vertices[j]]<k+1:
             for p in nx.all_simple_paths(S0,DAG_vertices[i],DAG_vertices[j]):
                L_D_k.extend(DAG_vertices_with_labels[j][1:])
          except:
           stop          
        P.append(sorted(L_D_k))
     P_Total.append(P) 
    print(P_Total[0])
    return(P_Total)

def getkmuDistance(P_Total):
 d_Total=[]
 for i in range(len(P_Total)):
  d=[]
  P_Supp=[]
  for p in P_Total[i]:
    if p not in P_Supp:
       P_Supp.append(p)
  for j in range(len(P_Total)):
    d_k=len(P_Total[i])+len(P_Total[j])
    for p in P_Supp:
        if P_Total[i].count(p)> P_Total[j].count(p):
            d_k=d_k-2*(P_Total[j].count(p))
        else:
            d_k=d_k-2*(P_Total[i].count(p))
    d.append(d_k)
  d_Total.append(d)
 return(d_Total)
