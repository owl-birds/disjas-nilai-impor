import numpy as np
import pandas
from pandas.core.indexes.base import Index 
import streamlit as st 

data = pandas.read_csv("dataImporAceh.csv")

st.write(" # Data Nilai Impor Provinsi Aceh ")
st.dataframe(data, width=500, height=500)
st.write("source : https://aceh.bps.go.id/site/resultTab")

st.markdown("""
## Konsep
### A. Cakupan komoditas
    Semua jenis barang termasuk kecuali yang termasuk dibawah ini:
        1.Pakaian dan perhiasan dari para penumpang.
        2.Barang bawaan penumpang yang digunakan 
        untuk keperluan sendiri, kecuali lemari es, 
        televisi, dsb.
        3.Barang-barang yang diekspor / diimpor dari 
        suatu negara untuk digunakan untuk keperluan 
        kedutaan besar negara tersebut.
        4.Barang-barang yang digunakan untuk keperluan
        ekspedisi dan pameran.
        5.Barang-barang yang di ekspor / diimpor 
        secara langsung oleh angkatan bersenjata.
        6.Peti Kemas yang dimaksudkan untuk diisi.
        7.Catatan-catatan dari Bank dan keamanan.
        8.Barang-barang contoh.
### B. Sistem Perdagangan
        Statistik Impor berdasarkan pada Sistem 
        Perdagangan Khusus yang meliputi seluruh 
        area geografi Indonesia kecuali Zona 
        Perdagangan Bebas dimana berlaku Perdagangan
        Luar Negeri.
### C. Penilaian
        Impor mengacu pada nilai Cost Insurance and Freight (CIF).
        Dinyatakan dalam Dollar Amerika (USD)
### D. Pengukuran Kuantitas 
        semua kuantitas dinyatakan dalam bentuk berat netto dalam 
        satuan kilogram.
### E. Rekan Negara
        - Negara tujuan adalah negara yang pada saat 
        pengiriman diketahui sebagai negara terakhir 
        dimana barang tersebut akan terkirim.
        - Negara asal adalah negara dimana barang-
        barang tersebut diproduksi, setelah 
        diverifikasi oleh Kantor Bea Cukai, sesuai 
        dengan peraturan.
## Metodologi
### A. Sumber Data
        Keseluruhan data dikumpulkan berdasarkan 
        dokumen-dokumen keterangan ekspor impor yang 
        dihasilkan oleh Kantor Pelayanan Bea dan Cukai.
### B. Metode Pengumpulan
        Data diperoleh berdasarkan penghitungan 
        lengkap, dan diterima dari Kantor Pelayanan
        Bea dan Cukai yang berlokasi di negara 
        tersebut.
source : https://aceh.bps.go.id/subject/8/ekspor-impor.html#subjekViewTab1
""")

st.write(" # Visualisasi Data Nilai Impor Provinsi Aceh ")
select_year = st.multiselect("Pilih Tahun", ["2014-2021",2014,2015,2016,2017,2018,2019,2020,2021])
# st.write(select_year)

data_dict = {
        2014: [data.iloc[:12, :], data.iloc[:12, 1:2]],
        2015: [data.iloc[12:24, :], data.iloc[12:24, 1:2]],
        2016: [data.iloc[24:36, :], data.iloc[24:36, 1:2]],
        2017: [data.iloc[36:48, :], data.iloc[36:48, 1:2]],
        2018: [data.iloc[48:60, :], data.iloc[48:60, 1:2]],
        2019: [data.iloc[60:72, :], data.iloc[60:72, 1:2]],
        2020: [data.iloc[72:84, :], data.iloc[72:84, 1:2]],
        2021: [data.iloc[84:96, :], data.iloc[84:96, 1:2]]
}

# METHOD/FUNCTION
# visual_data = pandas.DataFrame({
#                         "Bulan": [],
#                         "Nilai Impor (JT USD)": [],
#                         "year": []
#                 })
def visualize(year_list): 
        if len(year_list) == 0:
                st.write("PILIH TAHUN YANG AKAN DITAMPILKAN")
        elif select_year[0] == "2014-2021":
                st.write(f"Nilai Impor tahun {select_year[0]}")
                st.line_chart(data.iloc[:, 1:2])
                st.write(data)
        else:
                for year in year_list:
                        # visual_data.append(data_dict[year])  
                        st.write(f"Nilai Impor tahun {year}")
                        chart, table = st.columns([3,1])
                        # st.write(data_dict[year])
                        table.write(data_dict[year][0].iloc[:, :1])
                        chart.line_chart(data_dict[year][1])
                # st.write(visual_data)

visualize(select_year)

# st.write(visual_data.append(data.iloc[84:96, :]))




# test
# st.write(pandas.concat([data_dict[2014],data_dict[2015]]))

# st.write(data.iloc[:12, :])
# st.write(data.iloc[12:24, :])
# st.write(data.iloc[24:36, :])
# st.write(data.iloc[36:48, :])
# st.write(data.iloc[48:60, :])
# st.write(data.iloc[60:72, :])
# st.write(data.iloc[72:84, :])
# st.write(data.iloc[84:96, :])