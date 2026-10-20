#list all the variable we need to use in this function

expenses = []
expense = 1
num_expense = 0
total = 0

small_expense = []
large_expense = []
moderate_epxense = []

# we need a loop for users to input all information they want to input
while expense != 0:

    expense = float(input("Enter an expense or 0 to finish:"))
# in case num_expense including 0, we need "if" here to make sure expense != 0 so we can add it in our expense list
    if expense != 0:
        num_expense += 1
        expenses.append(expense)

# since we have input all the elements to the lise

# now we need to sort all numbers in this list

# firstly, we need to select one number in the list that we can campare that we can find thoes bigges and smallest numbers, and this number could be anyone in this list

for i in expenses:
    total += i 
    if i < 25:
        small_expense.append(i)

    elif i <= 100:
        moderate_epxense.append(i)

    else:
        large_expense.append(i)


# now, we need to slect the smallest number in small_expense list
# however, we have to make sure there are elements in it, so we need using if function to see does expense list have any elements = wether len(expenses) >0
if len(expenses) > 0:

    average = total/num_expense

    for i in expenses:

        lowest = expenses[0]
        highest = expenses[0]

        if i < lowest:
            lowest = i

        elif i > highest:
            highest = i
else:
    average = 0
    lowest = 0
    highest = 0
    


#now we just have to print everything out
print("Expense Summary")
print("---------------")
print(f"Number of expenses: {num_expense}")

print(f"Total: {total}")

print(f"Average: {average}")

print(f"Smallest expense: {lowest}")

print(f"Largest expense: {highest}")

print("")

print(f"Small expenses: {len(small_expense)}\nModerate expenses: {len(moderate_epxense)}\n Large expenses: {len(large_expense)}\n")