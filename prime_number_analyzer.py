a=int(input("enter the number:"))
# to check if the number is negative or less than 1 it shows it's not a prime number
if(a<2):
    print("the given number is not a prime number")
else:
    #condition to check if it is prime or not
    for i in range(2,a):
        if(a%i==0):
            print("the given number is not a prime number")
            break
    else:
            print("the given number is a prime number")