
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
     DAG_labels=[DAG_vertices_with_labels[j][1:] for j in range(num_vertices)]
     DAG_edges=DAGs[i][1]
     S0=nx.DiGraph()
     S0.add_nodes_from(DAG_vertices)
     S0.add_edges_from(DAG_edges)
     Sorted_vertices=list(nx.topological_sort(S0))
     Sorted_labels=[DAG_labels[DAG_vertices.index(Sorted_vertices[v])] for v in range(num_vertices)]
     P=[]
     for u in range(num_vertices):
         A=[[0]*(k+1) for _ in range(num_vertices)]
         A[u][0]=1
         for v in range(num_vertices):
             for j in range(k):
                if A[v][j]>0:
                    for w in range(num_vertices):
                     if [Sorted_vertices[v], Sorted_vertices[w]] in DAG_edges:
                        A[w][j+1]= A[w][j+1]+A[v][j]
         B=[]
         for v in range(num_vertices):
          path_count = sum(A[v][dist] for dist in range(0, k + 1))
          B.extend([i for i in Sorted_labels[v]] * path_count)
         P.append(sorted(B))
     P_Total.append(P)
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

