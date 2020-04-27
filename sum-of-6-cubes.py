import time
start_time = time.time()

# expresses number as sum of 6 cubes #

target = int(input("enter a number "))

cap = int(round( target ** (1. / 3))) 

def main():
    for a in range(cap):
        for b in range(cap):
            if b > a:
                continue
            for c in range(cap):
                if c > b:
                    continue
                for d in range(cap):
                    if d > c:
                        continue
                    for e in range(cap):
                        if e > d:
                            continue
                        for f in range(cap):
                            if f > e:
                                continue
                            if ((a ** 3) + (b ** 3) + (c ** 3) + (d ** 3) + (e ** 3) + (f ** 3)) == target:
                                print(f"{target} = {a}^3 + {b}^3 + {c}^3 + {d}^3 + {e}^3 + {f}^3")
                                print("Solved in  %s seconds" % (time.time() - start_time))
                                return
    print(f"no solution")

main()