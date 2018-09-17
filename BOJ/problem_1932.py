triangle = []
biggest = 0


def f(a=0, b=0, temp=0):
    global triangle
    global biggest

    if a == len(triangle):
        return

    temp += triangle[a][b]
    if temp > biggest:
        biggest = temp

    f(a + 1, b, temp)
    f(a + 1, b + 1, temp)


for i in range(int(input())):
    triangle.append([int(a) for a in input().split()])

f()
print(biggest)
w