# Caesar Cipher

A Python implementation of the **Caesar Cipher**, one of the oldest and
simplest known encryption techniques. Each letter in the plaintext is
shifted a fixed number of places (the *key*) down the alphabet.

## How It Works

For a shift key `k`, every letter is mapped as:

```
E(x) = (x + k) mod 26
D(y) = (y - k) mod 26
```

Non-alphabetic characters (spaces, numbers, punctuation) are left
unchanged, and the cipher preserves letter case.

**Example** (key = 3):

```
Plaintext:  HELLO
Ciphertext: KHOOR
```

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only the Python standard library)

## Installation

1. Make sure Python 3 is installed on your system:
   ```
   python3 --version
   ```
2. Clone or download this project, then navigate into this folder:
   ```
   cd caesar_cipher
   ```

## Usage

### Interactive mode

Run the script directly and follow the on-screen prompts:

```
python3 caesar_cipher.py
```

You'll be able to choose between:
1. **Encrypt** a message
2. **Decrypt** a message
3. **Brute force** a ciphertext (tries all 26 possible keys, useful when
   the key is unknown)

### As a module

You can also import the functions into your own scripts:

```python
from caesar_cipher import encrypt, decrypt

cipher_text = encrypt("Hello, World!", key=3)
print(cipher_text)          # Khoor, Zruog!

plain_text = decrypt(cipher_text, key=3)
print(plain_text)           # Hello, World!
```

## Notes

- The key can be any integer; it is automatically reduced modulo 26.
- The Caesar cipher is **not secure** by modern standards — it can be
  broken instantly with a brute-force or frequency analysis attack. It
  is included here for educational purposes only.
