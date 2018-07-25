import networkx
import os
import json


class Cluster_DisjointSets3(object):
    def __init__(self):
        self.lists_ = []

    def parse_block_files(self):
        blocktestfiles = "{}\{}".format(os.getcwd(), "cluster_test\\")
        for bfile in os.listdir(blocktestfiles):
            if bfile.endswith(".json"):
                # logger.info("Block data file : {}".format(bfile))
                print("Block data file:  {}".format(bfile))
                with open(r'{}\{}'.format(blocktestfiles, bfile), 'r') as bjson:
                    self.iterate_block(json.loads(bjson.read()))
        return {str(ind+1): value for ind, value in enumerate(list(networkx.connected_components(self.network_graph(self.lists_))))} # #labelling the cluster


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

    @staticmethod
    def pairs(lst): # iterate over pairs in a list in a circular way
        i = iter(lst)
        first = prev = item = i.__next__()
        for item in i:
            yield prev, item
            prev = item
        yield item, first

    def network_graph(self, inputs):
        # Designing it as a connected-components problem in a graph. below uses networkx graph library
        gg = networkx.Graph()
        for sub_list in inputs:
            for edge in self.pairs(sub_list):
                gg.add_edge(*edge)
        return gg

    def check_timeit(self):
        import timeit
        from code_imports_timeit import code3, imports3
        return ("Time: %s"%timeit.timeit(setup=imports3,
                                         stmt=code3,
                                         number=1000000))

if __name__ == '__main__':
    ufo = Cluster_DisjointSets3()
    print(ufo.parse_block_files())
    print(ufo.check_timeit())


