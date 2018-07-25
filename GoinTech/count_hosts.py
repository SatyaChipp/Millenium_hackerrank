import json
import re
from collections import Counter

def get_hostnames_count(filename):
    with open(r'{}\{}'.format("********\\", filename), 'r') as fi:
        hostname_list = []
        for line in fi:
            hostname_list.append(line.split(' ')[0])
        counts_unique = Counter(hostname_list)
        with open(r'records_{}.txt'.format(str(filename.split('.')[0])), 'w+') as fiw:
            for k in counts_unique:
                str_ = '{} {}'.format(k, counts_unique[k])
                fiw.write(str_)
