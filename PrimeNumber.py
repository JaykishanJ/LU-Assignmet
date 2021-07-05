

N=int(input("enter number:"))
if N>1:
  for i in range(2,N,):
    if (N%i)==0:
      print("Enter numbber is not prime number")
      break
  else:
    print("Enter number is prime number")
