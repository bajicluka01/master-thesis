import random

class Node:
    def __init__(self, id, label):
        self.id = id
        self.label = label 

def check6regularity(adj):
    for _, neighbors in adj.items():
        if len(list(neighbors)) != 6:
            return False
    return True

def union(a, b):
    out = {aa for aa in a}
    for bb in b:
        out.add(bb)
    return out

# i and j should be adjacent! 
# check this before calling the function
def contract(adj, maxid, i, j):
    #global maxid
    #global adj
    newnode = maxid+1
    maxid = maxid+1
    tmpi = adj.pop(i)
    tmpj = adj.pop(j)
    #ij = union(tmpi, tmpj)
    new_neighbors = set()
    tmp_adj = {}
    for v, neighbors in adj.items():
        tmpn = neighbors.copy()
        for it in neighbors:
            if it == i or it == j:
                tmpn.remove(it)
                tmpn.add(newnode)
                new_neighbors.add(v)
        tmp_adj[v] = tmpn
        
    for v, tmpn in tmp_adj.items():
        adj.pop(v)
        adj[v] = tmpn
    adj[newnode] = new_neighbors
    return adj, maxid

def checkall3contractions(adj, maxid, check_which=False):
    vertices = list(adj.keys())
    totalcount = 0
    n_valid = 0
    i1 = 1
    while i1 <= len(vertices):
        i2 = i1+1
        while i2 <= len(vertices):
            a1 = adj.copy()
            if vertices[i2-1] not in list(a1[vertices[i1-1]]):
                i2 += 1
                continue
            c1, max1 = contract(a1, maxid, vertices[i1-1], vertices[i2-1])
            vertices1 = list(c1.keys())
            i3 = 1
            while i3 <= len(vertices1):
                i4 = i3+1
                while i4 <= len(vertices1):
                    a2 = a1.copy()
                    if vertices1[i4-1] not in list(a2[vertices1[i3-1]]):
                        i4 += 1
                        continue
                    c2, max2 = contract(a2, max1, vertices1[i3-1], vertices1[i4-1])
                    vertices2 = list(c2.keys())
                    i5 = 1
                    while i5 <= len(vertices2):
                        i6 = i5+1
                        while i6 <= len(vertices2):
                            a3 = a2.copy()
                            if vertices2[i6-1] not in list(a3[vertices2[i5-1]]):
                                i6 += 1
                                continue
                            c3, max3 = contract(a3, max2, vertices2[i5-1], vertices2[i6-1])
                            vertices3 = list(c3.keys())

                            if check6regularity(c3):
                                n_valid += 1
                                if check_which:
                                    if is_cycle(complement(c3)):
                                        print("T9")
                                    else:
                                        print("T0")

                                else:
                                    print("START")
                                    print(vertices)
                                    print(vertices[i1-1], vertices[i2-1])
                                    print(vertices1)
                                    print(vertices1[i3-1], vertices1[i4-1])
                                    print(vertices2)
                                    print(vertices2[i5-1], vertices2[i6-1])
                                    print(vertices3)
                                    print("END")

                            totalcount += 1
                            if totalcount%100000 == 0:
                                print(totalcount)

                            i6 += 1
                        i5 += 1
                    i4 += 1
                i3 += 1
            i2 += 1
        i1 += 1

    print("Number of valid contractions found:", n_valid)
    print("Total number of contractions checked:", totalcount)

