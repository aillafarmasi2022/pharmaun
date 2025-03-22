import os
import streamlit as st
import pandas as pd

# Pastikan path benar dengan os.path.join
csv_path = os.path.join(os.path.dirname(__file__), "data/kamus.csv")

# Cek apakah file ada
if not os.path.exists(csv_path):
    st.error("File `kamus.csv` tidak ditemukan! Pastikan sudah diunggah ke GitHub.")
else:
    df = pd.read_csv(csv_path)
import os
st.write(os.listdir("."))  # Melihat file di direktori utama
st.write(os.listdir("data"))  # Jika folder data ada

