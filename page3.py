# pages/3_👥_Team_Members.py
import streamlit as st

st.title("👥 Team Members — Group 10")

cols = st.columns(3)
names = ["Jeanny Sherenita", "Lasmaida Harianja", "Mutia Anggraini"]
photos = ["assets/jeanny.jpg", "assets/lasmaida.jpg", "assets/mutia.jpg"]  # letakkan foto di folder assets/

for i, col in enumerate(cols):
    with col:
        st.image(photos[i], width=200)
        st.subheader(names[i])

st.write("---")
st.write("Klik tombol di bawah untuk melihat peran dan deskripsi singkat.")
if st.button("Next → Detail Peran & Cara Kerja"):
    st.session_state['goto_roles'] = True
    st.experimental_rerun()