def checkall4contractions(adj, maxid, check_which=False):
    vertices = list(adj.keys())
    totalcount = 0
    n_valid = 0
    i1 = 1
    while i1 <= len(vertices):
        i2 = i1+1
        while i2 <= len(vertices):
            a1 = adj.copy()
            if vertices[i2-1] not in list(a1[vertices[i1-1]]):
                i2 += 1
                continue
            c1, max1 = contract(a1, maxid, vertices[i1-1], vertices[i2-1])
            vertices1 = list(c1.keys())
            i3 = 1
            while i3 <= len(vertices1):
                i4 = i3+1
                while i4 <= len(vertices1):
                    a2 = a1.copy()
                    if vertices1[i4-1] not in list(a2[vertices1[i3-1]]):
                        i4 += 1
                        continue
                    c2, max2 = contract(a2, max1, vertices1[i3-1], vertices1[i4-1])
                    vertices2 = list(c2.keys())
                    i5 = 1
                    while i5 <= len(vertices2):
                        i6 = i5+1
                        while i6 <= len(vertices2):
                            a3 = a2.copy()
                            if vertices2[i6-1] not in list(a3[vertices2[i5-1]]):
                                i6 += 1
                                continue
                            c3, max3 = contract(a3, max2, vertices2[i5-1], vertices2[i6-1])
                            vertices3 = list(c3.keys())
                            i7 = 1
                            while i7 <= len(vertices3):
                                i8 = i7+1
                                while i8 <= len(vertices3):
                                    a4 = a3.copy()
                                    if vertices3[i8-1] not in list(a4[vertices3[i7-1]]):
                                        i8 += 1
                                        continue
                                    c4, max4 = contract(a4, max3, vertices3[i7-1], vertices3[i8-1])
                                    vertices4 = list(c4.keys())

                                    if check6regularity(c4):
                                        if check_which:
                                            if is_cycle(complement(c4)):
                                                print("T9")
                                            else:
                                                print("T0")

                                        else:
                                            print("START")
                                            print(vertices)
                                            print(vertices[i1-1], vertices[i2-1])
                                            print(vertices1)
                                            print(vertices1[i3-1], vertices1[i4-1])
                                            print(vertices2)
                                            print(vertices2[i5-1], vertices2[i6-1])
                                            print(vertices3)
                                            print(vertices3[i7-1], vertices3[i8-1])
                                            print(vertices4)
                                            print("END")
                                        n_valid += 1
                                    totalcount += 1
                                    if totalcount%100000 == 0:
                                        print(totalcount)
                                    i8 += 1
                                i7 += 1
                            i6 += 1
                        i5 += 1
                    i4 += 1
                i3 += 1
            i2 += 1
        i1 += 1

    print("Number of valid contractions found:", n_valid)
    print("Total number of contractions checked:", totalcount)

