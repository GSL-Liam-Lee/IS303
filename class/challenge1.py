blah = [1,7,19,22,24,8]
uneven = []
even = []
for i in blah:
    a = i%2
    if a == 0:
        even.append(i)
    else:
        uneven.append(i)
print(even)
print(uneven)