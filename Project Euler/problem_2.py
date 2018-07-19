fibo = [0, 1, 1]
result = 0

while True:
    temp = fibo[-1] + fibo[-2]
    if temp > 4000000:
        break
    fibo.append(temp)

print(sum(fibo[::3]))
