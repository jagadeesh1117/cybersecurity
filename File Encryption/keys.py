import random

def generate_keys():
    # Generate two distinct prime numbers
    p = generate_prime_number()
    q = generate_prime_number()

    # Compute n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Find e, a number coprime to phi_n
    e = find_coprime(phi_n)

    # Compute the modular inverse of e modulo phi_n
    d = modular_inverse(e, phi_n)

    # Return public and private keys
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def generate_prime_number():
    while True:
        prime_candidate = random.randint(2**8, 2**16)
        if is_prime(prime_candidate):
            return prime_candidate

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_coprime(phi_n):
    while True:
        coprime_candidate = random.randint(2, phi_n)
        if gcd(coprime_candidate, phi_n) == 1:
            return coprime_candidate

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modular_inverse(a, m):
    # Extended Euclidean Algorithm
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            (u1 - q * v1),
            (u2 - q * v2),
            (u3 - q * v3),
            v1,
            v2,
            v3,
        )
    return u1 % m

# Example usage
public_key, private_key = generate_keys()
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)
