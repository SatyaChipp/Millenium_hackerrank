import json
import re

def conect(filename):
    with open(r'{}\{}'.format("*******\\", filename), 'r') as fi:
        quoted = re.compile('"[^"]*"')
        set_gifs = set()
        for line in fi:
            value = quoted.findall(line)[0]
            list_req_details = value.replace('"', '').split(' ')
            print(list_req_details)
            if list_req_details[0] == 'GET' and list_req_details[1].endswith('.gif'):
                file_list = list_req_details[1].split('/')
                set_gifs.add(file_list[-1])
        print(r'gifs_{}.txt'.format(str(filename.split('.')[0])))
        with open(r'gifs_{}.txt'.format(str(filename.split('.')[0])), 'w') as fiw:
            for item in set_gifs:
                fiw.write(item)
