n = 0
print("введите диапазон лет: ")
ran1 = int(input("начальный год: "))
ran2 = int(input("конечный год: "))
f = open("B:\git\перепись.txt", 'r')
for i in f:
    l = []
    l.append(i.split('.'))
    if (int(l[0][2]) < 1978):
        n += 1
    if (ran1 < int(l[0][2]) < ran2):
        print(l[0][0])
f.close()
print("общее количество человек родившихся раньше 1978 года: ",n)