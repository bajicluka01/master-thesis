from tkinter import *
import numpy as np

def init():
    global d, h, o
    grid, vertices = create_grid(edge_len, width, height)
    lines = draw_grid(grid)

    # this 0.5 constant is purely arbitrary
    # the idea is that regardless of d, h, o parameters, the main keypoint is always 
    # located in the same position on the grid, which is hopefully intuitive for human readability
    kp = int(0.5*len(vertices)*len(vertices[0]))
    kp_i = int(kp/len(vertices))
    kp_j = int(kp/len(vertices[0]))
    keypoints = draw_keypoint(grid, kp_i, kp_j, circle_size)
    display_equivalence()
    return grid, lines, keypoints

def euclid_gcd(a, b):
    if b == 0:
        return a
    return euclid_gcd(b, a % b)

def equivalence(d, h, o):
    def beta(p, q, r):
        for b in range(max(p, r)+1):
            #if b*(r+q) == (-(euclid_gcd(p, q+r)))%p:
            if (b*(r+q))%p == (-(euclid_gcd(p, q+r)))%p:
                return b
        return None
    
    def eqI(p, q, r):
        p_ = p*r/euclid_gcd(p, q+r)
        bet = beta(p,q,r)
        if not bet: # shouldn't happen, but just in case
            return -1, -1, -1
        #q_ = ((-euclid_gcd(p, q))+(bet*r))%p_
        q_ = (bet*r)%p_
        r_ = euclid_gcd(p, q+r)
        return int(p_), int(q_), int(r_)

    def eqIII(p, q, r):
        return p, (-(q+r)%p), r
    
    print(eqI(d,h,o))
    print(eqIII(d,h,o))
    
    eq = [our((d, h, o))]
    eq.append(our(eqIII(d, h, o)))
    eq.append(our(eqI(d, h, o)))
    tmp = eqI(d, h, o)
    d_, h_, o_ = tmp
    eq.append(our(eqI(d_, h_, o_)))
    return eq

def negami(a):
    d, h, o = a
    return d, (o-h)%d, h

def our(a):
    p, q, r = a
    return (p, r, (r+q)%p)

def display_equivalence():
    text = ""
    p, q, r = negami((d, h, o))
    equiv = equivalence(p, q, r)


    alr = set()
    for e in equiv:
        alr.add(e)
        text += f"T({e[0]}, {e[1]}, {e[2]}) = "
    text = text[:-3]
    Label(root, text=text).place(x=400, y=y_padding)
    print(equivalence(12, 3, 1))

def random_color():
    rgb = (np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255))
    return "#%02x%02x%02x" % rgb 

def redraw():
    global grid, lines, keypoints
    canvas.delete('all')
    grid, lines, keypoints = init()

def print_state():
    print(f"d={d}, h={h}, o={o}")

def d_update(event=None):
    global d
    d = int(d_spin.get())
    print_state()
    redraw()

def h_update(event=None):
    global h
    h = int(h_spin.get())
    print_state()
    redraw()

def o_update(event=None):
    global o
    o = int(o_spin.get())
    print_state()
    redraw()

def click(event=None):
    global grid, lines, keypoints
    x, y = event.x, event.y
    line_click = False
    for line in lines:
        k, n = line
        if abs(k*x+n - y) <= 5:
            if k == 0:
                max_x = np.inf
                for i in range(1, len(grid)):
                    if abs(grid[i][0][0]-n) < max_x:
                        max_x = i  

                max_y = np.inf
                max_j1 = None
                max_j2 = None
                for j in range(1, len(grid[0])):
                    a = abs(grid[max_x][j-1][1]-x)+abs(grid[max_x][j][1]-x)
                    if a < max_y:
                        max_y = a
                        max_j1 = j-1
                        max_j2 = j

                new_x, new_y = grid[max_x][max_j1], grid[max_x][max_j2]
                line_click = True
                break

    nkp, nd, nx, ny = nearest_keypoint((x,y), keypoints)
    print("Clicked ", x, y)
    print("Nearest keypoint ", nkp)

    if line_click:
        color = random_color()
        draw_lines(new_x, new_y, color)
    
def draw_lines(x, y, color, wid=5):
    global grid, keypoints, edge_len
    canvas.create_line(x[1], x[0], y[1], y[0], fill=color, width=wid) 
    nkp1, nd1, nx1, ny1 = nearest_keypoint(x, keypoints)
    nkp2, nd2, nx2, ny2 = nearest_keypoint(y, keypoints)

    min_p = np.inf
    for p in keypoints:
        if p[1] == x[0]:
            if abs(p[0]-x[1]) < min_p:
                min_p = abs(p[0]-x[1])

    for p in keypoints:
        canvas.create_line(p[0]+min_p, p[1], p[0]+min_p+edge_len, p[1], fill=color, width=wid) 

    d1 = dist(x, nkp1)
    d2 = dist(y, nkp1)
    d3 = dist(x, nkp2)
    d4 = dist(y, nkp2)
    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])-1):
            nkp, nd, nx, ny = nearest_keypoint(grid[i][j], keypoints)
            #if nx == nx1 or nx == nx2:
            #    if nd == nd1 or nd == nd2:
            #        canvas.create_line(grid[i][j][1], grid[i][j][0], grid[i][j][1]+20, grid[i][j][0]+20, fill=color, width=wid) 


