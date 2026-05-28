import numpy as np

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

        #s1 = abs(max(k1*a+l*c, l*b))
        #s2 = abs(max(k2*a+l*c, l*b))

        s1 = max(abs(k1*a+l*c), l*b)
        s2 = max(abs(k2*a+l*c), l*b)

        if s1 < upper_bound:
            upper_bound = s1
        if s2 < upper_bound:
            upper_bound = s2
    return upper_bound

if __name__ == "__main__":
    a = 9
    b = 1
    c = 4
    print(fw(a, b, c))
