🔐 Secure Data Encryption System
This is a lightweight Streamlit web app that allows you to securely store and retrieve sensitive data using a title and passkey. Data is encrypted in memory and never saved to disk.

🚀 Features
🔐 Encrypt secrets with a passkey and store them under a title

🔓 Decrypt secrets by providing the correct title and passkey

🔁 Retry limit (3 attempts) before lockout

🧠 In-memory storage for privacy (data is lost when the app stops)

🔑 Admin login required to reset failed attempts

🧩 Technologies Used
Streamlit – for building the web interface

cryptography – for AES-based encryption using Fernet

hashlib – for hashing passkeys securely

🛠 Setup Instructions
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/data-encryption-system.git
cd data-encryption-system
2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
# On Windows:
venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If streamlit is not recognized, use:

bash
Copy
Edit
python -m streamlit run app.py
4. Run the App
bash
Copy
Edit
streamlit run app.py
Or (if the above doesn’t work):

bash
Copy
Edit
python -m streamlit run app.py
📂 App Structure
text
Copy
Edit
data-encryption-system/
│
├── app.py              # Main Streamlit app
├── README.md           # This file
└── requirements.txt    # Python dependencies
🔑 Default Master Password
To unlock the app after 3 failed attempts, use:

nginx
Copy
Edit
admin123
You can change this inside app.py for better security.

🔒 Disclaimer
This app is for educational/demo purposes only. It does not persist data or offer real-world security guarantees. Use production-ready security methods for sensitive information in real apps.

✅ To-Do / Future Improvements
 Add persistent storage (e.g., SQLite or JSON)

 Use passkey-derived encryption instead of single session key

 Export/import stored data

 User login system

📜 License
MIT License (or whatever license you prefer)

💡 Example Usage
To Store a Secret:

Title: EmailPassword

Secret: myS3cr3t!

Passkey: 1234

To Retrieve it:

Enter Title: EmailPassword

Enter Passkey: 1234

And you'll get back myS3cr3t!
