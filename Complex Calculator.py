A = input(
    "Type of operation: \n"
     "Addition: 1 \n"
     "Subtraction: 2 \n"
     "Multiplication: 3 \n"
     "Division: 4 \n"
    )

num_of_ops = int(input("How many numbers will you operate?"))
if A == "1":
    num = float(input("Give number:"))
    answer = num
    for x in range(num_of_ops-1):
        num = float(input("Give number:"))
        answer = answer + num
elif A == "2":
    for x in range(num_of_ops):
        num = float(input("Give number:"))
        x =  - x
elif A == "3":
    for x in range(num_of_ops):
        num = float(input("Give number:"))
        x = x * x
elif A == "4":
    for x in range(num_of_ops):
        num = float(input("Give number:"))
        x = x / x
print("The answer is", x )