l = [1,2,3,"nose", ["Buenos", "dias"], 3.6]
i = 0
largo = len(l)
while i < largo:
    print(l[i])
    i += 1

print("--------------------")
for elem in l:
    print(elem)

print("--------------------")
for i in range(0, len(l)):
    print(l[i])

r = [1,2,3,3,4,5,6,3]
print(r)

while 3 in r:
    r.remove(3)
print(r)
