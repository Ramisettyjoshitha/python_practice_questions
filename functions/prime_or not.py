def prime(n):
    i=2
    is_prime=True
    while n>i:
        if n%i==0:
            is_prime=False
            break
        i+=1
    if is_prime and n>1:
        return "it is prime number"
    else:
        return "not prime"
print(prime(100))
          
    

    