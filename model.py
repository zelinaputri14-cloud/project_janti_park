import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def train_model(df):

    df_model = df.copy()
    df_model["bulan_dalam_tahun"] = ((df_model["bulan_ke"]-1)%12)+1

    df_model = pd.get_dummies(df_model,
        columns=["bulan_dalam_tahun"],
        drop_first=True
    )

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
    mape = np.mean(np.abs((y_test-y_pred)/np.where(y_test==0,1,y_test))) * 100

    return model, r2, mae, rmse, mape, df_model