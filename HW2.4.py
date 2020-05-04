import math, numpy

# 17.8.1(2) find a,b less than 100 such that |.123456789-(a/b)|<10^(-8)
print(f"\n17.8.1(2)")
for b in range(1,99):
    for a in range(b):
        if(abs(.123456789 - (a/b)) < (10 ** (-8))):
            print(f"a = {a}, b = {b}")

# 17.8.1(4) Find a and b with 0<b<20 such that |(3141/5926)-(a/b)|<.001
print(f"\n17.8.1(4)")
for b in range(1,19):
    for a in range(round((3141 * 20) / 5926)):
        if(abs((3141 / 5926)-(a / b)) < .001):
            print(f"a = {a}, b = {b}")
    
# 17.8.1(8) For each denominator b with 1 <= b <= 6, 
# find the fraction a/b that is closest to pi
print(f"\n17.8.1(8)")
for b in range(1,8):
    fractions = [math.inf] * (4 * b)
    for a in range(4 * b):
        fractions[a] = abs((a / b) - math.pi)
    print(f"b = {b}, a = {numpy.argmin(fractions)}, (a/b) = {numpy.argmin(fractions)/b}")

def pellSolver (d):
    # compute the a_n
    a_n = []
    decimals = []
    a_n.append(math.floor(d ** (1 / 2)))
    decimals.append(d ** (1 / 2) % 1)
    i = 0
    while(a_n[i] != (2 * a_n[0])):
        a_n.append(math.floor(1 / decimals[i]))
        decimals.append(1 / decimals[i] % 1)
        i = i + 1
    
    # compute the p_n and q_n
    p_n = [0,1]
    q_n = [1,0]
    for a in range(len(a_n)):
        p_n.append(p_n[a] + (p_n[a + 1] * a_n[a]))
        q_n.append(q_n[a] + (q_n[a + 1] * a_n[a]))

    # find x and y
    x_i = p_n[len(a_n)]
    y_i = q_n[len(a_n)]
    if((x_i ** 2) - (d * (y_i ** 2)) == 1):
        x = x_i
        y = y_i
    elif((x_i ** 2) - (d * (y_i ** 2)) == -1):
        x = (x_i ** 2) + ((y_i ** 2) * d)
        y = 2 * x_i * y_i
    
    # print solution
    print(f"{x}^2 - {d}({y}^2) = 1")

# 17.8.3(1) Find a nontrivial solution of x^{2}-61y^{2}=1.
print(f"\n17.8.3(1)")
pellSolver(61)

# 17.8.3(2) Find a nontrivial solution of x^{2}-109y^{2}=1.
print(f"\n17.8.3(2)")
pellSolver(109)