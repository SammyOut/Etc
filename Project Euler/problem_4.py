def palindrome():
    for i in range(999, 899, -1):
        for j in range(999, 899, -1):
            temp = str(i * j)
            if temp == temp[::-1]:
                return temp


print(palindrome())