def checkall5contractions(adj, maxid, check_which=False):
    vertices = list(adj.keys())
    totalcount = 0
    n_valid = 0
    i1 = 0
    while i1 < len(vertices):
        i2 = i1+1
        while i2 < len(vertices):
            a1 = adj.copy()
            if vertices[i2] not in list(a1[vertices[i1]]):
                i2 += 1
                continue
            c1, max1 = contract(a1, maxid, vertices[i1], vertices[i2])
            vertices1 = list(c1.keys())
            i3 = 0
            while i3 < len(vertices1):
                i4 = i3+1
                while i4 < len(vertices1):
                    a2 = a1.copy()
                    if vertices1[i4] not in list(a2[vertices1[i3]]):
                        i4 += 1
                        continue
                    c2, max2 = contract(a2, max1, vertices1[i3], vertices1[i4])
                    vertices2 = list(c2.keys())
                    i5 = 0
                    while i5 < len(vertices2):
                        i6 = i5+1
                        while i6 < len(vertices2):
                            a3 = a2.copy()
                            if vertices2[i6] not in list(a3[vertices2[i5]]):
                                i6 += 1
                                continue
                            c3, max3 = contract(a3, max2, vertices2[i5], vertices2[i6])
                            vertices3 = list(c3.keys())
                            i7 = 0
                            while i7 < len(vertices3):
                                i8 = i7+1
                                while i8 < len(vertices3):
                                    a4 = a3.copy()
                                    if vertices3[i8] not in list(a4[vertices3[i7]]):
                                        i8 += 1
                                        continue
                                    c4, max4 = contract(a4, max3, vertices3[i7], vertices3[i8])
                                    vertices4 = list(c4.keys())
                                    i9 = 0
                                    while i9 < len(vertices4):
                                        i10 = i9+1
                                        while i10 < len(vertices4):
                                            a5 = a4.copy()
                                            if vertices4[i10] not in list(a5[vertices4[i9]]):
                                                i10 += 1
                                                totalcount += 1
                                                if totalcount%100000 == 0:
                                                    print(totalcount)
                                                continue
                                            c5, max5 = contract(a5, max4, vertices4[i9], vertices4[i10])
                                            vertices5 = list(c5.keys())

                                            if check6regularity(c5):
                                                n_valid += 1
                                                if check_which:
                                                    if is_cycle(complement(c5)):
                                                        print("T9")
                                                    else:
                                                        print("T0")
                                                else:
                                                    print("START")
                                                    print(vertices)
                                                    print(vertices[i1], vertices[i2])
                                                    print(vertices1, (i1), (i2))
                                                    print(c1)
                                                    print(vertices1[i3], vertices1[i4])
                                                    print(vertices2, (i3), (i4))
                                                    print(c2)
                                                    print(vertices2[i5], vertices2[i6])
                                                    print(vertices3, (i5), (i6))
                                                    print(c3)
                                                    print(vertices3[i7], vertices3[i8])
                                                    print(vertices4, (i7), (i8))
                                                    print(c4)
                                                    print(vertices4[i9], vertices4[i10])
                                                    print(vertices5, (i9), (i10))
                                                    print(c5)
                                                    randfilename = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(15))
                                                    f = open(randfilename+".txt", "w")
                                                    f.write(str(vertices)+"\n")
                                                    f.write(str(vertices[i1-1]) + " " + str(vertices[i2-1])+"\n")
                                                    f.write(str(vertices1)+"\n")
                                                    f.write(str(c1)+"\n")
                                                    f.write(str(vertices1[i3-1]) + " " + str(vertices1[i4-1])+"\n")
                                                    f.write(str(vertices2)+"\n")
                                                    f.write(str(c2)+"\n")
                                                    f.write(str(vertices1[i5-1]) + " " + str(vertices1[i6-1])+"\n")
                                                    f.write(str(vertices3)+"\n")
                                                    f.write(str(c3)+"\n")
                                                    f.write(str(vertices1[i7-1]) + " " + str(vertices1[i8-1])+"\n")
                                                    f.write(str(vertices4)+"\n")
                                                    f.write(str(c4)+"\n")
                                                    f.write(str(vertices1[i9-1]) + " " + str(vertices1[i10-1])+"\n")
                                                    f.write(str(vertices5)+"\n")
                                                    f.write(str(c5)+"\n")
                                                    f.close()
                                                    print("END")

                                            totalcount += 1
                                            if totalcount%100000 == 0:
                                                print(totalcount)
                                            i10 += 1
                                        i9 += 1
                                    i8 += 1
                                i7 += 1
                            i6 += 1
                        i5 += 1
                    i4 += 1
                i3 += 1
            i2 += 1
        i1 += 1

    print("Number of valid contractions found:", n_valid)
    print("Total number of contractions checked:", totalcount)

