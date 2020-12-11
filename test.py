
a = [35, 62, 2, 40, 6, 18, 24, 1, 55, 28]
for j in range(len(a)):
    check = False
    i = 0
    while i < len(a)-1:
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            check = True
        i = i+1
    print(a)
    if check == False:
        break
# print(a)
