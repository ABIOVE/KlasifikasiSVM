import streamlit as st
import base64
from styles import COMMON_STYLES, HIDE_ST_STYLE, display_sidebar_header

# Page config
st.set_page_config(
    page_title="BeanClassify - Tentang",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Remove default menu
st.markdown(HIDE_ST_STYLE, unsafe_allow_html=True)

# Custom CSS
st.markdown(COMMON_STYLES, unsafe_allow_html=True)

# Function to get base64 of image
def get_base64_of_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Logo tidak ditemukan: {image_path}")
        return None

logo_base64 = get_base64_of_image("assets/logo3.png")

# Additional CSS for Tentang page - WARNA TOMBOL DIHAPUS AGAR MENGIKUTI styles.py
st.markdown("""
<style>
    .info-container {
        background: linear-gradient(135deg, #f5f0e8 0%, #e8dcc8 100%);
        border-radius: 12px;
        padding: 15px 20px;
        margin: 12px 0;
        box-shadow: 0 4px 12px rgba(139, 115, 85, 0.1);
        border: 2px solid #D2B48C;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .info-container:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(139, 115, 85, 0.2);
    }
    
    .section-title {
        color: #6F4E37;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        border-bottom: 2px solid #8B7355;
        padding-bottom: 6px;
    }
    
    .feature-box {
        background: white;
        border-radius: 10px;
        padding: 15px;
        margin: 8px 0;
        border-left: 3px solid #D2B48C;
        box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    }
    
    .feature-title {
        color: #8B7355;
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 8px;
    }
    
    .feature-box p {
        font-size: 15px;
        line-height: 1.7;
        color: #5a5a5a;
    }
    
    .feature-box ul, .feature-box ol {
        font-size: 15px;
        line-height: 1.7;
        color: #5a5a5a;
    }
    
    .metric-box {
        background: linear-gradient(135deg, #ffffff 0%, #f9f6f0 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border: 2px solid #D2B48C;
        transition: all 0.3s ease;
    }
    
    .metric-box:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 15px rgba(139, 115, 85, 0.15);
    }
    
    .metric-value {
        font-size: 28px;
        font-weight: 700;
        color: #6F4E37;
        margin: 8px 0;
    }
    
    .metric-label {
        color: #8B7355;
        font-size: 14px;
        font-weight: 500;
    }
    
    .sub-section-title {
        color: #6F4E37;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        margin: 20px 0 12px 0;
    }
    
    /* HAPUS CUSTOM BUTTON STYLING - BIAR MENGIKUTI styles.py */
    /* CSS button dari styles.py akan digunakan */
    
    /* Perbaikan khusus untuk tombol navigasi agar teks tidak turun */
    div[data-testid="column"] .stButton > button {
        font-size: 0.9rem !important;
        padding: 0.6rem 0.8rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    @media (max-width: 768px) {
        div[data-testid="column"] .stButton > button {
            font-size: 0.8rem !important;
            padding: 0.5rem 0.6rem !important;
        }
    }
    
    /* Header styling - DISESUAIKAN DENGAN KLASIFIKASI.PY */
    .main-header-container {
        text-align: center;
        margin-bottom: 1.5rem;
        padding: 0 1rem;
    }
    
    .main-header-line1 {
        font-size: 2.2rem;
        font-weight: 800;
        color: #3B2A1A;
        margin-bottom: 0.2rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        line-height: 1.2;
    }
    
    .main-header-line2 {
        font-size: 1.6rem;
        font-weight: 600;
        color: #8B5E3C;
        margin-top: 0;
        opacity: 0.9;
        line-height: 1.3;
    }
</style>
""", unsafe_allow_html=True)

# Set current page untuk navigasi
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'tentang'

# Tampilkan sidebar header dengan navigasi
display_sidebar_header()

# Handle navigasi
if st.session_state.current_page == 'dashboard':
    st.switch_page("app.py")
elif st.session_state.current_page == 'klasifikasi':
    st.switch_page("pages/klasifikasi.py")

# Header dengan styling - DISESUAIKAN DENGAN KLASIFIKASI.PY
st.markdown(
    f'''
    <div class="main-header-container">
        <div class="main-header-line1">
            <img src="data:image/png;base64,{logo_base64}" width="60" style="vertical-align: middle; margin-right: 10px;">
            BeanClassify
            <img src="data:image/png;base64,{logo_base64}" width="60" style="vertical-align: middle; margin-left: 10px;">
        </div>
        <div class="main-header-line2" style="color: #4B2E05; font-family: 'Playfair Display', serif;">
            Sistem Klasifikasi Kualitas Biji Kopi
        </div>
    </div>
    ''', 
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Section 1: Overview & Cara Penggunaan
st.markdown("""
<div class='info-container'>
    <div class='section-title'>
        📚 Tentang Sistem & Cara Penggunaan
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class='feature-box'>
        <div class='feature-title'>🎯 Tentang Sistem</div>
        <p style='color: #5a5a5a; line-height: 1.7;'>
        BeanClassify adalah aplikasi berbasis Machine Learning yang dirancang untuk 
        mengklasifikasikan biji kopi menjadi 3 kategori berdasarkan kualitas:
        </p>
        <ul style='color: #5a5a5a; line-height: 1.7; font-size: 15px;'>
            <li><strong>Bagus ✅</strong> - Biji kopi berkualitas baik, layak untuk diproses lebih lanjut</li>
            <li><strong>Rusak ⚠️</strong> - Biji kopi rusak, patah, atau cacat</li>
            <li><strong>Jamur 🍄</strong> - Biji kopi terindikasi jamur atau kontaminasi</li>
        </ul>
        <p style='color: #5a5a5a; line-height: 1.7;'>
        Sistem ini menggunakan algoritma <strong>Support Vector Machine (SVM)</strong> yang 
        dilatih dengan dataset 740 gambar biji kopi.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box'>
        <div class='feature-title'>📖 Cara Penggunaan</div>
        <ol style='color: #5a5a5a; line-height: 1.7; font-size: 15px;'>
            <li><strong>Upload Gambar</strong><br>Pilih gambar biji kopi yang ingin dianalisis</li>
            <li><strong>Klik Analisis</strong><br>Klik tombol "Analisis Gambar" untuk memulai</li>
            <li><strong>Lihat Hasil</strong><br>Sistem akan menampilkan:
                <ul style='margin-top: 5px;'>
                    <li>Prediksi kelas</li>
                    <li>Tingkat kepercayaan (confidence)</li>
                    <li>Distribusi probabilitas untuk setiap kelas</li>
                    <li>Gambar hasil preprocessing dan segmentasi</li>
                </ul>
            </li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section 2: Performance & Dataset (DIPINDAH KE ATAS)
st.markdown("""
<div class='info-container'>
    <div class='section-title'>
        📊 Performance Model & Dataset
    </div>
</div>
""", unsafe_allow_html=True)

# Performance Metrics
st.markdown("<div class='sub-section-title'>Performance Model</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='metric-box'>
        <div class='metric-label'>Accuracy</div>
        <div class='metric-value'>94.37%</div>
        <div style='color: #8B7355; font-size: 12px;'>Training Set</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-box'>
        <div class='metric-label'>Precision</div>
        <div class='metric-value'>94.41%</div>
        <div style='color: #8B7355; font-size: 12px;'>Training Set</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-box'>
        <div class='metric-label'>Recall</div>
        <div class='metric-value'>94.37%</div>
        <div style='color: #8B7355; font-size: 12px;'>Training Set</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='metric-box'>
        <div class='metric-label'>F1-Score</div>
        <div class='metric-value'>94.35%</div>
        <div style='color: #8B7355; font-size: 12px;'>Training Set</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Dataset Information
st.markdown("<div class='sub-section-title'>Informasi Dataset</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='metric-box' style='background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); border-color: #28a745;'>
        <div style='font-size: 32px; margin-bottom: 8px;'>✅</div>
        <div class='metric-label'>Bagus</div>
        <div class='metric-value' style='color: #155724;'>286</div>
        <div style='color: #155724; font-size: 12px;'>Biji kopi berkualitas baik</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-box' style='background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); border-color: #ffc107;'>
        <div style='font-size: 32px; margin-bottom: 8px;'>⚠️</div>
        <div class='metric-label'>Rusak</div>
        <div class='metric-value' style='color: #856404;'>240</div>
        <div style='color: #856404; font-size: 12px;'>Biji kopi rusak/patah</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-box' style='background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%); border-color: #dc3545;'>
        <div style='font-size: 32px; margin-bottom: 8px;'>🍄</div>
        <div class='metric-label'>Jamur</div>
        <div class='metric-value' style='color: #721c24;'>214</div>
        <div style='color: #721c24; font-size: 12px;'>Biji kopi berjamur</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; margin-top: 15px;'>
    <div class='feature-box' style='display: inline-block; max-width: 600px;'>
        <strong style='color: #6F4E37; font-size: 15px;'>Total Dataset:</strong> <span style='color: #8B7355; font-size: 15px;'>740 gambar</span><br>
        <strong style='color: #6F4E37; font-size: 15px;'>Pembagian:</strong> <span style='color: #8B7355; font-size: 15px;'>60% Train, 20% Validation, 20% Test</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section 3: Teknologi yang Digunakan (DIPINDAH KE BAWAH)
st.markdown("""
<div class='info-container'>
    <div class='section-title'>
        🔧 Teknologi yang Digunakan
    </div>
</div>
""", unsafe_allow_html=True)

# Baris pertama: Machine Learning dan Computer Vision
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='feature-box'>
        <div class='feature-title'>🤖 Machine Learning</div>
        <ul style='color: #5a5a5a; line-height: 1.7; font-size: 15px;'>
            <li><strong>Algoritma:</strong> Support Vector Machine (SVM)</li>
            <li><strong>Kernel:</strong> Radial Basis Function (RBF)</li>
            <li><strong>Classifier:</strong> Multi-class (One-vs-Rest)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box'>
        <div class='feature-title'>👁️ Computer Vision</div>
        <ul style='color: #5a5a5a; line-height: 1.7; font-size: 15px;'>
            <li><strong>OpenCV:</strong> Image processing</li>
            <li><strong>Grayscale Conversion:</strong> Preprocessing</li>
            <li><strong>Otsu Thresholding:</strong> Segmentation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Baris kedua: Feature Extraction dan Libraries
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='feature-box'>
        <div class='feature-title'>🔍 Feature Extraction</div>
        <ul style='color: #5a5a5a; line-height: 1.7; font-size: 15px;'>
            <li><strong>Color Features:</strong> RGB, HSV</li>
            <li><strong>Texture Features:</strong> GLCM (Energy, Contrast, Homogeneity, Correlation)</li>
            <li><strong>Shape Features:</strong> Area, Perimeter, Circularity</li>
            <li><strong>Statistical Features:</strong> Mean, Standard Deviation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box'>
        <div class='feature-title'>📦 Libraries</div>
        <ul style='color: #5a5a5a; line-height: 1.7; font-size: 15px;'>
            <li>Streamlit - Web framework</li>
            <li>scikit-learn - Machine Learning</li>
            <li>scikit-image - Texture analysis</li>
            <li>OpenCV - Image processing</li>
            <li>NumPy, Pandas - Data processing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section 4: Tips & Informasi Tambahan
st.markdown("""
<div class='info-container'>
    <div class='section-title'>
        💡 Tips & Informasi Tambahan
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='feature-box'>
        <div class='feature-title'>✨ Tips untuk Hasil Terbaik</div>
        <ul style='color: #5a5a5a; line-height: 1.7; font-size: 15px; margin-top: 10px;'>
            <li><strong>📸 Gunakan foto dengan pencahayaan yang baik</strong><br>
                <span style='font-size: 14px; color: #757575;'>Pencahayaan natural atau merata membantu sistem mendeteksi fitur dengan lebih akurat</span>
            </li>
            <li><strong>🎯 Pastikan biji kopi jelas dan fokus</strong><br>
                <span style='font-size: 14px; color: #757575;'>Gambar yang tajam memberikan detail yang lebih baik untuk analisis</span>
            </li>
            <li><strong>🖼️ Hindari background yang kompleks</strong><br>
                <span style='font-size: 14px; color: #757575;'>Background polos memudahkan sistem melakukan segmentasi objek</span>
            </li>
            <li><strong>📐 Foto dari atas (top-down view)</strong><br>
                <span style='font-size: 14px; color: #757575;'>Sudut pengambilan dari atas memberikan hasil terbaik untuk klasifikasi</span>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box' style='background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-left: 3px solid #2196f3;'>
        <div class='feature-title' style='color: #1565c0;'>⚠️ Disclaimer</div>
        <p style='color: #0d47a1; line-height: 1.7; font-size: 15px; margin-top: 10px;'>
        Sistem ini adalah <strong>prototype untuk penelitian dan pembelajaran</strong>. 
        Hasil klasifikasi tidak 100% akurat dan hanya untuk tujuan <strong>analisis awal</strong>. 
        Untuk keputusan bisnis atau kontrol kualitas produksi yang kritis, sangat disarankan 
        untuk melakukan verifikasi manual oleh ahli atau quality control bersertifikat.
        </p>
        <p style='color: #1565c0; line-height: 1.7; font-size: 14px; margin-top: 10px; font-style: italic;'>
        💡 Model ini terus dikembangkan untuk meningkatkan akurasi dan keandalan.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bottom Navigation with responsive buttons and brown styling
st.markdown("<br><br>", unsafe_allow_html=True)

# TOMBOL DI TENGAH - menggunakan 3 kolom dengan kolom tengah lebih besar
col1, col2, col3= st.columns([1, 3, 1])

with col2:
    # Sub-columns di dalam kolom tengah untuk dua tombol sampingan
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        if st.button("🏠 Kembali ke Beranda", type="primary", use_container_width=True, key="btn_home"):
            st.session_state.current_page = 'dashboard'
            st.switch_page("app.py")
    
    with subcol2:
        if st.button("🔍 Mulai Klasifikasi", type="primary", use_container_width=True, key="btn_classify"):
            st.session_state.current_page = 'klasifikasi'
            st.switch_page("pages/klasifikasi.py")

st.markdown("<br>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #8B7355; padding: 30px; background: linear-gradient(135deg, #f5f0e8 0%, #e8dcc8 100%); border-radius: 20px; margin-top: 40px;'>
        <p style='font-size: 16px; font-weight: 600; margin-bottom: 10px;'>© 2024 BeanClassify - Sistem Klasifikasi Kualitas Biji Kopi</p>
        <p style='font-size: 14px;'>Dibuat dengan ❤️ menggunakan Python dan Machine Learning</p>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")