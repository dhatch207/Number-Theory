import math

def continued_fraction (d,n):
    # compute the a_n
    a_n = []
    decimals = []
    a_n.append(math.floor(d))
    decimals.append(d % 1)
    for i in range(n):
        a_n.append(math.floor(1 / decimals[i]))
        decimals.append(1 / decimals[i] % 1)
        i = i + 1
    return(a_n)    

# 17.8.3(3) LOOSES PRECISION QUICKLY
print(f"\n17.8.3(3)")
num_terms = 
print(f"\ne: {continued_fraction(math.e,num_terms)}")
print(f"\n(e+1)/(e-1): {continued_fraction((math.e+1)/(math.e-1),num_terms)}")
print(f"\n(e^2+1)/(e^2-1): {continued_fraction(((math.e ** 2) + 1)/((math.e ** 2) - 1),num_terms)}")