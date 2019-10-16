"""
Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
##Solution 1
import sys
if __name__ == '__main__':
    L = []
    for _ in range(0, int(input())):
        user_input = input().split(' ')
        command = user_input.pop(0)
        if len(user_input) > 0:
            if 'insert' == command:
                eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
            else:
                eval("L.{0}({1})".format(command, user_input[0]))
        elif command == 'print':
            print(L)
        else:
            eval("L.{0}()".format(command))

##Solution 2
import sys
if __name__ == '__main__':
    N = int(input())
    output_list = []
    while 1:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break
        if not line:
            break
        line = line.strip().lower()
        
        if line.startswith('insert'):
            inp = line.replace('insert ', '').split(' ')
            ##or push string into list and pop last two items
            output_list.insert(int(inp[0]), int(inp[1]))
        
        if line.startswith('print'):
            print(output_list)
        
        if line.startswith('remove'):
            if len(output_list) != 0:
                l = list(line)
            del output_list[int(l[-1])]
        
        if line.startswith('append'):
            l = list(line)
            output_list.append(int(l[-1])
        
        if line.startswith('sort'):
            if len(output_list) != 0:
                output_list.sort()
        
        if line.startswith('pop'):
            if len(output_list) != 0:
                output_list.pop()
        
        if line.startswith('reverse'):
            if len(output_list) != 0:
                output_list.reverse()
