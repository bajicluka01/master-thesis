import numpy as np

def sgn(x):
    if x >= 0:
        return 1
    else: 
        return -1

def fw(a, b, c):
    #if c == 0: # speculative
    #    return min(a, b)

    if c > (a+b)/2: #TODO convert into an equivalent representation
        print("large c")
    if a < 3:
        print("small a")
    upper_bound = a
    for l in range(1, int(np.floor(a/b))+1):
        tmp = (l*b-2*l*c)/(2*a)
        k1 = int(np.ceil(tmp))
        k2 = int(np.floor(tmp))

        c1 = k1*a+l*c
        c2 = k2*a+l*c
        lb = l*b

        if sgn(c1) != sgn(lb):
            d1 = abs(c1) + abs(lb)
        else:
            d1 = max(abs(k1*a+l*c), lb)

        if sgn(c2) != sgn(lb):
            d2 = abs(c2) + abs(lb)  
        else:
            d2 = max(abs(k2*a+l*c), lb)

        if d1 < upper_bound:
            upper_bound = d1
        if d2 < upper_bound:
            upper_bound = d2
    return upper_bound

if __name__ == "__main__":
    a = 18
    b = 1
    c = 11
    print(fw(a, b, c))
