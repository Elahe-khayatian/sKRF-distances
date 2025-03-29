import networkx as nx
def getpartitions(DAGs, k, m):
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
         if m==0:
          P.append(sorted(B))
         if m==1:
          a=S0.in_degree(Sorted_vertices[u])
          P.extend([sorted(B) for i in range(max(a,1))])
     P_Total.append(P)
    return(P_Total)



def get_skDistance(P_Total):
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

def get_normalized_skDistance(P_Total,DAGs,m):
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
    if m==0:
     d.append(d_k/(len(DAGs[i][0])+len(DAGs[j][0])))
    if m==1:
     S=[]
     for h in [i,j]:
      DAG_vertices_with_labels=DAGs[h][0]
      num_vertices=len(DAG_vertices_with_labels)
      DAG_vertices=[DAG_vertices_with_labels[j][0] for j in range(num_vertices)]
      S0=nx.DiGraph()
      S0.add_nodes_from(DAG_vertices)
      S0.add_edges_from(DAGs[i][1])
      s1=sum(max(S0.in_degree(v),1) for v in DAG_vertices)
      S.append(s1)
     d.append(d_k/(S[0]+S[1]))
  d_Total.append(d)
 return(d_Total)
