print("_"*80)
print("---------------------------Welcome to Movie Ticket Booking----------------------")
print("_"*80)


print("Please Enter your Age :")
age=int(input())

if(age <=5 ):
    print("Free Entry")
elif(age > 5 and age <= 18):
    print("Tikit price : 900")
elif(age > 18 and age <= 40):
    print("Tikit price : 1200")
else:
    print("Tikit Price : 500")