def checkall6contractions(adj, maxid, check_which=True):
    vertices = list(adj.keys())
    totalcount = 0
    n_valid = 0
    i1 = 1
    while i1 <= len(vertices):
        i2 = i1+1
        while i2 <= len(vertices):
            a1 = adj.copy()
            if vertices[i2-1] not in list(a1[vertices[i1-1]]):
                i2 += 1
                continue
            c1, max1 = contract(a1, maxid, vertices[i1-1], vertices[i2-1])
            vertices1 = list(c1.keys())
            i3 = 1
            while i3 <= len(vertices1):
                i4 = i3+1
                while i4 <= len(vertices1):
                    a2 = a1.copy()
                    if vertices1[i4-1] not in list(a2[vertices1[i3-1]]):
                        i4 += 1
                        continue
                    c2, max2 = contract(a2, max1, vertices1[i3-1], vertices1[i4-1])
                    vertices2 = list(c2.keys())
                    i5 = 1
                    while i5 <= len(vertices2):
                        i6 = i5+1
                        while i6 <= len(vertices2):
                            a3 = a2.copy()
                            if vertices2[i6-1] not in list(a3[vertices2[i5-1]]):
                                i6 += 1
                                continue
                            c3, max3 = contract(a3, max2, vertices2[i5-1], vertices2[i6-1])
                            vertices3 = list(c3.keys())
                            i7 = 1
                            while i7 <= len(vertices3):
                                i8 = i7+1
                                while i8 <= len(vertices3):
                                    a4 = a3.copy()
                                    if vertices3[i8-1] not in list(a4[vertices3[i7-1]]):
                                        i8 += 1
                                        continue
                                    c4, max4 = contract(a4, max3, vertices3[i7-1], vertices3[i8-1])
                                    vertices4 = list(c4.keys())
                                    i9 = 1
                                    while i9 <= len(vertices4):
                                        i10 = i9+1
                                        while i10 <= len(vertices4):
                                            a5 = a4.copy()
                                            if vertices4[i10-1] not in list(a5[vertices4[i9-1]]):
                                                i10 += 1
                                                totalcount += 1
                                                if totalcount%100000 == 0:
                                                    print(totalcount)
                                                continue
                                            c5, max5 = contract(a5, max4, vertices4[i9-1], vertices4[i10-1])
                                            vertices5 = list(c5.keys())
                                            i11 = 1
                                            while i11 <= len(vertices5):
                                                i12 = i11+1
                                                while i12 <= len(vertices5):
                                                    a6 = a5.copy()
                                                    if vertices5[i12-1] not in list(a6[vertices5[i11-1]]):
                                                        i12 += 1
                                                        totalcount += 1
                                                        if totalcount%100000 == 0:
                                                            print(totalcount)
                                                        continue
                                                    c6, max6 = contract(a6, max5, vertices5[i11-1], vertices5[i12-1])
                                                    vertices6 = list(c6.keys())

                                                    if check6regularity(c6):
                                                        n_valid += 1
                                                        if check_which:
                                                            if is_cycle(complement(c6)):
                                                                print("T9")
                                                            else:
                                                                print("T0")
                                                        else:
                                                            print("START")
                                                            print(vertices)
                                                            print(vertices[i1-1], vertices[i2-1])
                                                            print(vertices1)
                                                            print(c1)
                                                            print(vertices1[i3-1], vertices1[i4-1])
                                                            print(vertices2)
                                                            print(c2)
                                                            print(vertices2[i5-1], vertices2[i6-1])
                                                            print(vertices3)
                                                            print(c3)
                                                            print(vertices3[i7-1], vertices3[i8-1])
                                                            print(vertices4)
                                                            print(c4)
                                                            print(vertices4[i9-1], vertices4[i10-1])
                                                            print(vertices5)
                                                            print(c5)
                                                            print(vertices5[i11-1], vertices5[i12-1])
                                                            print(vertices6)
                                                            print(c6)
                                                            """randfilename = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(15))
                                                            f = open(randfilename+".txt", "w")
                                                            f.write(str(vertices)+"\n")
                                                            f.write(str(vertices[i1-1]) + " " + str(vertices[i2-1])+"\n")
                                                            f.write(str(vertices1)+"\n")
                                                            f.write(str(c1)+"\n")
                                                            f.write(str(vertices1[i3-1]) + " " + str(vertices1[i4-1])+"\n")
                                                            f.write(str(vertices2)+"\n")
                                                            f.write(str(c2)+"\n")
                                                            f.write(str(vertices2[i5-1]) + " " + str(vertices2[i6-1])+"\n")
                                                            f.write(str(vertices3)+"\n")
                                                            f.write(str(c3)+"\n")
                                                            f.write(str(vertices3[i7-1]) + " " + str(vertices3[i8-1])+"\n")
                                                            f.write(str(vertices4)+"\n")
                                                            f.write(str(c4)+"\n")
                                                            f.write(str(vertices4[i9-1]) + " " + str(vertices4[i10-1])+"\n")
                                                            f.write(str(vertices5)+"\n")
                                                            f.write(str(c5)+"\n")
                                                            f.write(str(vertices5[i11-1]) + " " + str(vertices5[i12-1])+"\n")
                                                            f.write(str(vertices6)+"\n")
                                                            f.write(str(c5)+"\n")
                                                            f.close()"""
                                                            print("END")

                                                    totalcount += 1
                                                    if totalcount%100000 == 0:
                                                        print(totalcount)
                                                    i12 += 1
                                                i11 += 1
                                            i10 += 1
                                        i9 += 1
                                    i8 += 1
                                i7 += 1
                            i6 += 1
                        i5 += 1
                    i4 += 1
                i3 += 1
            i2 += 1
        i1 += 1

    print("Number of valid contractions found:", n_valid)
    print("Total number of contractions checked:", totalcount)

