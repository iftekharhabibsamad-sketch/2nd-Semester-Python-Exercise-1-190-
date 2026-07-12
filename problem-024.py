#Using logical oparetor
a=int(input("Enter the 1st number ="))

b=int(input("Enter the 2nd number ="))

c=int(input("Enter the 3rd number ="))

if a>b and a>c:
	print("largest Number is =",a)
	
elif b>a and b>c:
	print("largest Number is =",b)
	
else:
	print("largest Numver is =",c)
	
#practice
today_holiday =input("Is today a holiday?(yes/no): ")
is_sick =input("are you sick (yes/no):")

if today_holiday=="yes" or is_sick=="yes":
    print("I don't have to go to college today.")
else:
    print("I have to go today.")
