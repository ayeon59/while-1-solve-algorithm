for a in range(2, 101):  # Cube 값 a는 2부터 100까지
    a3 = a ** 3
    for b in range(2, a):         # b < a
        b3 = b ** 3
        for c in range(b, a):     # c < a
            c3 = c ** 3
            for d in range(c, a): # d < a
                d3 = d ** 3
                if b3 + c3 + d3 == a3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
