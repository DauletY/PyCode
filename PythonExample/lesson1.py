import cProfile

a = 10
b = 20
c = a + b
print("Sum : " , c) #30


num = 153
sum1 = 0
temp = num #153

while temp != 0:
    rem = temp % 10
    sum1 = sum1 + rem * rem * rem
    temp = temp / 10

if num == sum1:
    print("Armstrong number")
else:
    print("not an armstrong number")


#cEben odd number python
num1= 10

if num1 % 2 == 0:
    print("Even number")
else:
    print("Odd number")



def printfg():
    print(1+2)

#cProfile.run('printfg()')


for i in range(1, 10):
    print(i)
    if i > 4:
        break
    














    
