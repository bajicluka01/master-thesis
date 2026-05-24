def negami(a):
    d, h, o = a
    return d, (o-h)%d, h

def our(a):
    p, q, r = a
    return (p, r, (r+q)%p)

def euclid_gcd(a, b):
    if b == 0:
        return a
    return euclid_gcd(b, a % b)

def equivalence(p, q, r):
    def beta(p, q, r):
        #max_b = 10000
        #b = 0
        #while b<max_b:
        for b in range(max(p, r)+1):
            if (b*(r+q))%p == (-(euclid_gcd(p, q+r)))%p:
                return b
        return None
    
    def eqI(p, q, r):
        p_ = p*r/euclid_gcd(p, q+r)
        bet = beta(p,q,r)
        if bet == None: # shouldn't happen, but just in case
            return -1, -1, -1
        q_ = (bet*r)%p_
        r_ = euclid_gcd(p, q+r)
        return int(p_), int(q_), int(r_)

    def eqIII(p, q, r):
        return p, (-(q+r)%p), r

    eq = [(p, q, r)]
    p1, q1, r1 = eqI(p,q,r)
    p2, q2, r2 = eqI(p1,q1,r1)
    p3, q3, r3 = eqIII(p,q,r)
    p4, q4, r4 = eqIII(p1,q1,r1)
    p5, q5, r5 = eqIII(p2,q2,r2)

    eq.append((p1,q1,r1))
    eq.append((p2,q2,r2))
    eq.append((p3,q3,r3))
    eq.append((p4,q4,r4))
    eq.append((p5,q5,r5))
    return eq

def full_printout():
    out = ""

    d = 1
    while d <= 20:
        h = 1
        while h <= d:
            o = 0
            if d*h < 7:
                h += 1
                continue
            while o < d:
                if d*h > 20:
                    o += 1
                    continue
                
                p, q, r = negami((d, h, o))
                equiv = equivalence(p, q, r)
                converted = [our(eq) for eq in equiv]

                tmpstr = ""
                for conv in converted:
                    tmp="T"+str(conv)
                    if tmp not in tmpstr and tmp not in out:
                        if tmpstr:
                            tmpstr += " = "+tmp
                        else:
                            tmpstr = tmp

                if tmpstr:
                    out += tmpstr + "\n"

                o += 1
            h += 1
        d += 1

    print(out)

d = 16
h = 1
o = 6

p, q, r = negami((d, h, o))

# uncomment this if you want to convert directly from Negami's notation
#p = 14
#q = 6
#r = 1

equiv = equivalence(p, q, r)
print("Negami: ", equiv)

converted = [our(eq) for eq in equiv]

print("Our:    ", converted)


#full_printout()

