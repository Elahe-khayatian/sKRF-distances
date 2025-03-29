import sKfunctions
import argparse
import json
"""
sK-RFmeasures.py computes pairwise (modified) simple K-RF distances of all labeled DAGs in an input file in which each DAG is represented by a list of directed edges and a list of  nodes with its label.
The command line for the execution is 'python3 sK-RFmeasures.py inputfile k m n', where one needs to set m=0 for simple K-RF and m=1 for modified simple K-RF; additionally, n=1 is for normalized distance computation and n=0 is for computation without normalization. 
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find pairwise (modified) simple k-RF scores of a set of DAGs.')
    parser.add_argument('inputfile')
    parser.add_argument('k')
    parser.add_argument('m')
    parser.add_argument('n')
    args = parser.parse_args()
    DAG_file = open(args.inputfile)
    DAGs=json.load(DAG_file)
    partitions=sKfunctions.getpartitions(DAGs, int(args.k), int(args.m))
    if int(args.n)==0:
     pairwise_distances=sKfunctions.get_skDistance(partitions)
    if int(args.n)==1:
     pairwise_distances=sKfunctions.get_normalized_skDistance(partitions,DAGs,int(args.m))
    with open("pairwise_distances", "w") as fp:
       json.dump(pairwise_distances, fp)
       
       
