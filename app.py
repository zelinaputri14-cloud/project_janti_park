import streamlit as st
from dashboard import show_dashboard
from prediksi import show_prediksi
from admin import show_admin
from pengelola import show_pengelola

import streamlit as st

# ======================
# SESSION INIT GLOBAL 🔥
# ======================
if "login" not in st.session_state:
    st.session_state.login = False

if "admin_user" not in st.session_state:
    st.session_state.admin_user = None

if "pengelola_login" not in st.session_state:
    st.session_state.pengelola_login = False

if "pengelola_user" not in st.session_state:
    st.session_state.pengelola_user = None

if "menu" not in st.session_state:
    st.session_state.menu = "Beranda"

st.set_page_config(page_title="Janti Park", layout="wide")

# ======================
# 🎨 GLOBAL CSS (PINDAHAN DARI style.py)
# ======================
st.markdown("""
<style>

/* RESET STREAMLIT */
header[data-testid="stHeader"],
[data-testid="stSidebar"],
footer {
    display: none;
}

html, body, [data-testid="stAppViewContainer"] {
    margin: 0;
    padding: 0;
}

/* CONTAINER OFFSET NAVBAR */
.block-container {
    padding-top: 70px !important;
}

/* ======================
   NAVBAR
====================== */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 0 60px;
    z-index: 9999;

    backdrop-filter: blur(10px);
}

/* LIGHT MODE */
@media (prefers-color-scheme: light) {
    .navbar {
        background: rgba(255,255,255,0.9);
        border-bottom: 1px solid rgba(0,0,0,0.1);
    }

    .logo { color: #111; }

    .menu a { color: #555; }

    .menu a:hover { color: #000; }

    .active {
        color: #000 !important;
        border-bottom: 2px solid #007bff;
    }
}

/* DARK MODE */
@media (prefers-color-scheme: dark) {
    .navbar {
        background: rgba(0,0,0,0.9);
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .logo { color: white; }

    .menu a { color: rgba(255,255,255,0.7); }

    .menu a:hover { color: white; }

    .active {
        color: white !important;
        border-bottom: 2px solid white;
    }
}

/* MENU */
.menu a {
    margin-left: 25px;
    text-decoration: none;
    font-size: 14px;
    transition: 0.3s;
}

/* RESPONSIVE */
@media (max-width: 768px) {

    .navbar {
        padding: 10px 20px;
        flex-direction: column;
        align-items: flex-start;
        height: auto;
    }

    .menu {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 5px;
    }

    .block-container {
        padding-top: 110px !important;
    }
}

/* SMOOTH */
html {
    scroll-behavior: smooth;
}

</style>
""", unsafe_allow_html=True)

# ======================
# SESSION STATE
# ======================
if "menu" not in st.session_state:
    st.session_state.menu = "Beranda"

# ======================
# QUERY PARAM NAVIGASI
# ======================
query = st.query_params

if "page" in query:
    if query["page"] != st.session_state.menu:
        st.session_state.menu = query["page"]

menu = st.session_state.menu

# ======================
# NAVBAR
# ======================
st.markdown(f"""
<div class="navbar">
    <div class="logo">🌿 Janti Park</div>
    <div class="menu">
        <a href="?page=Beranda" target="_self" class="{ 'active' if menu=='Beranda' else '' }">Beranda</a>
        <a href="?page=Prediksi" target="_self" class="{ 'active' if menu=='Prediksi' else '' }">Prediksi</a>
        <a href="?page=Admin" target="_self" class="{ 'active' if menu=='Admin' else '' }">Admin</a>
        <a href="?page=Pengelola" target="_self" class="{ 'active' if menu=='Pengelola' else '' }">Pengelola</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# SPACING
# ======================
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# ======================
# ROUTING
# ======================
if menu == "Beranda":
    show_dashboard()

elif menu == "Prediksi":
    show_prediksi()

elif menu == "Admin":
    show_admin()

elif menu == "Pengelola":
    show_pengelola()