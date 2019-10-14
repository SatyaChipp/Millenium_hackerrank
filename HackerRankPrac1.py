# -*- coding: utf-8 -*-
"""
HackerRank practice problems
Companies: Dialpad, etc
"""
"print odd numbers between l and r"
def oddNumbers(l, r):
    odd = []
    while l<=r:
        if l%2!=0:
            odd.append(l)
            l+=2
        elif l==0:
            l+=1
        else:
            l+=1
    return odd

"print multiples of x and y but not z and <=n"
def multiple(x, y, z, n):
    # Write your code here
    a = n//x if x!=0 else x
    b = n//y if y!=0 else y
    c = n//z if z!=0 else z
    mulx = [x*i for i in range(1, a+1)]
    muly = [y*i for i in range(1, b+1)]
    mulz = [z*i for i in range(1, c+1)]
    addxy = mulx + muly
    suby = list(set(addxy) - set(mulz))
    return sorted(suby)

"print reservations in second order not present in first order and "
def missingReservations(firstReservationList, secondReservationList):
    # Write your code here
    dict1 = {i[0]:i[1] for i in firstReservationList}
    dict2 = {i[0]:i[1] for i in secondReservationList}
    di3 = {item: dict2[item] for item in dict2.keys() if item not in dict1.keys()}
    return sorted(di3, key=di3.get, reverse=True) #gives a sorted list of sorted keys
    ##reverse is ascending order [256, 458, 1231]


if __name__ == '__main__':
    #print(oddNumbers(3,9))
    #print(multiple(3, 5, 10, 0))
    print(missingReservations([[1234,532632],[234,632633],[2354,732634],[1234,532632]],[[234,632633],[458,642633],[2354,732634],[256, 786545], [1231, 635468]]))
