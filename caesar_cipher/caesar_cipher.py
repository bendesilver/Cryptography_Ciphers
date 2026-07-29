"""
Caesar Cipher
-------------
A simple substitution cipher that shifts each letter in the plaintext
by a fixed number of positions ('key') down the alphabet.

Example (key = 3):
    A -> D, B -> E, C -> F ... Z -> C

Only alphabetic characters (A-Z, a-z) are shifted. All other
characters (numbers, spaces, punctuation) are left unchanged.
"""

ALPHABET_SIZE = 26


def encrypt(plaintext: str, key: int) -> str:
    """Encrypt plaintext using the Caesar cipher with the given key (shift)."""
    key = key % ALPHABET_SIZE
    result = []

    for char in plaintext:
        if char.isupper():
            shifted = (ord(char) - ord('A') + key) % ALPHABET_SIZE
            result.append(chr(shifted + ord('A')))
        elif char.islower():
            shifted = (ord(char) - ord('a') + key) % ALPHABET_SIZE
            result.append(chr(shifted + ord('a')))
        else:
            result.append(char)

    return ''.join(result)


def decrypt(ciphertext: str, key: int) -> str:
    """Decrypt ciphertext using the Caesar cipher with the given key (shift)."""
    return encrypt(ciphertext, -key)


def brute_force(ciphertext: str) -> None:
    """Print all 26 possible shifts to help crack a ciphertext without the key."""
    for key in range(ALPHABET_SIZE):
        print(f"Key {key:2d}: {decrypt(ciphertext, key)}")


def main():
    print("=== Caesar Cipher ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute force (try all keys)")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        text = input("Enter plaintext: ")
        key = int(input("Enter key (integer shift): "))
        print(f"\nCiphertext: {encrypt(text, key)}")

    elif choice == '2':
        text = input("Enter ciphertext: ")
        key = int(input("Enter key (integer shift): "))
        print(f"\nPlaintext: {decrypt(text, key)}")

    elif choice == '3':
        text = input("Enter ciphertext: ")
        print()
        brute_force(text)

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
