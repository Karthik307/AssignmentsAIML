#5.Generate first N number of Fibonacci numbers. Take N value from the user
n = int(input("Enter n value? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
