num_1 = int (input("Enter 1st no:"))
num_2 = int (input("Enter 2nd no:"))
choice = input("Enter the opeartion + - * /")
if choice == "+" :
    sum = num_1+num_2
    print(type(num_1))
    print("the sum of two nos.:", sum)
if choice == "-" :   
    subs = num_1-num_2
    print ("The division of two nos is :", subs)
if choice == "*" :
    mul =num_1*num_2
    print("the multiplication of 2 nos is:",mul)
if choice == "/" :
    div =num_1/num_2
    print("the of two nos is:",div)
else:
    print("Invalid opearation")
