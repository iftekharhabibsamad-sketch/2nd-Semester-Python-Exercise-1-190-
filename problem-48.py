#Determine the largest number among the three numbers.
n_1=float(input("Enter the 1st number :"))
n_2=float(input("Enter the 2nd number :"))
n_3=float(input("Enter the 3rd number :"))
if n_1>n_2 and n_1>n_3:
    print(n_1,"is largest")
elif n_2>n_1 and n_2>n_3:
    print(n_2,"is largest")
else :
    print(n_3,"is largest")