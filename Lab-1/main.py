def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: Integer to check
    
    Returns:
        Boolean: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(limit):
    """
    Generate all prime numbers up to a given limit using Sieve of Eratosthenes.
    
    Args:
        limit: Upper bound for prime generation
    
    Returns:
        List of prime numbers up to limit
    """
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, limit + 1) if sieve[i]]


def prime_factorization(n):
    """
    Get prime factorization of a number.
    
    Args:
        n: Integer to factorize
    
    Returns:
        List of prime factors
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


# Main execution
if __name__ == "__main__":
    # Test: Check if numbers are prime
    print("=== Prime Checker ===")
    test_numbers = [2, 15, 17, 20, 29]
    for num in test_numbers:
        print(f"{num} is prime: {is_prime(num)}")
    
    # Test: Get all primes up to 50
    print("\n=== Primes up to 50 ===")
    primes = get_primes_up_to(50)
    print(primes)
    
    # Test: Prime factorization
    print("\n=== Prime Factorization ===")
    test_factorize = [12, 30, 97]
    for num in test_factorize:
        factors = prime_factorization(num)
        print(f"Prime factors of {num}: {factors}")
