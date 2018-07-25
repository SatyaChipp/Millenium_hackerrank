# read the string filename

from collections import Counter
filename = input()

def create_file(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        file = open(filename, 'w')
        #we can write some data t file and test

def get_timestamps(filename):
    create_file(filename)
    with open(r'{}'.format(filename), 'r') as fi:
        set_timestamps = list()
        for line in fi:
            brackets_ = re.match(r"[^[]*\[([^]]*)\]", line).groups()[0].split(' ')[0]
            set_timestamps.append(brackets_)
        counter = Counter(set_timestamps)
        create_file()
        with open(r'req_{}.txt'.format(str(filename.split('.')[0])), 'w') as fiw:
            for key, value in counter.items():
                if value>1:
                    fiw.write(key)
                    print(key)
