#How to determine if a year is a Leap Year.
y=float(input("Enter Year :"))
if (y%400==0)or(y%4==0 and y%100!=0):
    print(y,"= is leap year.")
else:
    print(y,"=is not leap year.")