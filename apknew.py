import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image as PILImage
from streamlit_option_menu import option_menu

# Konstanta
IMG_SIZE = 224
THRESHOLD = 0.6
CLASS_LABELS = [
    'banten_dogdoglojor', 'jakarta_tehyan',
    'jawabarat_angklung', 'jawabarat_calung', 'jawabarat_celempung', 'jawabarat_gong',
    'jawabarat_karinding', 'jawabarat_kecapi', 'jawabarat_rebab', 'jawabarat_suling',
    'jawabarat_tarawangsa', 'jawatengah_bonang', 'jawatengah_demung', 'jawatengah_siter',
    'jawatimur_kluncing', 'jawatimur_saronen', 'yogjakarta_kendang'
]

# Load model
@st.cache_resource
def load_model_cached():
    return load_model("alatmusiktradnew.h5")

model = load_model_cached()

# Sidebar Navigasi
with st.sidebar:
    selected = option_menu(
        menu_title="Navigasi",
        options=["Welcome", "Klasifikasi", "Daftar Alat Musik"],
        icons=["house", "music", "list-task"],
        default_index=0
    )

# --- Welcome Page ---
if selected == "Welcome":
    st.markdown("<h1>🎵 Aplikasi Klasifikasi Alat Musik Tradisional Jawa</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 18px; text-align: justify;'>
        Aplikasi ini menggunakan teknologi deep learning untuk mengenali gambar alat musik tradisional dari Pulau Jawa.
        <br><br>
        Upload atau ambil foto alat musik tradisional, dan sistem akan memberikan prediksi berdasarkan model klasifikasi.
        <br><br>
        Cocok digunakan untuk edukasi budaya dan pelestarian musik tradisional Indonesia.
    </div>
    """, unsafe_allow_html=True)

# --- Diagnosis Page ---
elif selected == "Klasifikasi":
    st.title("🔍 Klasifikasi Gambar Alat Musik Tradisional")

    uploaded_file = st.file_uploader("Upload gambar alat musik tradisional", type=['jpg', 'png', 'jpeg'])
    camera_image = st.camera_input("Atau ambil gambar langsung")

    input_image = uploaded_file if uploaded_file is not None else camera_image

    if input_image is not None:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(input_image, caption="Gambar yang diproses", use_column_width=True)

        with col2:
            img = PILImage.open(input_image).convert("RGB")
            img_resized = img.resize((IMG_SIZE, IMG_SIZE))
            img_array = image.img_to_array(img_resized)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            pred = model.predict(img_array)
            confidence = float(np.max(pred))
            class_idx = int(np.argmax(pred))
            predicted_class = CLASS_LABELS[class_idx]

            st.subheader("Hasil Prediksi:")
            st.success(f"🎶 Alat musik terdeteksi: **{predicted_class}**")
            st.write(f"📊 Keyakinan Model: **{confidence * 100:.2f}%**")

# --- Informasi Alat Musik ---
elif selected == "Daftar Alat Musik":
    st.title("📚 Daftar Alat Musik Tradisional yang Didukung")

    for label in CLASS_LABELS:
        with st.expander(f"📌 {label.replace('_', ' ').title()}"):
            st.write(f"**Nama:** {label.replace('_', ' ').title()}")
            st.image(f"images/{label}.jpg", use_column_width=True, caption=label.replace('_', ' ').title())
