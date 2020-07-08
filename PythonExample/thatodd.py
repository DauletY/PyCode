stop = int(input())
nums = []
x = 0


while x < stop:
    y = int(input())
    nums.append(y)
    x += 1

filt = lambda x: x % 2 == 0

res = sum(list(filter(filt, nums)))
print(res)
