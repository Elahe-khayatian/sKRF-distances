import kmufunctions
import sKfunctions
import argparse
import json
"""
kmu-measures.py computes pairwise simplified K-RF distances of all DAGs in an input file in which each DAG is represented by a list of directed edges and a list of  nodes with its label.
The command line for the execution is 'python3 sK-RFmeasures.py inputfile k'.
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find pairwise simplified k-RF scores of a set of DAGs.')
    parser.add_argument('inputfile')
    parser.add_argument('k')
    args = parser.parse_args()
    DAG_file = open(args.inputfile)
    partitions=sKfunctions.getpartitions(DAG_file, int(args.k))
    pairwise_distances=sKfunctions.getkmuDistance(partitions)
    with open("pairwise_distances_4newsecond", "w") as fp:
       json.dump(pairwise_distances, fp)
       
