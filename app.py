import streamlit as st
from styles import DASHBOARD_STYLES, HIDE_ST_STYLE, display_sidebar_header

# Page config
st.set_page_config(
    page_title="BeanClassify - Klasifikasi Kualitas Biji Kopi",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Remove default menu & apply CSS
st.markdown(DASHBOARD_STYLES, unsafe_allow_html=True)

# Set current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

# Sidebar
display_sidebar_header()

import base64

def get_base64_of_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Logo tidak ditemukan: {image_path}")
        return None

logo_base64 = get_base64_of_image("assets/logo3.png")

if st.session_state.current_page == 'dashboard':
    # Header utama
    st.markdown(
        f'''
        <div style="text-align: center">
            <div class="main-header" style= "color: #4B2E05; font-family: Playfair Display; font-size: 2.5rem; 
            margin-bottom: 0px;">👋Selamat Datang👋</div>
            <div class="main-header-line1" style= "color: #3B2A1A; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
              font-size: 4rem; font-family: 'sans-serif'; margin-top: 0px;">
            <img src="data:image/png;base64,{logo_base64}" width="80" style="vertical-align: middle;">
                Di BeanClassify
            <img src="data:image/png;base64,{logo_base64}" width="80" style="vertical-align: middle;">
            </div>
        </div>
        ''', 
        unsafe_allow_html=True
    )
    # Welcome card
    st.markdown("""
    <div class="welcome-card">
        <h2 style="text-align: center">!Klasifikasi Kualitas Biji Kopi! </h2>
        <p>Sistem ini digunakan untuk mengklasifikasikan kualitas biji kopi menjadi 3 kategori:</p>
        <ul>
            <li><strong>✅ Bagus</strong> - Biji kopi berkualitas baik</li>
            <li><strong>⚠️ Rusak</strong> - Biji kopi rusak/patah</li>
            <li><strong>🍄 Jamur</strong> - Biji kopi berjamur</li>
        </ul>     
        <p>Silakan gunakan tombol di bawah untuk memulai klasifikasi atau mempelajari lebih lanjut tentang sistem ini.</p>
    </div>
    """, unsafe_allow_html=True)
    # TOMBOL DI TENGAH - menggunakan 3 kolom dengan kolom tengah lebih besar
    col1, col2, col3= st.columns([1, 2, 1])
    
    with col2:
        # Sub-columns di dalam kolom tengah untuk dua tombol sampingan
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            if st.button("🔍 Mulai Klasifikasi", type="primary", use_container_width=True):
                st.session_state.current_page = 'klasifikasi'
                st.switch_page("pages/klasifikasi.py")
        with subcol2:
            if st.button("ℹ️ Tentang Sistem", type="primary", use_container_width=True):
                st.session_state.current_page = 'tentang'
                st.switch_page("pages/tentang.py")
    st.markdown("<br>", unsafe_allow_html=True)

    # # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #8B7355; padding: 30px; background: linear-gradient(135deg, #f5f0e8 0%, #e8dcc8 100%); border-radius: 20px; margin-top: 40px;'>
        <p style='font-size: 16px; font-weight: 600; margin-bottom: 10px;'>© 2024 BeanClassify - Sistem Klasifikasi Kualitas Biji Kopi</p>
        <p style='font-size: 14px;'>Dibuat dengan ❤️ menggunakan Python dan Machine Learning</p>
    </div>
""", unsafe_allow_html=True)
    st.markdown("---")