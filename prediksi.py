import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

DATA_FILE = "database_pengunjung.xlsx"

# ===============================
# 🎨 STYLE (TIDAK DIUBAH)
# ===============================
st.markdown("""
<style>
.bgblue {
  background: linear-gradient(135deg, #ffffffcc, #3a4b8a55, #ffffff88);
  padding: 2px;
  border-radius: 18px;
  margin-bottom: 15px;
}
.card {
  font-size: 14px;
  color: #eaeaea;
  background: linear-gradient(135deg, #0d1120 0%, #3a4b8a 50%, #0d1120 100%);
  padding: 18px;
  border-radius: 16px;
  line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

def glass(text):
    return f"""
    <div class="bgblue">
        <div class="card">{text}</div>
    </div>
    """

# ===============================
# LOAD DATA
# ===============================
def load_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_excel(DATA_FILE)
        return df.sort_values("bulan_ke").reset_index(drop=True)
    return pd.DataFrame(columns=[
        "bulan_ke",
        "jumlah_pengunjung",
        "akhir_pekan",
        "libur_nasional"
    ])

# ===============================
# MODEL (TETAP PUNYA KAMU)
# ===============================
def train_model(df):

    df_model = df.copy()
    df_model["bulan_dalam_tahun"] = ((df_model["bulan_ke"] - 1) % 12) + 1
    df_model = pd.get_dummies(df_model, columns=["bulan_dalam_tahun"], drop_first=True)

    X = df_model.drop(columns=["jumlah_pengunjung"])
    y = df_model["jumlah_pengunjung"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mape = np.mean(np.abs((y_test - y_pred) / np.where(y_test==0,1,y_test))) * 100

    return model, r2, mae, rmse, mape, df_model

# ===============================
# KATEGORI
# ===============================
def kategori_r2(r2):
    if r2 >= 0.9:
        return "Sangat Baik"
    elif r2 >= 0.7:
        return "Baik"
    elif r2 >= 0.5:
        return "Cukup"
    return "Buruk"

def kategori_mape(mape):
    if mape < 10:
        return "Sangat Baik"
    elif mape < 20:
        return "Baik"
    elif mape < 50:
        return "Cukup"
    return "Buruk"

# ===============================
# 🔥 RESET FUNCTION (ANTI ERROR)
# ===============================
def reset_input():
    st.session_state["bulan"] = 1
    st.session_state["akhir"] = 0
    st.session_state["libur"] = 0

# ===============================
# MAIN UI
# ===============================
def show_prediksi():

    st.title("📊 Prediksi Pengunjung Janti Park")

    df = load_data()

    if len(df) < 12:
        st.warning("Minimal 12 bulan data untuk training.")
        return

    model, r2, mae, rmse, mape, df_model = train_model(df)

    # ===============================
    # METRIK
    # ===============================
    st.subheader("📊 Evaluasi Model")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("R²", f"{r2:.3f}")
    col2.metric("MAE", f"{mae:.0f}")
    col3.metric("RMSE", f"{rmse:.0f}")
    col4.metric("MAPE", f"{mape:.2f}%")

    # ===============================
    # TABEL
    # ===============================
    penjelasan_df = pd.DataFrame({
        "Metrik": ["R²", "MAE", "RMSE", "MAPE"],
        "Arti": [
            "Kemampuan model menjelaskan data",
            "Rata-rata selisih prediksi",
            "Error sensitif nilai besar",
            "Persentase kesalahan"
        ],
        "Nilai": [
            f"{r2:.3f}",
            f"{mae:.0f}",
            f"{rmse:.0f}",
            f"{mape:.2f}%"
        ],
        "Kategori": [
            kategori_r2(r2),
            "Relatif",
            "Relatif",
            kategori_mape(mape)
        ]
    })

    st.dataframe(penjelasan_df, use_container_width=True, hide_index=True)

    # ===============================
    # GRAFIK
    # ===============================
    st.subheader("📈 Grafik Aktual vs Prediksi")

    X_full = df_model.drop(columns=["jumlah_pengunjung"])
    y_full = df_model["jumlah_pengunjung"]
    y_pred_full = model.predict(X_full)

    fig, ax = plt.subplots()
    ax.plot(y_full.values, label="Aktual")
    ax.plot(y_pred_full, label="Prediksi")
    ax.legend()
    st.pyplot(fig)

    # ===============================
    # INIT SESSION STATE (WAJIB)
    # ===============================
    if "bulan" not in st.session_state:
        st.session_state["bulan"] = 1
    if "akhir" not in st.session_state:
        st.session_state["akhir"] = 0
    if "libur" not in st.session_state:
        st.session_state["libur"] = 0

    # ===============================
    # INPUT
    # ===============================
    st.subheader("🎯 Prediksi Baru")

    st.info("""
- Bulan ke → 1–12
- Akhir Pekan → minimal 8 hari
- Libur Nasional → jumlah hari libur
""")

    col1, col2, col3 = st.columns(3)

    bulan = col1.number_input("Bulan ke-", min_value=1, max_value=12, key="bulan")
    akhir = col2.number_input("Akhir Pekan", min_value=0, max_value=10, key="akhir")
    libur = col3.number_input("Libur Nasional", min_value=0, max_value=15, key="libur")

    if akhir < 8:
        st.warning("Akhir pekan minimal 8 ❗")

    # ===============================
    # BUTTON
    # ===============================
    colb1, colb2 = st.columns(2)

    prediksi_btn = colb1.button(
        "Prediksi",
        disabled=(akhir < 8),
        key="btn_prediksi"
    )

    colb2.button(
        "Reset",
        key="btn_reset",
        on_click=reset_input   # 🔥 FIX TANPA ERROR
    )

    # ===============================
    # PREDIKSI
    # ===============================
    if prediksi_btn:

        bulan_dalam_tahun = ((bulan - 1) % 12) + 1

        input_dict = {
            "bulan_ke": bulan,
            "akhir_pekan": akhir,
            "libur_nasional": libur
        }

        for i in range(2, 13):
            input_dict[f"bulan_dalam_tahun_{i}"] = 1 if bulan_dalam_tahun == i else 0

        input_df = pd.DataFrame([input_dict])

        for col in X_full.columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[X_full.columns]

        hasil = model.predict(input_df)[0]

        st.markdown(glass(f"""
        🎯 <b>Hasil Prediksi</b><br><br>
        <h2>{int(hasil):,} orang</h2>
        """), unsafe_allow_html=True)