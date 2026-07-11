#Using quotient
num_1=int(input("Enter the 1st number :"))
num_2=int(input("Enter the 2nd number :"))
quotient=num_1//num_2
print("quotient (num_1//num_2) :",quotient)

#practice

# A shopkeeper has 57 eggs. Each egg tray holds 12 eggs.
# How many full trays can be filled? How many eggs will remain?

eggs =57
tray_size=12

full_trays=eggs//tray_size
remainder=eggs%tray_size

print("Number of full trays:",full_trays)
print("Remaining eggs:",remainder)