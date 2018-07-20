i = 2

prime = [2]
while len(prime) < 10000:
    i += 1
    for a in prime:
        if i % a == 0:
            break
    else:
        prime.append(i)

print(prime[-1])