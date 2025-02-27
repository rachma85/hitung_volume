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
