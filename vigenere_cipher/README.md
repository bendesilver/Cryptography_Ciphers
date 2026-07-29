# Vigenere Cipher

A Python implementation of the **Vigenere Cipher**, a polyalphabetic
substitution cipher that uses a repeating keyword to shift each letter
of the plaintext by a different amount.

## How It Works

Each letter of the keyword determines the shift applied to the
corresponding letter of the plaintext (A=0, B=1, ... Z=25). The
keyword repeats as many times as needed to cover the whole message.

```
Plaintext:  H  E  L  L  O
Key:        K  E  Y  K  E
Shift:      10 4  24 10 4
Ciphertext: R  I  J  V  S
```

- Only alphabetic characters are shifted; the key only advances on
  alphabetic characters, so spaces and punctuation don't throw off the
  key alignment.
- Letter case is preserved in the output.
- The key itself may contain spaces or mixed case — only its letters
  are used, and they're automatically converted to uppercase
  internally.

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
   cd vigenere_cipher
   ```

## Usage

### Interactive mode

```
python3 vigenere_cipher.py
```

Choose to **encrypt** or **decrypt** and enter your keyword when
prompted.

### As a module

```python
from vigenere_cipher import encrypt, decrypt

cipher_text = encrypt("Hello, World!", key="KEY")
print(cipher_text)             # Rijvs, Uyvjn!

plain_text = decrypt(cipher_text, key="KEY")
print(plain_text)               # Hello, World!
```

## Notes

- The keyword must contain at least one alphabetic character, or a
  `ValueError` will be raised.
- The Vigenere cipher was historically considered "unbreakable" for
  centuries, but it can be broken with techniques like the
  Kasiski examination or index of coincidence analysis once the key
  length is known. Included here for educational purposes.
