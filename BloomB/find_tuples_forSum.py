##find tupels that satisfy for below -- can be repeated
#2x+3y+7z = 10

from collections import defaultdict
def func_combs(list_, X=10):
    # dic = defaultdict(int)
    # for i in [2, 3, 7]:
    #     # if isinstance(X/i, float):
    #     dic[i] = range(X//i)
    # zip_list = zip(dic.values())
    # print(list(zip_list))
    sum_list = [(a, b, c) for a in range(10//2 + 1) for b in range(10//3 + 1) for c in range(10//7 + 1) if 2*a+3*b+7*c==X]
    for a in range(10//2 + 1):
        for b in range(10//3 + 1):
            for c in range(10//7 + 1):
                # print(a*2+b*3+c*7)
                if a*2+b*3+c*7 == 10:
                    print(a, b, c)

    print(sum_list)
func_combs([2, 3, 7], 10)
