#add two number
def twonumber(a,b):
  sum=a+b
  print(sum)

twonumber(4,5)

def factorial(n):
   fact=1
   for i in range(1,n+1):
    fact *= i

   return fact

result=factorial(5)
print(result)


