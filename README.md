# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset Bike Sharing untuk memahami pola penyewaan sepeda berdasarkan kondisi cuaca dan waktu (jam) pada tahun 2012.  

Hasil analisis divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## Pertanyaan Bisnis

1. Bagaimana pengaruh kondisi cuaca terhadap rata-rata jumlah penyewaan sepeda per jam pada tahun 2012, dan kondisi cuaca mana yang menghasilkan penyewaan tertinggi?

2. Pada jam berapa terjadi puncak penyewaan sepeda pada tahun 2012, dan bagaimana perbedaannya antara hari kerja dan akhir pekan?

---

## Insight Hasil Analisis

### Pengaruh Cuaca
- Cuaca cerah (Clear) menghasilkan jumlah penyewaan tertinggi
- Semakin buruk kondisi cuaca, semakin rendah jumlah penyewaan
- Hujan deras (Heavy Rain) memiliki penyewaan terendah

### Pola Waktu
- Puncak penyewaan terjadi pada:
  - Pagi hari (sekitar jam 08.00)
  - Sore hari (sekitar jam 17.00)
- Pada hari kerja, pola sangat jelas (jam berangkat & pulang kerja)
- Pada akhir pekan, penyewaan lebih merata sepanjang hari

---

## Rekomendasi

1. Menyediakan lebih banyak sepeda saat cuaca cerah
2. Meningkatkan ketersediaan sepeda pada jam sibuk (07.00–09.00 dan 17.00–19.00)
3. Mengoptimalkan strategi promosi pada akhir pekan

---

## Struktur Direktori

submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt