import streamlit as st

st.title("Aplikasi Menghitung Volume")
st.write(
    "Aplikasi ini digunakan untuk menghitung volume benda antara lain: bola, tabung, kerucut, prisma, balok, kubus."
)
option = st.selectbox(
    "Volume apa yang akan dihitung?",
    ("Bola", "Tabung", "Kerucut","Prisma","Balok","Kubus"),
)

st.write("You selected:", option)
if option==Bola:
    jari = st.number_input("Masukkan jari-jari bola (cm):")
    st.write("Jari-jari bola sebesar", jari)
    vol=3,14*jari*jari*jari
    st.write("Volume bola dengan jari-jari sebesar",jari,"cm adalah",vol,"cm3")
