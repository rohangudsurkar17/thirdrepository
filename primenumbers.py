num = 23

if num > 1:
    for i in range(2,num):
       if (num%i == 0):
           print("the number is not a prime number")
           break
    else:
       print("the number is a prime number")
else:
    print("the number is not a prime number")