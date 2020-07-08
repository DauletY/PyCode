p = input()
p2 = p.split()

nums = "zero one two three four five six seven eight nine ten".split()

fin = ""

for chr in p2:
    if chr.isdigit():
        fin = fin + nums[int(chr)] + " "
    else:
        fin = fin + chr + " "

print(fin)
