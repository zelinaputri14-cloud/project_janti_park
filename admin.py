import streamlit as st
import pandas as pd
import os
from data import load_admin

# ===== CONFIG =====
st.set_page_config(page_title="Admin Panel", layout="centered")

DATA_FILE = "database_pengunjung.xlsx"

# ===== SESSION INIT (WAJIB) =====
if "login" not in st.session_state:
    st.session_state.login = False

if "admin_user" not in st.session_state:
    st.session_state.admin_user = None


# ===== LOAD DATA =====
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_excel(DATA_FILE)
    else:
        return pd.DataFrame(columns=[
            "bulan_ke",
            "jumlah_pengunjung",
            "akhir_pekan",
            "libur_nasional"
        ])


# ===== STYLE =====
def load_style():
    st.markdown("""
    <style>
    #MainMenu, footer, header {
        visibility: hidden;
    }
    .login-container {
        max-width: 380px;
        margin: auto;
        margin-top: 80px;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
    }
    .subtitle {
        font-size: 14px;
        color: #9ca3af;
        margin-bottom: 25px;
    }
    .stButton button {
        width: 100%;
        border-radius: 10px;
        background-color: #22c55e;
        color: white;
        font-weight: bold;
        padding: 12px;
    }
    </style>
    """, unsafe_allow_html=True)


# ===== LOGIN PAGE =====
def login_page():
    load_style()

    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    st.markdown(
        '<div class="title">🔐 Admin Login</div>',
        unsafe_allow_html=True
    )

    st.info(
    """
    Ketentuan akun admin:
    - Username maksimal 20 karakter
    - Username hanya menggunakan huruf kecil
    - Password harus 8 karakter
    - Password hanya menggunakan huruf kecil dan angka
    """
    )

    username = st.text_input(
        "Username",
        placeholder="contoh: adminjanti"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="contoh: admin1234"
    )

    if st.button("Login"):

        # Validasi Username
        if len(username) > 20:
            st.error("Username maksimal 20 karakter ❌")

        elif not username.islower() or not username.isalpha():
            st.error("Username hanya boleh menggunakan huruf kecil ❌")

        # Validasi Password
        elif len(password) < 8:
            st.error("Password minimal 8 karakter ❌")

        elif not password.islower() or not password.isalnum():
            st.error(
                "Password hanya boleh menggunakan huruf kecil dan angka ❌"
            )

        else:
            df = load_admin()

            if (
                (df["username"] == username)
                & (df["password"] == password)
            ).any():

                st.session_state.login = True
                st.session_state.admin_user = username
                st.rerun()

            else:
                st.error("Username atau password salah ❌")

    st.markdown('</div>', unsafe_allow_html=True)


# ===== ADMIN DASHBOARD =====
def admin_page():
    load_style()

    st.title("📊 Dashboard Admin")
    st.success(f"Login sebagai: {st.session_state.admin_user}")

    df = load_data()

    st.subheader("📋 Kelola Data Training")

    edited_df = st.data_editor(
        df,
        num_rows="dynamic",
        use_container_width=True
    )

    if st.button("💾 Simpan Data"):
        edited_df.to_excel(DATA_FILE, index=False)
        st.success("Data berhasil disimpan ✅")

    st.divider()

    if st.button("Logout"):
        st.session_state.login = False
        st.session_state.admin_user = None
        st.rerun()


# ===== MAIN FUNCTION =====
def show_admin():
    if st.session_state.login:
        admin_page()
    else:
        login_page()
