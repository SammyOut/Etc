# 1000보다 작은 자연수 중 3 또는 5의 배수의 합
print(sum([a for a in range(1000) if a % 3 == 0 or a % 5 == 0]))