#Swapping without temporary variable (Pythonic way)
number_1=int(input("Enter the 1st number.="))
number_2=float(input("Enter the 2nd number.="))

print("befor the swap number_1 =",number_1,"number_2 =",number_2 )

number_1,number_2 = number_2,number_1

print("After the swap number_1 =",number_1,"number_2 =",number_2)
#Arithmetic Swapping Logic(using mul and div)
a=int(input("Enter the value of a ="))
b=int(input("Enter the value of b ="))
a=a*b;b=a/b;a=a/b
print("After the swap a=",a,"b =",b)