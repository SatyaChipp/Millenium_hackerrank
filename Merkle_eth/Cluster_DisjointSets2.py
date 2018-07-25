import json
import os
import timeit
from collections import defaultdict


class Cluster_DisjointSets2(object):
    def __init__(self):
        self.cluster_sets = []
        self.lists_ = []

    def parse_block_files(self):
        blocktestfiles = "{}\{}".format(os.getcwd(), "cluster_test\\")
        for bfile in os.listdir(blocktestfiles):
            if bfile.endswith(".json"):
                # logger.info("Block data file : {}".format(bfile))
                print("Block data file:  {}".format(bfile))
                with open(r'{}\{}'.format(blocktestfiles, bfile), 'r') as bjson:
                    blockdata = json.loads(bjson.read())
                    self.iterate_block(blockdata)
        return {str(ind+1): value for ind, value in enumerate(self.union_(self.lists_))} # #labelling the cluster

    def iterate_block(self, blockdata):
        data_=[]
        for txn in blockdata['txs']: # list of dicts
            # logger.info("Block transaction hash: {}".format(txn['hash']))
            inputs_ = set()
            for item in txn['inputs']: #item is a dict here
                try:
                    inputs_.add(item['coin']['address'])
                except KeyError:
                    if item['address']:
                        inputs_.add(item['address'])
            if len(inputs_) != 0:
                data_.append(inputs_)
        self.lists_.extend(data_)

    def union_(self, lsts):
        lis_sets = [set(lst) for lst in lsts if lst]
        merged = 1
        while merged:
            merged = 0
            clusters = []
            while lis_sets:
                common_ele, other_ele = lis_sets[0], lis_sets[1:]
                lis_sets = []
                for x in other_ele:
                    if x.isdisjoint(common_ele):
                        lis_sets.append(x)
                    else:
                        merged = 1
                        common_ele |= x
                clusters.append(common_ele)
            lis_sets = clusters
        return lis_sets

    def check_timeit(self):
        from code_imports_timeit import code2, imports2
        return ("Time: %s"%timeit.timeit(setup=imports2,
                                         stmt=code2,
                                         number=1000000))

if __name__ == '__main__':
    ufo = Cluster_DisjointSets2()
    print(ufo.parse_block_files())
    print(ufo.check_timeit())