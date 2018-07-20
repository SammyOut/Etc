prime = [2]
result = 2

for i in range(3, 21):
    for a in prime:
        if i % a == 0:
            break
    else:
        prime.append(i)
        result *= i

result *= 2 ** 3
result *= 3

print(result)