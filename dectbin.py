#4.Decimal to binay
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

dec=int(input("a:"))

convertToBinary(dec)
print()
