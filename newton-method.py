M = 2 # value one wants to approximate for sqrt(M)
x1 = 1 # a x1 reasonably close to c such that f(c) = 0


def root(x):
    return (x - (((x ** 2) - M)/(2*x)))

def newtonmethod(n):
    counter = 1
    holder = root(x1)
    while counter < n:
        holder = root(holder)
        counter = counter + 1
    return holder



