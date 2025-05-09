import hashlib
import random
from typing import List, Tuple, Union

class Cryptography:
    class RSA:
        @staticmethod
        def generate_keypair(bits: int = 1024) -> Tuple[Tuple[int, int], Tuple[int, int]]:
            """
            Generate RSA key pair.
            
            Args:
                bits: Key size in bits
                
            Returns:
                ((n, e), (n, d)) - public and private key pairs
            """
            def is_prime(n, k=5):
                """Miller-Rabin primality test."""
                if n <= 1:
                    return False
                if n <= 3:
                    return True
                if n % 2 == 0:
                    return False
                
                # Write n as 2^r * d + 1
                r, d = 0, n - 1
                while d % 2 == 0:
                    r += 1
                    d //= 2
                
                # Witness loop
                for _ in range(k):
                    a = random.randint(2, n - 2)
                    x = pow(a, d, n)
                    if x == 1 or x == n - 1:
                        continue
                    for _ in range(r - 1):
                        x = pow(x, 2, n)
                        if x == n - 1:
                            break
                    else:
                        return False
                return True
            
            def generate_prime(bits):
                """Generate a prime number with specified bit length."""
                while True:
                    p = random.getrandbits(bits)
                    # Ensure the number has the correct bit length
                    p |= (1 << bits - 1) | 1
                    if is_prime(p):
                        return p
            
            def gcd(a, b):
                """Calculate greatest common divisor."""
                while b:
                    a, b = b, a % b
                return a
            
            def mod_inverse(e, phi):
                """Calculate modular multiplicative inverse."""
                def extended_gcd(a, b):
                    if a == 0:
                        return b, 0, 1
                    else:
                        gcd, x, y = extended_gcd(b % a, a)
                        return gcd, y - (b // a) * x, x
                
                gcd, x, y = extended_gcd(e, phi)
                if gcd != 1:
                    raise ValueError("Modular inverse does not exist")
                else:
                    return x % phi
            
            # Generate two distinct primes
            p = generate_prime(bits // 2)
            q = generate_prime(bits // 2)
            while p == q:
                q = generate_prime(bits // 2)
            
            # Calculate n and phi
            n = p * q
            phi = (p - 1) * (q - 1)
            
            # Choose e
            e = 65537  # Common choice for e
            while gcd(e, phi) != 1:
                e += 2
            
            # Calculate d
            d = mod_inverse(e, phi)
            
            # Return public and private key pairs
            return ((n, e), (n, d))
        
        @staticmethod
        def encrypt(message: int, public_key: Tuple[int, int]) -> int:
            """
            Encrypt a message using RSA.
            
            Args:
                message: Integer message to encrypt
                public_key: (n, e) tuple
                
            Returns:
                Encrypted message
            """
            n, e = public_key
            if message >= n:
                raise ValueError("Message too large for the key size")
            return pow(message, e, n)
        
        @staticmethod
        def decrypt(ciphertext: int, private_key: Tuple[int, int]) -> int:
            """
            Decrypt a message using RSA.
            
            Args:
                ciphertext: Encrypted message
                private_key: (n, d) tuple
                
            Returns:
                Decrypted message
            """
            n, d = private_key
            return pow(ciphertext, d, n)
    
    @staticmethod
    def integer_factorization(n: int, method: str = "trial_division") -> List[int]:
        """
        Factor an integer into its prime components.
        
        Args:
            n: Integer to factorize
            method: Factorization method ('trial_division', 'pollard_rho')
            
        Returns:
            List of prime factors
        """
        if method == "trial_division":
            return Cryptography._trial_division(n)
        elif method == "pollard_rho":
            return Cryptography._pollard_rho(n)
        else:
            raise ValueError(f"Unknown factorization method: {method}")
    
    @staticmethod
    def _trial_division(n: int) -> List[int]:
        """Simple trial division factorization."""
        factors = []
        
        # Handle 2 separately
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Check odd numbers up to sqrt(n)
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        
        # If n is a prime greater than 2
        if n > 2:
            factors.append(n)
        
        return factors
    
    @staticmethod
    def _pollard_rho(n: int) -> List[int]:
        """Pollard's rho algorithm for integer factorization."""
        if n <= 1:
            return [n]
        
        if n % 2 == 0:
            return [2] + Cryptography._pollard_rho(n // 2)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def pollard_rho_factor(n):
            if n <= 1:
                return n
            if n % 2 == 0:
                return 2
            
            x = random.randint(1, n - 1)
            y = x
            c = random.randint(1, n - 1)
            d = 1
            
            def f(x):
                return (x * x + c) % n
            
            while d == 1:
                x = f(x)
                y = f(f(y))
                d = gcd(abs(x - y), n)
                
                if d == n:
                    return pollard_rho_factor(n)  # Try again with different values
            
            return d
        
        factors = []
        to_factor = [n]
        
        while to_factor:
            current = to_factor.pop()
            
            # Check if current is prime (simple primality test)
            is_prime = True
            for i in range(2, int(current**0.5) + 1):
                if current % i == 0:
                    is_prime = False
                    break
            
            if is_prime or current <= 3:
                factors.append(current)
            else:
                factor = pollard_rho_factor(current)
                to_factor.append(factor)
                to_factor.append(current // factor)
        
        return sorted(factors)
    
    @staticmethod
    def sha256(data: Union[str, bytes]) -> str:
        """
        Compute SHA-256 hash of data.
        
        Args:
            data: Input data (string or bytes)
            
        Returns:
            Hexadecimal digest
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha256(data).hexdigest()
    
    @staticmethod
    def sha512(data: Union[str, bytes]) -> str:
        """
        Compute SHA-512 hash of data.
        
        Args:
            data: Input data (string or bytes)
            
        Returns:
            Hexadecimal digest
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha512(data).hexdigest()
