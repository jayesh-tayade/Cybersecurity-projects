# 🔐 Secure File Locker using Hybrid Cryptography

## 📌 Description
This project implements a secure file encryption system using a hybrid cryptographic approach.
AES is used for fast file encryption, while RSA is used to securely encrypt the AES key.
The system is visualized using a Streamlit-based web interface.

## 🔑 Cryptography Algorithms Used
- AES (Symmetric Encryption)
- RSA (Asymmetric Encryption)

## Technologies Used
- Python
- PyCryptodome
- Streamlit

## 🏗️ How It Works
1. User uploads a file through the Streamlit interface
2. The file is encrypted using AES (CBC mode)
3. The AES key is encrypted using RSA public key
4. Encrypted file and encrypted AES key are stored securely
5. Decryption uses the RSA private key to restore the original file

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

### 📌 Security Notes
- Private RSA keys must never be shared
- Loss of private key results in permanent data loss
- Files are processed in binary mode to prevent corruption