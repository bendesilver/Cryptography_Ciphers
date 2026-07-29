# Classical Cryptography Ciphers

A collection of classical (pre-modern) cipher implementations written
in Python, built as part of my **Cryptography course in Semester 6**.

## About This Project

As part of the cryptography course I'm studying this semester, I took
it upon myself to build clean, well-documented implementations of
three classic ciphers instead of just studying them on paper. Working
through the math and edge cases (like figuring out modular inverses
for the Affine cipher, or handling key alignment for the Vigenere
cipher) helped me understand these algorithms far better than reading
about them alone. This repository is the result — a small,
self-contained collection I can refer back to and share.

## Ciphers Included

| Cipher | Type | Folder |
|---|---|---|
| **Caesar Cipher** | Monoalphabetic substitution (single shift) | [`caesar_cipher/`](./caesar_cipher) |
| **Affine Cipher** | Monoalphabetic substitution (linear function) | [`affine_cipher/`](./affine_cipher) |
| **Vigenere Cipher** | Polyalphabetic substitution (keyword-based) | [`vigenere_cipher/`](./vigenere_cipher) |

Each cipher lives in its own folder with:
- A standalone Python script (with both an interactive CLI and
  importable functions)
- Its own `README.md` covering how the cipher works, installation, and
  usage instructions

## Project Structure

```
cryptography-ciphers-project/
├── README.md                      <- you are here
├── caesar_cipher/
│   ├── caesar_cipher.py
│   └── README.md
├── affine_cipher/
│   ├── affine_cipher.py
│   └── README.md
└── vigenere_cipher/
    ├── vigenere_cipher.py
    └── README.md
```

## Requirements

- Python 3.6 or higher
- No third-party dependencies — every cipher relies only on the
  Python standard library

## Getting Started

1. Clone or download this repository.
   ```
   https://github.com/bendesilver/Cryptography_Ciphers.git
   ```
2. Navigate into whichever cipher folder you'd like to try, e.g.:
   ```
   cd caesar_cipher
   python3 caesar_cipher.py
   ```
3. Refer to that folder's `README.md` for detailed usage instructions
   and code examples.

## Disclaimer

These ciphers are **classical algorithms built for learning purposes
only**. They are not secure by modern cryptographic standards and
should never be used to protect real, sensitive data. For actual
security needs, use established modern algorithms (e.g. AES, RSA)
through well-vetted libraries.

## Author's Note

This project reflects my own learning process for my Semester 6
cryptography course — I built it to strengthen my grasp of classical
cipher mathematics before moving on to modern cryptographic systems.
Feedback and suggestions are always welcome!
