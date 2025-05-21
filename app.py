import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# --- Session State Setup ---
if 'KEY' not in st.session_state:
    st.session_state.KEY = Fernet.generate_key()
cipher = Fernet(st.session_state.KEY)

if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'authorized' not in st.session_state:
    st.session_state.authorized = True

# --- Utility Functions ---
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_secret(secret):
    return cipher.encrypt(secret.encode()).decode()

def decrypt_secret(encrypted_secret):
    return cipher.decrypt(encrypted_secret.encode()).decode()

# --- Streamlit UI ---
st.title("🔐 Title-Based Secret Storage")

menu = ["Home", "Store Secret", "Retrieve Secret", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# --- Home ---
if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Securely store secrets using a title and passkey. Retrieve them later using the same combination.")

# --- Store Secret ---
elif choice == "Store Secret":
    st.subheader("📂 Store a Secret")

    title = st.text_input("Title:")
    secret = st.text_area("Secret:")
    passkey = st.text_input("Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if title and secret and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_secret = encrypt_secret(secret)

            st.session_state.stored_data[title] = {
                "encrypted_secret": encrypted_secret,
                "hashed_passkey": hashed_passkey
            }

            st.success(f"✅ Secret stored under title: '{title}'")
        else:
            st.error("⚠️ All fields are required!")

# --- Retrieve Secret ---
elif choice == "Retrieve Secret":
    if not st.session_state.authorized:
        st.warning("🔒 Please reauthorize before continuing.")
        st.rerun()

    st.subheader("🔍 Retrieve a Secret")

    title = st.text_input("Title:")
    passkey = st.text_input("Passkey:", type="password")

    if st.button("Retrieve"):
        data = st.session_state.stored_data.get(title)
        if data:
            if hash_passkey(passkey) == data['hashed_passkey']:
                decrypted_secret = decrypt_secret(data['encrypted_secret'])
                st.success("✅ Secret retrieved successfully!")
                st.code(decrypted_secret)
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.session_state.authorized = False
                    st.warning("🚫 Too many failed attempts! Redirecting to login...")
                    st.rerun()
        else:
            st.error("❌ Title not found!")

# --- Login Page ---
elif choice == "Login":
    st.subheader("🔑 Reauthorization")
    master_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if master_pass == "admin123":  # Replace with env var or secrets in production
            st.session_state.authorized = True
            st.session_state.failed_attempts = 0
            st.success("✅ Reauthorized! You can now retrieve secrets.")
            st.rerun()
        else:
            st.error("❌ Incorrect master password.")
