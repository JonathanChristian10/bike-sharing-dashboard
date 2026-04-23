import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("🚲 Bike Sharing Dashboard")

# Load data
df = pd.read_csv("main_data.csv")

# Data preprocessing
df['season'] = df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

df['weathersit'] = df['weathersit'].map({
    1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain'
})

df["day_type"] = df["workingday"].apply(lambda x: "Weekday" if x == 1 else "Weekend")

# ======================
# SECTION 1: Hourly Trend
# ======================
st.subheader("Pola Penyewaan Berdasarkan Jam")

fig1, ax1 = plt.subplots()
sns.lineplot(x="hr", y="cnt", data=df, ax=ax1)
ax1.set_xticks(range(0,24))
st.pyplot(fig1)

st.write("Terjadi lonjakan penyewaan pada jam sibuk (pagi dan sore).")

# ======================
# SECTION 2: Weather Impact
# ======================
st.subheader("Pengaruh Cuaca")

fig2, ax2 = plt.subplots()
sns.barplot(x="weathersit", y="cnt", data=df, ax=ax2)
st.pyplot(fig2)

st.write("Cuaca cerah memiliki jumlah penyewaan tertinggi.")

# ======================
# SECTION 3: Weekday vs Weekend
# ======================
st.subheader("Weekday vs Weekend")

fig3, ax3 = plt.subplots()
sns.barplot(x="day_type", y="cnt", data=df, ax=ax3)
st.pyplot(fig3)

st.write("Penyewaan lebih tinggi pada hari kerja dibandingkan weekend.")