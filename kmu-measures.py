import kmufunctions
import argparse
import json
"""
kmu-measures.py computes pairwise (k,\mu)-distances of all DAGs in an input file in which each DAG is represented by a list of directed edges and a list of  nodes with its label.
The command line for the execution is 'python3 kmu-measures.py inputfile k'.
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find pairwise (k,\mu)-scores of a set of DAGs.')
    parser.add_argument('inputfile')
    parser.add_argument('k')
    #parser.add_argument( action='store_true')
    args = parser.parse_args()
    DAG_file = open(args.inputfile)
    #DAGs=functions.getDAGs(DAG_file)
    partitions=kmufunctions.getpartitions(DAG_file, int(args.k))
    #if args.rooted:
    pairwise_distances=kmufunctions.getkmuDistance(partitions)
    #else:
        #pairwise_distances=functions.getkRFmeasure_unrooted(partitions)
    with open("pairwise_distances", "w") as fp:
       json.dump(pairwise_distances, fp)
       
