
a=[]
b=[]
result = []

a = 3, 2, 1
b = True, False, False

for i in zip(a, b):
    if i[1] == False:
        result.append(i[0] * -1)
    else:
        result.append(i[0] * 1)

print(sum(result))


for i in range(3):
    print(b[i])
    if b[i] == False:
        result.append(abs(a[i]) * -1)
    else:
        result.append(abs(a[i]) * 1)

print(sum(result))
