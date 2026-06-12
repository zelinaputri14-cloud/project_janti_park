import pandas as pd
import os

DATA_FILE = "database_pengunjung.xlsx"
ADMIN_FILE = "admin_accounts.xlsx"

def load_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_excel(DATA_FILE)
        return df.sort_values("bulan_ke").reset_index(drop=True)
    return pd.DataFrame(columns=[
        "bulan_ke","jumlah_pengunjung",
        "akhir_pekan","libur_nasional"
    ])

def load_admin():
    if os.path.exists(ADMIN_FILE):
        return pd.read_excel(ADMIN_FILE)
    df = pd.DataFrame(columns=["username","password"])
    df.to_excel(ADMIN_FILE,index=False)
    return df