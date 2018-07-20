def pythagoras():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == 1000:

                return int(a * b * c)

print(pythagoras())