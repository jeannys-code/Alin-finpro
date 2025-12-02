import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🖼️ Matrix-Based Image Processing Web App")
st.subheader("Transformasi Matriks & Konvolusi pada Pengolahan Gambar")

st.write("""
Aplikasi ini dibuat untuk mendemonstrasikan penggunaan **transformasi matriks** dan 
**operasi konvolusi** dalam pengolahan gambar. Pengguna dapat menerapkan 
**translation, scaling, rotation, shearing, reflection**, serta filter berbasis konvolusi 
seperti **blur** dan **sharpen**.  
""")

# ————————————————
# Penjelasan Transformasi Matriks
# ————————————————
st.header("🔢 Apa itu Transformasi Matriks?")
st.write("""
Transformasi matriks adalah proses mengubah posisi pixel gambar menggunakan operasi matriks.
Contohnya:
- **Translation** → menggeser gambar  
- **Scaling** → memperbesar/perkecil gambar  
- **Rotation** → memutar gambar  
- **Shearing** → memiringkan gambar  
- **Reflection** → membuat cerminan gambar
""")

st.code("""
Rotation (θ):
[ cosθ  -sinθ   0 ]
[ sinθ   cosθ   0 ]
[  0      0     1 ]
""")

# ————————————————
# Penjelasan Konvolusi
# ————————————————
st.header("🧮 Apa itu Konvolusi?")
st.write("""
Konvolusi adalah teknik pengolahan gambar dengan menggeser **kernel** di atas gambar 
untuk menghasilkan pixel baru.  
Filter umum:
- **Blur** → menghaluskan gambar  
- **Sharpen** → menajamkan tepi (edge enhancement)
""")

col1, col2 = st.columns(2)

with col1:
    st.write("**Kernel Blur (3×3)**")
    st.code("""
1/9 * [
 [1 1 1]
 [1 1 1]
 [1 1 1]
]
""")

with col2:
    st.write("**Kernel Sharpen (3×3)**")
    st.code("""
[
 [ 0 -1  0]
 [-1  5 -1]
 [ 0 -1  0]
]
""")

# ————————————————
# Contoh visual
# ————————————————
st.subheader("📌 Contoh Visual Konvolusi (Dummy Image)")

demo = np.zeros((200, 200))
demo[50:150, 50:150] = 255

fig, ax = plt.subplots()
ax.imshow(demo, cmap="gray")
ax.axis("off")

st.pyplot(fig)

st.info("Silakan buka halaman **Image Processing Tools** untuk mencoba fitur transformasi & filter.")