def dist(x, y):
    return np.sqrt(pow(x[0]-y[0], 2) + pow(x[1]-y[1], 2))

def create_grid(l, total_w, total_h):
    i = -l-5
    grid = []
    mapp = []
    c = 0
    loop1 = 0
    while i < total_h+l+5:
        j = -l-5
        grid.append([])
        mapp.append([])
        while j < total_w+l+5:
            if loop1%2 == 0:
                grid[loop1].append((i, j))
            else:
                grid[loop1].append((i, j+l/2))
            mapp[loop1].append(c)
            c += 1
            j += l
        i += l*np.sqrt(3)/2 # to ensure the triangles are equilateral 
        loop1 += 1

    return grid, mapp

def draw_grid(grid):
    lines = []
    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])-1):
            # horizontal lines
            a1, b1 = grid[i][j-1]
            a2, b2 = grid[i][j]
            canvas.create_line(b1, a1, b2, a2)

            if (0, a1) not in lines:
                lines.append((0, a1))

            # vertical lines
            a1, b1 = grid[i-1][j]
            a2, b2 = grid[i][j]
            a3, b3 = grid[i][j-1]
            a4, b4 = grid[i][j+1]
            canvas.create_line(b1, a1, b2, a2)

            if i%2 == 0:
                canvas.create_line(b4, a4, b1, a1)
            else:
                canvas.create_line(b3, a3, b1, a1)
    
    return lines

def draw_keypoint(grid, center_x, center_y, circle_size=2):
    keypoints = []
    i = center_y
    while i < len(grid[0]):
        x, y = grid[center_x][i]
        canvas.create_oval(y-circle_size, x-circle_size, y+circle_size, x+circle_size, fill="black")
        keypoints.append((y, x))
        i += d

    i = center_y-d
    while i >= 0:
        x, y = grid[center_x][i]
        canvas.create_oval(y-circle_size, x-circle_size, y+circle_size, x+circle_size, fill="black")
        keypoints.append((y, x))
        i -= d

    if center_x%2 == 0:
        c = o-1
    else:
        c = o
    j = center_x-h
    while j >= 0:
        i = center_y+c
        start_i = center_y+c
        while i < len(grid[0]):
            x, y = grid[j][i]
            canvas.create_oval(y-circle_size, x-circle_size, y+circle_size, x+circle_size, fill="black")
            keypoints.append((y, x))
            i += d

        i = start_i-d
        while i >= len(grid[j]):
            i -= d # this is just to get back into legal range on topmost layers
        while i >= 0:
            x, y = grid[j][i]
            canvas.create_oval(y-circle_size, x-circle_size, y+circle_size, x+circle_size, fill="black")
            keypoints.append((y, x))
            i -= d

        if j%2 == 0:
            c += o-1
        else:
            c += o
        j -= h

    #for i in range(len(grid)):
    #    x, y = grid[i][9]
    #    canvas.create_oval(y-circle_size, x-circle_size, y+circle_size, x+circle_size, fill="red")

    return keypoints

def nearest_keypoint(point, keypoints):
    x, y = point
    min_d = np.inf
    min_kp = None
    min_x = np.inf
    min_y = np.inf
    for p in keypoints:
        #x_, y_ = p
        y_, x_ = p
        d = np.sqrt(pow(x_-x, 2)+pow(y_-y, 2))
        if d < min_d:
            min_d = d
            min_kp = p
            min_x = abs(x-x_)
            min_y = abs(y-y_)
    
    return min_kp, min_d, min_x, min_y

d = 7
h = 1
o = 3

y_padding = 10
width = 1200
height = 700
edge_len = 50
circle_size = 4

root = Tk()
root.title("6-regular toroidal graph")

d_spin = Spinbox(root, from_=1, to=100, width=3, relief="sunken", command=d_update, textvariable=DoubleVar(value=d))
d_spin.bind("<Return>", d_update)
d_spin.place(x=50, y=y_padding)

h_spin = Spinbox(root, from_=1, to=100, width=3, relief="sunken", command=h_update, textvariable=DoubleVar(value=h))
h_spin.bind("<Return>", h_update)
h_spin.place(x=120, y=y_padding)

o_spin = Spinbox(root, from_=0, to=100, width=3, relief="sunken", command=o_update, textvariable=DoubleVar(value=o))
o_spin.bind("<Return>", o_update)
o_spin.place(x=190, y=y_padding)

Label(root, text="d=").place(x=30, y=y_padding)
Label(root, text="h=").place(x=100, y=y_padding)
Label(root, text="o=").place(x=170, y=y_padding)

canvas = Canvas(root, width=width, height=height)
canvas.bind("<Button-1>", click)
canvas.pack(padx=50, pady=50)

grid, lines, keypoints = init()

root.mainloop()
