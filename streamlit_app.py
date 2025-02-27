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
if option=="Bola":
    jari = st.number_input("Masukkan jari-jari bola (cm):")
    st.write("Jari-jari bola sebesar", jari)
    vol=3,14*jari*jari*jari
    st.write("Volume bola dengan jari-jari sebesar",jari,"cm adalah",vol,"cm3")
elif option=="Tabung":
    tinggi=st.number_input("Masukkan tinggi tabung (cm):")
    jari = st.number_input("Masukkan jari-jari tabung (cm):")
    vol=3,14*jari*jari*tinggi
    st.write("Volume tabung dengan tinggi",tinggi,"dan jari-jari sebesar",jari,"cm adalah",vol,"cm3")
elif option=="Kerucut":
    tinggi=st.number_input("Masukkan tinggi kerucut (cm):")
    jari = st.number_input("Masukkan jari-jari kerucut (cm):")
    vol=(3,14*jari*jari*tinggi)/3
    st.write("Volume kerucut dengan tinggi",tinggi,"dan jari-jari sebesar",jari,"cm adalah",vol,"cm3")    
elif option=="Balok":
    p=st.number_input("Masukkan panjang tabung (cm):")
    jari = st.number_input("Masukkan jari-jari tabung (cm):")
    vol=3,14*jari*jari*tinggi
    st.write("Volume tabung dengan tinggi",tinggi,"dan jari-jari sebesar",jari,"cm adalah",vol,"cm3")   
