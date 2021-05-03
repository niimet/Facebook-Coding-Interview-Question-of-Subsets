# This codes displays subsets of any set

def ul(n):
    length = 2**(len(n))
    sublists = [0]*length
    sublists[0] = []

    i = 0
    for s in n:
        for r in range(2**i,2**(i+1)):
            sublists[r] = [s] + sublists[r-2**i]

        i += 1


    return sublists

mylist = [1,2,3,4]
print(ul(mylist))
