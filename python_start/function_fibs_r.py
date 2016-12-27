#! /usr/bin/env python
#coding = utf-8

def fibs(n):
    """
    This is Fibonacci by recursion.
    """
    
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fibs(n - 1) + fibs(n - 2)
    
meno = {0:0, 1:1}
def fibs_good(n):
    if n not in meno:
        meno[n] = fibs_good(n - 1) + fibs_good(n - 2)
    return meno[n]
    
if __name__ == "__main__":
    f = fibs(8)
    print "fibs = ", f
    f = fibs_good(8)
    print "fibs_good = ", f
    
    
    
