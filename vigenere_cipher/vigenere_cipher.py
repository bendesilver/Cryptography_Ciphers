"""
Vigenere Cipher
---------------
A polyalphabetic substitution cipher that uses a keyword to shift
letters by varying amounts. Each letter of the keyword determines
the shift for the corresponding letter of the plaintext (A=0, B=1, ...).

Example:
    Plaintext:  H  E  L  L  O
    Key:        K  E  Y  K  E
    Shift:      10 4  24 10 4

Only alphabetic characters (A-Z, a-z) are shifted; the key cycles
over only the alphabetic characters in the text, so spaces and
punctuation are preserved without consuming a key letter.
"""

ALPHABET_SIZE = 26


def _clean_key(key: str) -> str:
    """Keep only alphabetic characters from the key, uppercased."""
    cleaned = ''.join(ch for ch in key if ch.isalpha()).upper()
    if not cleaned:
        raise ValueError("Key must contain at least one alphabetic character.")
    return cleaned


def encrypt(plaintext: str, key: str) -> str:
    """Encrypt plaintext using the Vigenere cipher with the given keyword."""
    key = _clean_key(key)
    result = []
    key_index = 0

    for char in plaintext:
        if char.isupper():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(char) - ord('A') + shift) % ALPHABET_SIZE + ord('A')))
            key_index += 1
        elif char.islower():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(char) - ord('a') + shift) % ALPHABET_SIZE + ord('a')))
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def decrypt(ciphertext: str, key: str) -> str:
    """Decrypt ciphertext using the Vigenere cipher with the given keyword."""
    key = _clean_key(key)
    result = []
    key_index = 0

    for char in ciphertext:
        if char.isupper():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(char) - ord('A') - shift) % ALPHABET_SIZE + ord('A')))
            key_index += 1
        elif char.islower():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(char) - ord('a') - shift) % ALPHABET_SIZE + ord('a')))
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def main():
    print("=== Vigenere Cipher ===")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ").strip()

    try:
        if choice == '1':
            text = input("Enter plaintext: ")
            key = input("Enter keyword: ")
            print(f"\nCiphertext: {encrypt(text, key)}")

        elif choice == '2':
            text = input("Enter ciphertext: ")
            key = input("Enter keyword: ")
            print(f"\nPlaintext: {decrypt(text, key)}")

        else:
            print("Invalid option.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
