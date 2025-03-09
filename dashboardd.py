import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
# Load dataset
day_df = pd.read_csv('archive_day_cleaned.csv')
hour_df = pd.read_csv('archive_hour_cleaned.csv')

# Judul Dashboard 
st.markdown(
    "<h1 style='text-align: center;'>Bike Sharing Dashboard 🚴‍♂</h1>", 
    unsafe_allow_html=True
)

# Mapping angka bulan ke nama bulan
bulan = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

# Mapping bulan
day_df["mnth"] = day_df["mnth"].map(bulan)

# Mengatur urutan bulan
order_bulan = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
day_df["mnth"] = pd.Categorical(day_df["mnth"], categories=order_bulan, ordered=True)

# Agregasi data berdasarkan workingday dan bulan
bulan_casual = day_df.groupby(["workingday", "mnth"]).agg({
    "casual": "mean",
    "registered": "mean"
}).reset_index()

# Sidebar
st.sidebar.image("sepeda.jpeg", width=200)
category = st.sidebar.selectbox("Pilih Kategori Pengguna", ["Semua", "Registered", "Casual"])

# Menampilkan visualisasi berdasarkan kategori
if category == "Registered":
    st.subheader("Rata-rata Penyewa Sepeda Registered Berdasarkan Workingday per Bulan")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=bulan_casual, x="mnth", y="registered", hue="workingday", palette=["#FF9999", "#66B3FF"], ax=ax)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-rata Jumlah Penyewa")
    ax.legend(["Hari Non-Kerja", "Hari Kerja"], title="Workingday")
    st.pyplot(fig)

elif category == "Casual":
    st.subheader("Rata-rata Penyewa Sepeda Casual Berdasarkan Workingday per Bulan")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=bulan_casual, x="mnth", y="casual", hue="workingday", palette=["#FF9999", "#66B3FF"], ax=ax)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-rata Jumlah Penyewa")
    ax.legend(["Hari Non-Kerja", "Hari Kerja"], title="Workingday")
    st.pyplot(fig)

else:
    st.subheader("Rata-rata Penyewa Sepeda Registered Berdasarkan Workingday per Bulan")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=bulan_casual, x="mnth", y="registered", hue="workingday", palette=["#FF9999", "#66B3FF"], ax=ax)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-rata Jumlah Penyewa")
    ax.legend(["Hari Non-Kerja", "Hari Kerja"], title="Workingday")
    st.pyplot(fig)
    
    st.subheader("Rata-rata Penyewa Sepeda Casual Berdasarkan Workingday per Bulan")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=bulan_casual, x="mnth", y="casual", hue="workingday", palette=["#FF9999", "#66B3FF"], ax=ax)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-rata Jumlah Penyewa")
    ax.legend(["Hari Non-Kerja", "Hari Kerja"], title="Workingday")
    st.pyplot(fig)
    
    st.subheader("Perbandingan Penyewa Sepeda Casual & Registered Berdasarkan Workingday dalam Sehari")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=hour_df[hour_df["workingday"] == 1], x="hr", y="casual", label="Casual - Hari Kerja", marker="o", ax=ax)
    sns.lineplot(data=hour_df[hour_df["workingday"] == 1], x="hr", y="registered", label="Registered - Hari Kerja", marker="o", ax=ax)
    sns.lineplot(data=hour_df[hour_df["workingday"] == 0], x="hr", y="casual", label="Casual - Akhir Pekan", marker="o", ax=ax)
    sns.lineplot(data=hour_df[hour_df["workingday"] == 0], x="hr", y="registered", label="Registered - Akhir Pekan", marker="o", ax=ax)
    ax.set_xlabel("Jam dalam Sehari (hr)")
    ax.set_ylabel("Jumlah Penyewa")
    ax.legend()
    ax.grid()
    st.pyplot(fig)
    
    st.subheader("Heatmap Penyewaan Sepeda Berdasarkan Jam dan Workingday")
    heatmap_data = hour_df.pivot_table(values="cnt", index="hr", columns="workingday", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".1f", linewidths=0.5, ax=ax)
    ax.set_xlabel("Workingday (0 = Akhir Pekan, 1 = Hari Kerja)")
    ax.set_ylabel("Jam dalam Sehari (hr)")
    st.pyplot(fig)

st.sidebar.write("\n\n**Dashboard Analisis Penyewaan Sepeda**")

# Footer
st.caption("📊 Dashboard Bike Sharing | Dibuat oleh Salsabila Mahiroh")