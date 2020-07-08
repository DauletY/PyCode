str1  = str(input().u)
inp = str1.split()
animal = []

for x in inp:
    if 'Grr' in inp:
        animal.append('Lion')
    elif 'Rawr' in inp:
        animal.append('Tiger')
    elif 'Ssss' in inp:
        animal.append('Snake')
    elif 'Chirp' in inp:
        animal.append('Bird')
    else:
        continue


ou = ' '.join(animal)
print(ou)
