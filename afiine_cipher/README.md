# Affine Cipher

A Python implementation of the **Affine Cipher**, a type of
monoalphabetic substitution cipher built on a linear mathematical
function.

## How It Works

Each letter (converted to a number, A=0 ... Z=25) is transformed using:

```
E(x) = (a * x + b) mod 26      -> Encryption
D(y) = a⁻¹ * (y - b) mod 26     -> Decryption
```

Where:
- `a` and `b` form the encryption key
- `a⁻¹` is the modular multiplicative inverse of `a` modulo 26
- `a` **must be coprime with 26** (i.e. `gcd(a, 26) = 1`), otherwise the
  cipher cannot be reversed

Valid values for `a` include: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.
`b` can be any integer from 0-25.

Non-alphabetic characters are left unchanged, and letter case is
preserved.

**Example** (a = 5, b = 8):

```
Plaintext:  HELLO
Ciphertext: RCLLA
```

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only the Python standard library)

## Installation

1. Make sure Python 3 is installed:
   ```
   python3 --version
   ```
2. Navigate into this folder:
   ```
   cd affine_cipher
   ```

## Usage

### Interactive mode

```
python3 affine_cipher.py
```

Choose to **encrypt** or **decrypt**, then supply your keys `a` and `b`
when prompted. The program will raise an error if `a` is not a valid
(coprime) key.

### As a module

```python
from affine_cipher import encrypt, decrypt

cipher_text = encrypt("Hello, World!", a=5, b=8)
print(cipher_text)              # Rclla, Oaplx!

plain_text = decrypt(cipher_text, a=5, b=8)
print(plain_text)                # Hello, World!
```

## Notes

- If you choose an invalid `a` (not coprime with 26), the program will
  raise a `ValueError` explaining why.
- Like the Caesar cipher, the Affine cipher is easily broken with
  frequency analysis and is only suitable for learning purposes, not
  real-world security.
