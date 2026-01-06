"""
File CSS untuk styling aplikasi Streamlit (BeanClassify) - WARNA BARU
"""

# Warna tema baru sesuai permintaan
COLOR_BROWN_DARK = "#8B5E3C"      # Coklat Kopi (sidebar)
COLOR_BROWN_DARKER = "#6B4226"    # Coklat Kopi lebih gelap
COLOR_CREAM_LIGHT = "#F9E8D2"     # Krem Terang (background utama)
COLOR_CREAM_LIGHTER = "#F7E2C5"   # Krem lebih terang
COLOR_BROWN_MEDIUM = "#C69C72"    # Coklat Muda (kotak selamat datang)
COLOR_BROWN_LIGHT = "#DAB894"     # Coklat lebih muda
COLOR_BROWN_TEXT = "#3B2A1A"      # Coklat Gelap / Hitam Kopi (teks)
COLOR_BUTTON_ACTION = "#A86B43"   # Tombol Aksi - Coklat Medium

SIMPLE_CSS = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    /* Reset dasar */
    * {{
        font-family: 'Poppins', sans-serif;
    }}
    
    /* Background utama - Krem Terang */
    .stApp {{
        background-color: {COLOR_CREAM_LIGHT};
    }}
    
    /* Sidebar - Coklat Kopi */
    section[data-testid="stSidebar"] {{
        background-color: {COLOR_BROWN_DARK};
        background-image: linear-gradient(135deg, {COLOR_BROWN_DARK} 0%, {COLOR_BROWN_DARKER} 100%);
    }}
    
    /* Sidebar content */
    [data-testid="stSidebar"] * {{
        color: {COLOR_CREAM_LIGHT};
    }}
    
    /* SEMBUNYIKAN NAVIGASI DEFAULT STREAMLIT */
    [data-testid="stSidebarNav"] {{
        display: none !important;
    }}
    
    /* TOMBOL SIDEBAR */
    section[data-testid="stSidebar"] .stButton > button {{
        background: transparent !important;
        border: none !important;
        color: {COLOR_CREAM_LIGHT} !important;
        font-weight: 500;
        text-align: left;
        padding: 0.5rem 0.8rem !important;
        width: 100%;
        border-radius: 8px !important;
        box-shadow: none !important;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        margin: 0.1rem 0 !important;
        min-height: auto !important;
        transition: all 0.1s ease;
    }}
    
    section[data-testid="stSidebar"] .stButton > button:hover {{
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: {COLOR_CREAM_LIGHT} !important;
        transform: translateX(8px);
        border-color: rgba(255, 255, 255, 0.3) !important;
    }}
    
    /* Tombol aktif di sidebar */
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] {{
        background-color: {COLOR_BUTTON_ACTION} !important;
        border-color: {COLOR_BROWN_LIGHT} !important;
        font-weight: 600;
    }}
    
    /* TOMBOL UTAMA DI CONTENT (FIX WARNA + RESPONSIVE) */
    .stButton > button[kind="primary"] {{
        background-color: {COLOR_BUTTON_ACTION} !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.2rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px rgba(168, 107, 67, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        min-width: auto !important;
        white-space: normal !important;
        line-height: 1.4 !important;
        min-height: 44px !important;
    }}
    
    .stButton > button[kind="primary"]:hover {{
        background-color: {COLOR_BROWN_DARKER} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(168, 107, 67, 0.4) !important;
    }}
    
    /* HILANGKAN BORDER PADA TOMBOL SECONDARY */
    section[data-testid="stSidebar"] .stButton > button[kind="secondary"] {{
        background: transparent !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: {COLOR_CREAM_LIGHT} !important;
        box-shadow: none !important;
    }}
    
    /* Sidebar header custom */
    .sidebar-header {{
        text-align: center;
        padding: 1rem 0.5rem 0.5rem 0.5rem;
        border-bottom: 2px solid {COLOR_BUTTON_ACTION};
        margin-bottom: 0.3rem;
        border-radius: 5px;
        background: linear-gradient(135deg, {COLOR_BROWN_MEDIUM} 0%, {COLOR_BROWN_DARK} 0%);
    }}
    
    .logo-full {{
        width: 100% !important;
        max-width: 700px !important;
        height: auto !important;
        margin: 0 auto 0.1rem auto !important;
        display: block;
        border-radius: 0px;
        box-shadow: 0 4px 0px rgba(0, 0, 0, 0.2);
    }}
    
    .app-title {{
        color: {COLOR_CREAM_LIGHT};
        font-size: 1.8rem !important;
        font-weight: 700;
        margin: 0.2rem 0 0.1rem 0 !important;
        line-height: 1.2 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }}
    
    .app-subtitle {{
        color: {COLOR_CREAM_LIGHT};
        font-size: 1rem !important;
        margin: 0 !important;
        opacity: 0.9;
        line-height: 1.3 !important;
        font-weight: 400;
    }}
    
    /* KONTAINER NAVIGASI */
    .nav-container {{
        display: flex;
        flex-direction: column;
        gap: 0rem !important;
        margin-top: 0.3rem !important;
        padding: 0 0.2rem;
    }}
    
    /* Header utama - Coklat Gelap */
    .main-header {{
        font-size: 2.2rem;
        font-weight: 800;
        text-align: center;
        color: {COLOR_BROWN_TEXT};
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    
    /* Sub header */
    .sub-header {{
        font-size: 1.1rem;
        text-align: center;
        color: {COLOR_BROWN_TEXT};
        margin-bottom: 2rem;
        opacity: 0.8;
        font-weight: 400;
    }}
    
    /* Styling untuk konten kartu (Selamat Datang) - DIKECILKAN */
    .welcome-card {{
        background: linear-gradient(135deg, {COLOR_BROWN_MEDIUM} 0%, {COLOR_BROWN_LIGHT} 100%);
        border-radius: 16px;
        padding: 1.5rem !important;  /* DIKECILKAN dari 2rem */
        margin: 1rem auto !important;
        border: none;
        box-shadow: 0 8px 24px rgba(198, 156, 114, 0.2);
        color: {COLOR_BROWN_TEXT};
        max-width: 600px !important;  /* DIKECILKAN dari 800px */
    }}
    
    /* CONTAINER TOMBOL TENGAH */
    .button-center-container {{
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1rem auto;
        max-width: 600px;
        padding: 0 1rem;
    }}
    
    /* RESPONSIVE DESIGN UNTUK BUTTON PRIMARY */
    @media (max-width: 768px) {{
        .stButton > button[kind="primary"] {{
            font-size: 0.9rem !important;
            padding: 0.5rem 1rem !important;
            min-height: 42px !important;
        }}
    }}
    
    @media (max-width: 576px) {{
        .stButton > button[kind="primary"] {{
            font-size: 0.85rem !important;
            padding: 0.5rem 0.8rem !important;
            min-height: 40px !important;
        }}
    }}
    
    @media (max-width: 400px) {{
        .stButton > button[kind="primary"] {{
            font-size: 0.75rem !important;
            padding: 0.4rem 0.6rem !important;
            min-height: 38px !important;
        }}
    }}
    
    /* Sembunyikan elemen default */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
</style>
"""

# CSS untuk dashboard
DASHBOARD_STYLES = SIMPLE_CSS

# CSS untuk halaman lain  
COMMON_STYLES = SIMPLE_CSS

# Fungsi untuk membuat kartu selamat datang
def create_welcome_card():
    import streamlit as st
    
    st.markdown(
        f"""
        <div class="welcome-card">
            <h2 style="color: {COLOR_BROWN_TEXT}; margin-bottom: 1rem;">☕ Selamat Datang di BeanClassify!</h2>
            <p style="color: {COLOR_BROWN_TEXT}; line-height: 1.6;">
                Sistem ini menggunakan teknologi Machine Learning untuk mengklasifikasikan 
                kualitas biji kopi menjadi 3 kategori dengan akurasi tinggi.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Fungsi sidebar header dengan navigasi
def display_sidebar_header():
    import streamlit as st
    import os
    
    # Logo path - coba beberapa lokasi
    logo_paths = [
        "assets/logo3.png",
        "logo3.png", 
        "../assets/logo3.png",
        "./assets/logo3.png"
    ]
    
    logo_src = ""
    logo_found = False
    
    # Cari logo di beberapa lokasi
    for path in logo_paths:
        if os.path.exists(path):
            try:
                import base64
                with open(path, "rb") as img_file:
                    img_data = base64.b64encode(img_file.read()).decode()
                    logo_src = f"data:image/png;base64,{img_data}"
                    logo_found = True
                    break
            except Exception as e:
                continue
    
    # Jika logo tidak ditemukan, gunakan placeholder
    if not logo_found:
        st.sidebar.markdown(
            f"""
            <div class="sidebar-header">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">☕</div>
                <h1 class="app-title">BeanClassify</h1>
                <p class="app-subtitle">Klasifikasi Kualitas Biji Kopi</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        # Tampilkan sidebar header dengan logo
        st.sidebar.markdown(
            f"""
            <div class="sidebar-header">
                <img src="{logo_src}" class="logo-full" alt="BeanClassify Logo">
                <h1 class="app-title">BeanClassify</h1>
                <p class="app-subtitle">Klasifikasi Kualitas Biji Kopi</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Definisikan halaman
    pages = [
        {"name": "Beranda", "target": "dashboard"},
        {"name": "Klasifikasi", "target": "klasifikasi"},
        {"name": "Tentang Sistem", "target": "tentang"}
    ]
    
    # Container untuk navigasi
    st.sidebar.markdown('<div class="nav-container">', unsafe_allow_html=True)
    
    # Tampilkan navigasi sebagai tombol
    for page in pages:
        if st.sidebar.button(
            page["name"],
            key=page["target"],
            use_container_width=True,
            type="primary" if st.session_state.get('current_page') == page["target"] else "secondary"
        ):
            # Set session state untuk halaman aktif
            st.session_state.current_page = page["target"]
            
            # Navigasi ke halaman yang sesuai
            if page["target"] == "klasifikasi":
                st.switch_page("pages/klasifikasi.py")
            elif page["target"] == "tentang":
                st.switch_page("pages/tentang.py")
            elif page["target"] == "dashboard":
                st.rerun()
    
    st.sidebar.markdown('</div>', unsafe_allow_html=True)

HIDE_ST_STYLE = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""