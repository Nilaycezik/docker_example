def fibonacci_series(n):
   if n <= 1:
       return n
   else:
       return(fibonacci_series(n-1) + fibonacci_series(n-2))

nterms = 15

print("Fibonacci sequence:")
for i in range(nterms):
    print(fibonacci_series(i))