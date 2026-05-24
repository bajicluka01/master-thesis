import numpy as np

def fw(a, b, c):
    #TODO
    if c > (a+b)/2:
        print("large c")
    upper_bound = a
    for l in range(1, int(np.floor(a/b))):
        print("l", l)
        tmp = int(np.ceil((l*b-2*l*c)/(2*a)))
        print("tmp", tmp)
        k1 = int(np.ceil(tmp))
        k2 = int(np.floor(tmp))
        #s1 = np.abs(max(c+k1*a, b))
        #s2 = np.abs(max(c+k2*a, b))

        print("k", k1, k2)

        #s1 = max(k1*a+l*c, l*b)
        #s2 = max(k2*a+l*c, l*b)

        #s1 = abs(k1*a+l*c)
        #s2 = abs(k2*a+l*c)

        s1 = max(abs(c+k1*a), b)
        s2 = max(abs(c+k2*a), b)

        print("s", s1, s2)
        if s1 < upper_bound:
            upper_bound = s1
        if s2 < upper_bound:
            upper_bound = s2
        print("ub", upper_bound)
        print()
    return upper_bound

if __name__ == "__main__":
    print(fw(16, 1, 6))
