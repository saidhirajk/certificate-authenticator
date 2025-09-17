import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="Certificate Authenticity Checker", layout="centered")

# Sidebar
st.sidebar.image("https://static.vecteezy.com/system/resources/previews/020/045/181/original/verified-checkmark-sign-icon-symbol-logo-green-design-free-vector.jpg", width=100)
st.sidebar.title("Certificates secured by Blockchain")
st.sidebar.markdown("""
This tool helps verify certificates/documents (academic) using simulated AI and database checks.
""")
test_case = st.sidebar.selectbox("🧪 Choose Test Case", ["Both Pass", "Hash Pass, DB Fail", "Hash Fail, DB Pass"])

# Main Title
st.title("📄 CertiChain")

# Step 1: Upload Screen
st.header("Upload the Certificate/Document")
uploaded_file = st.file_uploader("Upload Certificate (PDF/JPEG)", type=["pdf", "jpg", "jpeg", "png"])

st.divider()

# Step 2: Extracted Details + Verification
if uploaded_file:
    if st.button("Check Authenticity"):
        st.header("Extracted Details (Simulated OCR)")
        st.markdown("✅ Certificate uploaded successfully. Extracting details...")

        # Simulated extracted data
        extracted_name = "Rahul Sharma"
        extracted_roll = "JH2025-001"
        extracted_marks = "82%"

        time.sleep(2)
        st.write(f"**👤 Name:** {extracted_name}")
        st.write(f"**🆔 Roll No:** {extracted_roll}")
        st.write(f"**📊 Marks:** {extracted_marks}")

        st.divider()

        # Step 3A: Hash Verification
        st.subheader("🔗Hash Verification")
        simulated_hash = "abc123xyz"
        valid_hashes = ["abc123xyz", "def456uvw", "ghi789rst"]

        st.write("🔍 Verifying hash against trusted records...")
        time.sleep(3)
        st.write(f"Extracted Hash: `{simulated_hash}`")

        hash_pass = simulated_hash in valid_hashes
        if test_case == "Hash Fail, DB Pass":
            hash_pass = False

        if hash_pass:
            st.success("✅ Hash matched. Hash Verification Successful.")
        else:
            st.error("❌ Hash mismatch. Possible forgery.")

        st.divider()

        # Step 3B: Database Verification
        st.subheader("Database Verification")
        mock_db = {
            "JH2025-001": {"name": "Rahul Sharma", "marks": "82%"},
            "JH2025-002": {"name": "Priya Verma", "marks": "76%"},
            "JH2025-003": {"name": "Amit Singh", "marks": "89%"}
        }

        st.write("🔍 Checking certificate details in database...")
        time.sleep(5)

        db_pass = extracted_roll in mock_db and mock_db[extracted_roll]["name"] == extracted_name
        if test_case == "Hash Pass, DB Fail":
            db_pass = False

        if db_pass:
            st.success("✅ Certificate matched with database. .")
        else:
            st.error("❌ Certificate details do not match database. Possible forgery.")

        st.divider()

        # Final Verdict
        st.subheader("🧾 Final Verdict")
        if hash_pass and db_pass:
            st.success("✅ Certificate is authentic. Verified against all checks.")
            st.image("https://static.vecteezy.com/system/resources/previews/020/045/181/original/verified-checkmark-sign-icon-symbol-logo-green-design-free-vector.jpg", width=150)

        else:
            st.error("❌ Certificate failed one or more checks. Manual review recommended.")
            st.image("https://th.bing.com/th/id/OIP.qPwszvHoCv8_7jffgfzVbwHaHa?w=198&h=198&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3", width=150)


        st.caption("Demo by Saidhiraj • Smart India Hackathon 2025")
