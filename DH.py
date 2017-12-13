import math
import random
 

def main():
    while 1:
        n = int(input("n: "))
        g = int(input("g: "))
        if not (is_prime(n) and is_prime(g)):
            raise ValueError('Both numbers must be prime.')
        elif n == g:
            raise ValueError('n and g cannot be equal')
        elif n < g:
            raise ValueError('n < g')
        
     
        aliceSecret = secret()    # a
        bobSecret = secret()      # b

        # Begin
        print( "Publicly Variables:")
        print( "    Publicly Prime: " , n )
        print( "    Publicly Base:  " , g )
         
        # Alice Sends Bob A = g^a mod p
        A = (g**aliceSecret) % n
        print( "\n  Alice Sends Over Public Chanel: " , A )
         
        # Bob Sends Alice B = g^b mod p
        B = (g ** bobSecret) % n
        print( "  Bob Sends Over Public Chanel: ", B )
         
        print( "\n------------\n" )
        print( "Privately Calculated Shared Secret:" )
        # Alice Computes Shared Secret: s = B^a mod p
        aliceSharedSecret = (B ** aliceSecret) % n
        print( "    Alice Shared Secret: ", aliceSharedSecret )
         
        # Bob Computes Shared Secret: s = A^b mod p
        bobSharedSecret = (A**bobSecret) % n
        print( "    Bob Shared Secret: ", bobSharedSecret )

    

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def secret ():
    secret = int(random.randint(0,100))
    return secret

if __name__ == "__main__":
    main()
