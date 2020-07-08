keyf = list(input())
count = 0


for i in keyf:
    count += keyf.count(i)
    print(i)

if (count != len(keyf)):
    print("Deja Vu")
else:
    print("Unique")