from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")
KEYS_DIR = os.path.join(BASE_DIR, "keys")

def decrypt_file(encrypted_path):
    name = os.path.splitext(os.path.basename(encrypted_path))[0]

    encrypted_key_file = os.path.join(FILES_DIR, "aes_key.enc")
    ext_file = os.path.join(FILES_DIR, "file_ext.txt")

    # Read original extension
    with open(ext_file, "r") as f:
        ext = f.read()

    output_file = os.path.join(FILES_DIR, name + "_decrypted" + ext)

    # Load RSA private key
    with open(os.path.join(KEYS_DIR, "private.pem"), "rb") as f:
        private_key = RSA.import_key(f.read())

    # Decrypt AES key
    with open(encrypted_key_file, "rb") as f:
        encrypted_aes_key = f.read()

    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Read encrypted file
    with open(encrypted_path, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()

    # AES decryption
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher_aes.decrypt(ciphertext), AES.block_size)

    with open(output_file, "wb") as f:
        f.write(plaintext)

    return output_file