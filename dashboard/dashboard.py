import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ======================
# LOAD DATA
# ======================
path = os.path.join(os.path.dirname(__file__), "main_data.csv")
df = pd.read_csv(path)

st.title("🚲 Bike Sharing Dashboard")

# ======================
# FILTER 1: TAHUN
# ======================
year_option = st.selectbox("Pilih Tahun", ["2011", "2012"])

if year_option == "2011":
    df_filtered = df[df['yr'] == 0].copy()
else:
    df_filtered = df[df['yr'] == 1].copy()

# ======================
# TAMBAH KOLOM DAY TYPE
# ======================
df_filtered["day_type"] = df_filtered["workingday"].apply(
    lambda x: "Weekday" if x == 1 else "Weekend"
)

# ======================
# FILTER 2: TIPE HARI
# ======================
day_option = st.selectbox("Pilih Tipe Hari", ["Semua", "Weekday", "Weekend"])

if day_option != "Semua":
    df_filtered = df_filtered[df_filtered["day_type"] == day_option]

# ======================
# FILTER 3: JAM
# ======================
hour_range = st.slider("Pilih Rentang Jam", 0, 23, (0, 23))

df_filtered = df_filtered[
    (df_filtered["hr"] >= hour_range[0]) &
    (df_filtered["hr"] <= hour_range[1])
]

# ======================
# INFO DATA
# ======================
st.write("Jumlah data setelah filter:", df_filtered.shape[0])

# ======================
# VISUALISASI 1: CUACA
# ======================
st.subheader("🌤️ Pengaruh Cuaca terhadap Penyewaan")

fig1, ax1 = plt.subplots()

sns.barplot(
    x="weathersit",
    y="cnt",
    data=df_filtered,
    order=["Clear", "Mist", "Light Snow/Rain", "Heavy Rain"],
    ax=ax1
)

ax1.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig1)

# ======================
# VISUALISASI 2: JAM
# ======================
st.subheader("⏰ Pola Penyewaan per Jam")

fig2, ax2 = plt.subplots()

sns.lineplot(
    x="hr",
    y="cnt",
    hue="day_type",
    data=df_filtered,
    marker="o",
    ax=ax2
)

ax2.set_title("Pola Penyewaan Sepeda per Jam")
ax2.set_xlabel("Jam")
ax2.set_ylabel("Jumlah Penyewaan")
ax2.set_xticks(range(0, 24))

st.pyplot(fig2)