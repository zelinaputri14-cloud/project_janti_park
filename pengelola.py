import streamlit as st
import pandas as pd
from data import load_admin

PENGELOLA_PASSWORD = "pengelola123"
ADMIN_FILE = "admin_accounts.xlsx"

# ===== SESSION =====
if "pengelola_login" not in st.session_state:
    st.session_state.pengelola_login = False


# ===== STYLE =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f172a, #020617);
    color: white;
}
#MainMenu, footer, header {
    visibility: hidden;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}
.stTextInput input {
    background-color: #020617;
    color: white;
}
.stButton button {
    border-radius: 10px;
    background-color: #3b82f6;
    color: white;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)


# ===== LOGIN =====
def login_page():
    st.title("🔐 Login Pengelola")

    password = st.text_input("Masukkan Password", type="password")

    if st.button("Login"):
        if password == PENGELOLA_PASSWORD:
            st.session_state.pengelola_login = True
            st.rerun()
        else:
            st.error("Password salah ❌")


# ===== DASHBOARD =====
def dashboard():
    st.title("👤 Dashboard Pengelola")

    df = load_admin()

    # =====================
    # 📋 DAFTAR ADMIN
    # =====================
    st.subheader("📋 Daftar Admin")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # =====================
    # ➕ TAMBAH ADMIN
    # =====================
    st.subheader("➕ Tambah Admin")

    col1, col2 = st.columns(2)
    new_user = col1.text_input("Username Baru")
    new_pass = col2.text_input("Password Baru", type="password")

    if st.button("Tambah Admin"):
        if new_user and new_pass:
            new = pd.DataFrame([{
                "username": new_user,
                "password": new_pass
            }])
            df = pd.concat([df, new], ignore_index=True)
            df.to_excel(ADMIN_FILE, index=False)
            st.success("Admin berhasil ditambahkan ✅")
            st.rerun()
        else:
            st.warning("Isi semua field!")

    st.divider()

    # =====================
    # ✏ EDIT ADMIN
    # =====================
    st.subheader("✏ Edit Admin")

    if len(df) > 0:
        idx = st.selectbox("Pilih Admin", df.index)

        edit_user = st.text_input("Username", value=df.loc[idx, "username"])
        edit_pass = st.text_input("Password", value=df.loc[idx, "password"], type="password")

        if st.button("Update Admin"):
            df.loc[idx] = [edit_user, edit_pass]
            df.to_excel(ADMIN_FILE, index=False)
            st.success("Admin berhasil diupdate ✅")
            st.rerun()

    st.divider()

    # =====================
    # ❌ HAPUS ADMIN
    # =====================
    st.subheader("❌ Hapus Admin")

    if len(df) > 0:
        del_idx = st.selectbox("Pilih Admin yang dihapus", df.index, key="hapus")

        if st.button("Hapus Admin"):
            df = df.drop(del_idx).reset_index(drop=True)
            df.to_excel(ADMIN_FILE, index=False)
            st.success("Admin berhasil dihapus ✅")
            st.rerun()

    st.divider()

    # =====================
    # 🚪 LOGOUT
    # =====================
    if st.button("Logout"):
        st.session_state.pengelola_login = False
        st.rerun()


# ===== MAIN =====
def show_pengelola():
    if st.session_state.pengelola_login:
        dashboard()
    else:
        login_page()