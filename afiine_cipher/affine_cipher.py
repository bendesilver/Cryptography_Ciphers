# Affine Cipher
# A monoalphabetic substitution cipher based on the mathematical
# function:

#   E(x) = (a * x + b) mod m

# where:
#   x = the numerical value of the plaintext letter (A=0, B=1, ..., Z=25)
#   a, b = the key (a must be coprime with m, i.e. gcd(a, m) = 1)
#   m = size of the alphabet (26)

# Decryption uses the modular inverse of 'a':

#   D(y) = a_inverse * (y - b) mod m

# Only alphabetic characters (A-Z, a-z) are transformed. All other
# characters are left unchanged.


ALPHABET_SIZE = 26


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a: int, m: int) -> int:
    """Return the modular multiplicative inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse exists for a={a} under modulo {m}.")


def validate_key(a: int) -> None:
    """Ensure 'a' is coprime with the alphabet size, otherwise the cipher is not invertible."""
    if gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError(
            f"Key 'a'={a} is not valid. 'a' must be coprime with {ALPHABET_SIZE} "
            f"(gcd(a, {ALPHABET_SIZE}) must equal 1)."
        )


def encrypt(plaintext: str, a: int, b: int) -> str:
    """Encrypt plaintext using the Affine cipher with keys a and b."""
    validate_key(a)
    result = []

    for char in plaintext:
        if char.isupper():
            x = ord(char) - ord('A')
            result.append(chr((a * x + b) % ALPHABET_SIZE + ord('A')))
        elif char.islower():
            x = ord(char) - ord('a')
            result.append(chr((a * x + b) % ALPHABET_SIZE + ord('a')))
        else:
            result.append(char)

    return ''.join(result)


def decrypt(ciphertext: str, a: int, b: int) -> str:
    """Decrypt ciphertext using the Affine cipher with keys a and b."""
    validate_key(a)
    a_inv = mod_inverse(a, ALPHABET_SIZE)
    result = []

    for char in ciphertext:
        if char.isupper():
            y = ord(char) - ord('A')
            result.append(chr((a_inv * (y - b)) % ALPHABET_SIZE + ord('A')))
        elif char.islower():
            y = ord(char) - ord('a')
            result.append(chr((a_inv * (y - b)) % ALPHABET_SIZE + ord('a')))
        else:
            result.append(char)

    return ''.join(result)


def main():
    print("=== Affine Cipher ===")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ").strip()

    try:
        if choice == '1':
            text = input("Enter plaintext: ")
            a = int(input("Enter key 'a' (must be coprime with 26): "))
            b = int(input("Enter key 'b': "))
            print(f"\nCiphertext: {encrypt(text, a, b)}")

        elif choice == '2':
            text = input("Enter ciphertext: ")
            a = int(input("Enter key 'a' (must be coprime with 26): "))
            b = int(input("Enter key 'b': "))
            print(f"\nPlaintext: {decrypt(text, a, b)}")

        else:
            print("Invalid option.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