def complement(adj):
    vertices = list(adj.keys())
    newadj = {}
    for v in vertices:
        newadj[v] = set()
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if j <= i:
                continue
            v1 = vertices[i]
            v2 = vertices[j]
            if v2 in list(adj[v1]):
                continue
            newadj[v1].add(v2)
            newadj[v2].add(v1)        
    return newadj

def is_cycle(adj):
    vertices = list(adj.keys())
    for v, neighbors in adj.items():
        if len(neighbors) != 2: # neither T9 nor T0
            return False
    first = vertices[0]
    current = vertices[0]
    visited = [vertices[0]]
    for _ in range(len(vertices)):
        tmp = list(adj[current])
        if tmp[0] in visited and tmp[1] in visited:
            return (first in tmp and len(visited) == len(vertices))
        if tmp[0] in visited:
            current = tmp[1]
            visited.append(tmp[1])
        elif tmp[1] in visited:
            current = tmp[0]
            visited.append(tmp[0])
        else:
            current = tmp[0]
            visited.append(tmp[0])
    return False
        

# T(3, 4, 2)
maxid = 12
adj = {1:{2,4,5,11,12,3}, 2:{1,3,5,6,10,12}, 3:{1,2,4,6,10,11}, 4:{1,5,7,8,3,6}, 5:{1,2,4,6,8,9}, 6:{2,3,4,5,7,9}, 7:{4,8,10,11,6,9}, 
       8:{4,5,9,7,11,12}, 9:{5,6,7,8,10,12}, 10:{7,11,2,3,9,12}, 11:{7,8,10,12,3,1}, 12:{8,9,10,11,1,2}}

#checkall4contractions(adj, maxid)
#checkall3contractions(adj, maxid, check_which=True)

# T(3, 4, 1)
maxid = 12
adj = {1:{2,4,5,10,11,3}, 2:{1,5,6,3,11,12}, 3:{1,2,6,4,10,12}, 4:{1,5,7,8,3,6}, 5:{1,2,4,6,8,9}, 6:{2,3,4,5,7,9}, 7:{4,7,10,11,6,9}, 
       8:{4,5,7,9,11,12}, 9:{5,6,7,8,10,12}, 10:{7,3,11,1,9,12}, 11:{10,7,1,2,12,8}, 12:{8,9,10,11,2,3}}

#checkall4contractions(adj, maxid, check_which=True)

# T(13, 1, 4)
maxid = 13
adj = {1: {2,10,11,13,4,5}, 2:{1,3,11,12,5,6}, 3:{2,4,12,13,6,7}, 4:{1,13,3,5,7,8}, 5:{1,2,4,6,8,9}, 6:{2,3,5,7,9,10}, 7:{6,8,10,11,3,4},
       8:{4,5,7,9,11,12}, 9:{8,10,12,13,5,6}, 10:{1,11,6,7,9,13}, 11:{10,12,1,2,7,8}, 12:{13,11,2,3,8,9}, 13:{1,3,4,12,9,10}}

#checkall4contractions(adj, maxid, check_which=True)
#checkall5contractions(adj, maxid)

# T(12, 1, 4)
maxid = 12
adj = {1:{2,9,10,12,4,5}, 2:{1,3,10,11,5,6}, 3:{2,4,11,12,6,7}, 4:{3,5,1,12,7,8}, 5:{4,6,1,2,8,9}, 6:{5,7,2,3,9,10}, 7:{6,8,3,4,10,11},
       8:{7,9,4,5,11,12}, 9:{8,10,5,6,1,10}, 10:{9,11,6,7,1,2}, 11:{10,12,7,8,2,3}, 12:{1,11,8,9,3,4}}

#checkall3contractions(adj, maxid, check_which=True)
#checkall4contractions(adj, maxid)

# T(14, 1, 4)
maxid = 14
adj = {1:{2,11,12,14,4,5}, 2:{1,3,12,13,5,6}, 3:{2,4,13,14,6,7}, 4:{3,5,1,14,7,8}, 5:{4,6,1,2,8,9}, 6:{5,7,2,3,9,10}, 7:{6,8,3,4,10,11},
       8:{7,9,4,5,11,12}, 9:{8,10,5,6,12,13}, 10:{9,11,6,7,13,1}, 11:{10,1,12,7,8,14}, 12:{11,13,8,9,1,2}, 13:{12,14,9,10,2,3}, 14:{1,13,10,11,3,4}}

