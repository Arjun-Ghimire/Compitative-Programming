""" Find out all possible values of (a,b,c,d,e) which are single digit natural numbers excluding 0,
which are such that a*b+c/d = 2+e. Treat each set (a,b.c.d.e) as a number abcde, report the final answer
as the sum of all such sets. 

For eg : If the possible values of set are (1,2,4,2,1) and (2,4,2,1,3) then report the answer as 12421 + 24213 = 36634
"""


def find_sum():
    mysum =0
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                for d in range(1,10):
                    for e in range(1,10):
                        if (a*b)+(c/d) == 2+e:
                            mysum = mysum+ int(str(a)+str(b)+str(c)+str(d)+str(e))
    

    return mysum


print("The sum is = {}".format(find_sum()))