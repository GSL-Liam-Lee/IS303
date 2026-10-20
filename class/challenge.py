num = int(input("How many numbers do u wanna input?"))
nums = []

for i in range(num):
    place = i+1
    a = input(f"what's the {place}th number?")
    nums.append(a)

total = 0
negative = []
positive = []
for a in nums:
    total += int(a)
    if a >= 0:
        positive.append(a)
    else:
        negative.append(a)

print(nums)
print(total)
print(negative)
print(positive)