#checkall5contractions(adj, maxid, check_which=True)

# T(15, 1, 4)
maxid = 15
adj = {1:{2,12,13,15,4,5}, 2:{1,3,13,14,5,6}, 3:{2,4,14,15,6,7}, 4:{3,5,15,1,7,8}, 5:{4,6,1,2,8,9}, 6:{5,7,2,3,9,10}, 7:{6,8,3,4,10,11},
       8:{7,9,4,5,11,12}, 9:{8,10,5,6,12,13}, 10:{9,11,6,7,13,14}, 11:{10,12,7,8,14,15}, 12:{11,13,8,9,1,15}, 13:{12,14,9,10,1,2}, 14:{13,15,10,11,2,3}, 15:{14,1,11,12,3,4}}

#checkall6contractions(adj, maxid, check_which=True)

# T(3, 5, 0)
maxid = 15
adj = {1:{2,4,5,3,13,15}, 2:{1,3,5,6,13,14}, 3:{2,1,6,4,14,15}, 4:{1,5,7,8,3,6}, 5:{1,2,4,6,8,9}, 6:{2,3,4,5,7,9}, 7:{4,10,8,11,6,9},
       8:{4,5,7,9,11,12}, 9:{5,6,7,8,10,12}, 10:{7,13,11,14,9,12}, 11:{7,8,10,12,14,15}, 12:{8,9,10,11,13,15}, 13:{1,10,2,14,15,12}, 14:{10,11,13,15,2,3}, 15:{11,12,13,14,1,3}}

#checkall6contractions(adj, maxid, check_which=True)

# T(3, 5, 1)
maxid = 15
adj = {1:{2,4,5,3,13,14}, 2:{1,3,5,6,14,15}, 3:{2,1,6,4,15,13}, 4:{1,5,7,8,3,6}, 5:{1,2,4,6,8,9}, 6:{2,3,4,5,7,9}, 7:{4,8,11,10,6,9},
       8:{7,9,4,5,11,12}, 9:{5,6,7,8,10,12}, 10:{7,11,13,14,9,12}, 11:{7,8,10,12,14,15}, 12:{8,9,10,11,13,15}, 13:{10,14,1,3,15,12}, 14:{10,11,13,15,1,2}, 15:{11,12,13,14,2,3}}

checkall6contractions(adj, maxid, check_which=True)

maxid7 = 7
t7 = {1:{2,5,6,7,3,4}, 2:{1,3,6,7,4,5}, 3:{2,4,7,1,5,6}, 4:{3,5,1,2,6,7}, 5:{4,6,2,3,1,7}, 6:{5,7,3,4,1,2}, 7:{6,1,4,5,2,3}}

maxid8 = 8
t8 = {1:{2,6,7,8,3,4}, 2:{1,3,7,8,4,5}, 3:{2,4,8,1,5,6}, 4:{3,5,1,2,6,7}, 5:{4,6,2,3,7,8}, 6:{5,7,3,4,8,9}, 7:{6,8,4,5,1,9}, 8:{7,9,5,6,1,2}}

maxid9 = 9
t9 = {1:{2,7,8,9,3,4}, 2:{1,3,8,9,4,5}, 3:{2,4,9,1,5,6}, 4:{3,5,1,2,6,7}, 5:{4,6,2,3,7,8}, 6:{5,7,3,4,8,9}, 7:{6,8,4,5,1,9}, 8:{7,9,5,6,1,2}, 9:{8,1,6,7,2,3}}

maxid0 = 9
t0 = {1:{2,4,5,3,9,7}, 2:{1,3,5,6,7,8}, 3:{2,1,6,4,8,9}, 4:{1,7,5,8,3,6}, 5:{1,2,4,6,8,9}, 6:{2,3,4,5,7,9}, 7:{1,4,8,2,6,9}, 8:{7,4,5,9,3,2}, 9:{8,3,1,7,6,5}}

c7 = complement(t7)
c8 = complement(t8)
c9 = complement(t9)
c0 = complement(t0)
