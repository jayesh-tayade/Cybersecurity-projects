from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")
KEYS_DIR = os.path.join(BASE_DIR, "keys")

def encrypt_file(input_path):
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)

    encrypted_file = os.path.join(FILES_DIR, name + ".enc")
    encrypted_key_file = os.path.join(FILES_DIR, "aes_key.enc")
    ext_file = os.path.join(FILES_DIR, "file_ext.txt")

    # Read RSA public key
    with open(os.path.join(KEYS_DIR, "public.pem"), "rb") as f:
        public_key = RSA.import_key(f.read())

    # Read file data
    with open(input_path, "rb") as f:
        data = f.read()

    # Generate AES key
    aes_key = get_random_bytes(32)

    # AES encryption
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    ciphertext = cipher_aes.encrypt(pad(data, AES.block_size))

    # Save encrypted file
    with open(encrypted_file, "wb") as f:
        f.write(cipher_aes.iv)
        f.write(ciphertext)

    # Encrypt AES key using RSA
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    with open(encrypted_key_file, "wb") as f:
        f.write(encrypted_aes_key)

    # Save extension
    with open(ext_file, "w") as f:
        f.write(ext)

    return encrypted_file