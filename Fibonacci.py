def fibonacci (n):
    if n == 0 or n == 1:
        return 1

    return fibonacci (n - 1) + fibonacci (n-2) 

# Forma iterativa
 
def fib (n):
    a = 0
    b = 1

    for k in range (n):
        c = a+b
        a = b
        b = c

    return b 

  # Forma Recursiva

def fib_r (n):
    if n == 0 or n == 1:
        return n 

    return fibonacci (n - 1) + fibonacci (n-2)  


for x in range(20):
    print (fib_r(x))