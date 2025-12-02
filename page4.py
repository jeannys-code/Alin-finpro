import streamlit as st

st.title("📄 Roles & App Description")

st.subheader("Jeanny Sherenita")
st.write("- Developer UI Streamlit & dokumentasi")

st.subheader("Lasmaida Harianja")
st.write("- Implementasi transformasi matriks")

st.subheader("Mutia Anggraini")
st.write("- Implementasi konvolusi & background removal")

st.divider()

st.header("📘 Cara Kerja Aplikasi")
st.write("""
Setiap gambar diproses menggunakan **matriks 3x3** untuk transformasi geometris 
dan **kernel konvolusi** untuk filtering. Operasi dilakukan secara manual tanpa 
fungsi bawaan OpenCV, agar konsep matematis dapat dipahami secara langsung.
""")
