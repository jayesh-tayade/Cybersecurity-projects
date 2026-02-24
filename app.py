import streamlit as st
import os
from encrypt import encrypt_file
from decrypt import decrypt_file

st.set_page_config(page_title="Secure File Locker")

st.title("🔐 Secure File Locker")
st.write("Hybrid Encryption using AES + RSA")

st.warning(
    "⚠️ Security Note: Private RSA key must be kept secret. "
    "Loss of private key means encrypted data cannot be recovered."
)   

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

# ---------------- ENCRYPT TAB ----------------
with tab1:
    uploaded_file = st.file_uploader(
        "Upload file to encrypt",
        type=["txt", "png", "jpg", "jpeg", "pdf"]
    )

    if uploaded_file:
        save_path = os.path.join("files", uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("File uploaded successfully")    

        original_size = os.path.getsize(save_path)
        st.write(f"📄 Original file size: {original_size} bytes")

        st.info("🔹 Step 1: Reading file as binary data")
        st.info("🔹 Step 2: Generating 256-bit AES key")
        st.info("🔹 Step 3: Encrypting file using AES (CBC mode)")
        st.info("🔹 Step 4: Encrypting AES key using RSA public key")
        st.info("🔹 Step 5: Saving encrypted file and encrypted key")

        if st.button("Encrypt File"):
            with st.spinner("Encrypting using AES + RSA..."):
                encrypted_path = encrypt_file(save_path)

            st.success("Encryption completed")

            with open(encrypted_path, "rb") as f:
                st.download_button(
                    "Download Encrypted File",
                    f,
                    file_name=os.path.basename(encrypted_path)
                )
                encrypted_size = os.path.getsize(encrypted_path)
                st.write(f"🔐 Encrypted file size: {encrypted_size} bytes")
        

# ---------------- DECRYPT TAB ----------------
with tab2:
    encrypted_upload = st.file_uploader(
        "Upload encrypted file",
        type=["enc"],
        key="decrypt"
    )

    if encrypted_upload:
        enc_path = os.path.join("files", encrypted_upload.name)

        with open(enc_path, "wb") as f:
            f.write(encrypted_upload.read())

        st.success("File uploaded successfully")

        st.info("🔹 Step 1: Loading RSA private key")
        st.info("🔹 Step 2: Decrypting AES key using RSA")
        st.info("🔹 Step 3: Decrypting file using AES")
        st.info("🔹 Step 4: Restoring original file format")

        if st.button("Decrypt File"):
            with st.spinner("Decrypting securely..."):
                decrypted_path = decrypt_file(enc_path)

            st.success("Decryption completed")

            with open(decrypted_path, "rb") as f:
                st.download_button(
                    "Download Decrypted File",
                    f,
                    file_name=os.path.basename(decrypted_path)
                )