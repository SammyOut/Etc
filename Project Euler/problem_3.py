num = 600851475143
prime = [2]
i = 2
while num > 1:
    while num % prime[-1] == 0:
        num //= prime[-1]

    i += 1
    for a in prime:
        if i % a == 0:
            break
    else:
        prime.append(i)

print(prime[-1])
