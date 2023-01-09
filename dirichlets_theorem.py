def dirichlets_theorem(a, b):
    # Assume that there are only finitely many prime numbers satisfying p ≡ a (mod b)
    # Let S be the set of such prime numbers
    S = []
    
    # Check all prime numbers starting from the smallest prime (2)
    p = 2
    while True:
        # If p ≡ a (mod b), add it to S
        if p % b == a:
            S.append(p)
        
        # Check the next prime number
        p = next_prime(p)
        
        # If the size of S is greater than or equal to b, there are at least b prime numbers satisfying p ≡ a (mod b)
        if len(S) >= b:
            # Let k be any integer such that k ≥ b
            k = b
            while True:
                # Show that a + bk is prime by showing that it is not divisible by any element of S
                is_prime = True
                for s in S:
                    if (a + b * k) % s == 0:
                        is_prime = False
                        break
                
                # If a + bk is prime, it is a counterexample to the assumption that there are only finitely many prime numbers satisfying p ≡ a (mod b)
                if is_prime:
                    print(f"Counter-example found: a = {a}, b = {b}, k = {k}")
                    return
                
                # Increment k and try again
                k += 1

def next_prime(n):
    """Returns the smallest prime number greater than n"""
    # Check odd numbers starting from n + 1
    for i in range(n + 1, n + 1000000, 2):
        # If i is prime, return it
        if is_prime(i):
            return i

def is_prime(n):
    """Returns True if n is prime, False otherwise"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
       
