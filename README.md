# 🔐 Secure File Locker using Hybrid Cryptography

## 📌 Description
This project implements a secure file encryption system using hybrid cryptography.
AES is used to encrypt files, RSA is used to encrypt the AES key, and SHA-256 is used
for password authentication.

## 🔑 Cryptography Algorithms Used
- AES (Symmetric Encryption)
- RSA (Asymmetric Encryption)
- SHA-256 (Password Hashing)

## Technologies Used
- Python
- PyCryptodome
- Streamlit

## 🏗️ How It Works
1. User sets a password (stored as SHA-256 hash)
2. File is encrypted using AES
3. AES key is encrypted using RSA public key
4. Decryption requires correct password and RSA private key

## RSA Key Generation

This project does not include RSA keys for security reasons.

Generate keys using the following Python code:

```python
from Crypto.PublicKey import RSA

key = RSA.generate(2048)

with open("keys/private.pem", "wb") as f:
    f.write(key.export_key())

with open("keys/public.pem", "wb") as f:
    f.write(key.publickey().export_key())
```
Place the generated keys inside the keys/ folder.

## How to Run
1. Install dependencies:
   pip install streamlit pycryptodome
2. Run the app:
   python -m streamlit run app.py