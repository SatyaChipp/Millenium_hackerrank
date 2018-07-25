#!/usr/bin/python

# --	What if we want this system to quickly iterate over all historical blocks
# --	What if we want this system to run in real time as blocks coming in

"""
This is a disjoint-set data structure problem - (Disjoint sets: Keeps track of elements, it keeps track of a set of elements
partitioned into a number of disjoint (non-overlapping) subsets)

Some of the possible implementations to form address clusters are in Cluster_DisjointSets1, Cluster_DisjointSets2 and Cluster_DisjointSets3.

We can also use Union find for the same.
For very large n (or if wide/huge clusters are formed- we), we can implement union find weighted path compression technique
"""

import json
import logging
import os
import timeit

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(logging.Formatter("[%(asctime)s] (%(levelname)s) %(message)s"))
# logger.addHandler(handler)


class Cluster_DisjointSets1(object):

    def __init__(self):
        self.cluster_sets = []

    def parse_block_files(self):
        blocktestfiles = "{}\{}".format(os.getcwd(), "cluster_test\\")
        cluster_list = []
        for bfile in os.listdir(blocktestfiles):
            if bfile.endswith(".json"):
                # logger.info("Block data file : {}".format(bfile))
                print("Block data file:  {}".format(bfile))
                with open(r'{}\{}'.format(blocktestfiles, bfile), 'r') as bjson:
                    blockdata = json.loads(bjson.read())
                    cluster_list = self.iterate_block(blockdata) #lets keep the last set of clusters
        return {str(ind+1): value for ind, value in enumerate(cluster_list)} #labelling the clusters

    def iterate_block(self, blockdata): #iterate over each block -- n blocks
        data_=[]
        for txn in blockdata['txs']: # list of dicts - t transactions
            # logger.info("Block transaction hash: {}".format(txn['hash']))
            inputs_ = []
            for item in txn['inputs']: #item is a dict here
                try:
                    inputs_.append(item['coin']['address'])
                except KeyError:
                    if item['address']:
                        inputs_.append(item['address'])
            if len(inputs_) != 0:
                data_.append(inputs_)
        return self.union_(data_)
        #set is implemented as a hash table. So you can expect to lookup/insert/delete in O(1) average.

    def union_(self, txn_input_lis):
        lis = map(set, txn_input_lis) #map input txns for each block to set - remove duplicates
        # logger.info("Transaction inputs for this block  {}".format(list(lis)))
        for item in lis:
            temp = []
            for s in self.cluster_sets:
                if not s.isdisjoint(item):
                    item = s.union(item)
                else:
                    temp.append(s)
            temp.append(item)
            self.cluster_sets = temp
        return self.cluster_sets

    def check_timeit(self):
        from code_imports_timeit import code1, imports1
        return ("Time: %s"%timeit.timeit(setup=imports1,
                                         stmt=code1,
                                         number=1000000))

if __name__ == '__main__':
    ufo = Cluster_DisjointSets1()
    print(ufo.parse_block_files())
    print(ufo.check_timeit())
