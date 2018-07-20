prime = [2]


def check_prime(i):
    global prime
    for a in prime:
        if a**2 > i:
            return True
        elif i % a == 0:
            return False
    return True


for i in range(3, 2000000, 2):
    if check_prime(i):
        prime.append(i)

print(sum(prime))