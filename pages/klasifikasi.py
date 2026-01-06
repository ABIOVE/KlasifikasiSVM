import streamlit as st
import cv2
import numpy as np
import joblib
from PIL import Image
import io
import os
import matplotlib.pyplot as plt
from skimage.feature import graycomatrix, graycoprops
from styles import COMMON_STYLES, HIDE_ST_STYLE, display_sidebar_header


# Page config
st.set_page_config(
    page_title="BeanClassify - Klasifikasi",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Remove default menu
st.markdown(HIDE_ST_STYLE, unsafe_allow_html=True)
# Custom CSS
st.markdown(COMMON_STYLES, unsafe_allow_html=True)

# CSS LENGKAP untuk halaman klasifikasi - DIPERBAIKI
COMPLETE_UPLOAD_STYLES = """
<style>
    /* Hide default Streamlit file uploader */
    div[data-testid="stFileUploader"] {
        position: relative;
        width: 100%;
        max-width: 600px;
        margin: 0 auto !important;
    }
    
    div[data-testid="stFileUploader"] > label {
        display: none !important;
    }
    
    div[data-testid="stFileUploader"] > div {
        border: none !important;
        padding: 0 !important;
        background: transparent !important;
        margin: 0 !important;
    }
    
    div[data-testid="stFileUploader"] section {
        border: none !important;
        padding: 0 !important;
        background: transparent !important;
        margin: 0 !important;
    }
    
    div[data-testid="stFileUploader"] button {
        background-color: #8B5E3C !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
    }
    
    div[data-testid="stFileUploader"] button:hover {
        background-color: #6D4C2F !important;
    }
    
    /* Style untuk area drag and drop bawaan streamlit - WARNA COKLAT */
    div[data-testid="stFileUploader"] section > div {
        border-color: #A86B43 !important;
        background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%) !important;
        margin: 0 !important;
    }
    
    /* Custom upload box styling - WARNA COKLAT KEMERAHAN */
    .custom-upload-box {
        background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%);
        border: 3px dashed #A86B43;
        border-radius: 24px;
        padding: 2rem 2rem;
        text-align: center;
        margin: 2rem auto;
        max-width: 600px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        box-shadow: 0 8px 24px rgba(168, 107, 67, 0.15);
        position: relative;
        overflow: hidden;
    }
    
    .custom-upload-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(168, 107, 67, 0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
    }
    
    .custom-upload-box:hover {
        border-color: #8B5E3C;
        background: linear-gradient(135deg, #FEF9F4 0%, #FCECD5 100%);
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(168, 107, 67, 0.25);
        border-width: 3px;
    }
    
    .custom-upload-box:hover::before {
        opacity: 1;
    }
    
    .custom-upload-box:active {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(168, 107, 67, 0.2);
    }
    
    /* Upload icon animation */
    .upload-icon-animated {
        font-size: 4rem;
        color: #8B5E3C;
        margin-bottom: 0.5rem;
        display: inline-block;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 4px 8px rgba(139, 94, 60, 0.2);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .custom-upload-box:hover .upload-icon-animated {
        animation: bounce 0.6s ease-in-out;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        25% { transform: translateY(-15px); }
        50% { transform: translateY(-8px); }
        75% { transform: translateY(-12px); }
    }
    
    /* Text styling - WARNA COKLAT */
    .upload-text-primary {
        font-size: 1.4rem;
        font-weight: 700;
        color: #3B2A1A;
        margin-bottom: 0.3rem;
        letter-spacing: 0.5px;
    }
    
    /* STYLING KHUSUS UNTUK TOMBOL MULAI ANALISIS SAJA */
    /* Target tombol dengan key start_analysis_btn */
    button[kind="primary"][data-testid="baseButton-primary"][key="start_analysis_btn"] {
        background-color: #27AE60 !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
    }
    
    button[kind="primary"][data-testid="baseButton-primary"][key="start_analysis_btn"]:hover {
        background-color: #229954 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(39, 174, 96, 0.3) !important;
    }
    
    button[kind="primary"][data-testid="baseButton-primary"][key="start_analysis_btn"]:active {
        transform: translateY(0px);
        box-shadow: 0 2px 8px rgba(39, 174, 96, 0.2) !important;
    }

    /* PERBAIKAN: Styling tombol Hapus dengan warna soft coklat */
    .stButton > button[kind="secondary"] {
        background-color: #B3543A !important;
        color: white !important;
        border: none !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
    }

    .stButton > button[kind="secondary"]:hover {
        background-color: #9A4A32 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(179, 84, 58, 0.25) !important;
    }

    .stButton > button[kind="secondary"]:active {
        transform: translateY(0px);
        box-shadow: 0 2px 8px rgba(179, 84, 58, 0.2) !important;
    }
    
    .upload-text-info {
        font-size: 0.85rem;
        color: #A86B43;
        opacity: 0.8;
        font-weight: 500;
        margin-top: 0.5rem;
        padding: 0.4rem 1rem;
        background: rgba(255, 255, 255, 0.6);
        border-radius: 8px;
        display: inline-block;
    }
    
    /* Preview container - DIPERKECIL */
    .preview-box {
        background: white;
        border-radius: 12px;
        padding: 0.5rem 1rem;
        margin: 40px auto;
        max-width: 280px;
        box-shadow: 0 2px 12px rgba(139, 94, 60, 0.1);
        border: 2px solid #F7E2C5;
        text-align: center;
        animation: fadeIn 0.4s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .preview-box h4 {
        color: #8B5E3C;
        margin: 0;
        font-size: 0.95rem;
        font-weight: 600;
    }
    
    /* Container untuk hasil - TANPA KOTAK PUTIH BESAR */
    .result-section {
        margin: 2rem auto;
        max-width: 1200px;
    }
    
    /* Header hasil analisis di dalam kotak - DIPERBESAR DAN GRADASI COKLAT */
    .result-header-box {
        background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%);
        border-radius: 16px;
        padding: 1.2rem 1.2rem;
        margin-top: 0.3rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(139, 94, 60, 0.15);
        border: 2px solid #D4A574;
        text-align: center;
        display: inline-block;
        margin-left: auto;
        margin-right: auto;
        width: auto;
    }
    
    .result-header-box h3 {
        color: #3B2A1A;
        margin-top: 0px;
        font-size: 1.7rem;
        font-weight: 800;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Header utama dengan dua baris */
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
    
    /* Container untuk tombol aksi - DIPERBAIKI AGAR SEJAJAR DAN LEBIH KECIL */
    .action-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        margin-top: 10px;
        max-width: 700px;
        padding: 0 1rem;
    }
    
    .action-container > div {
        flex: 1;
        max-width: 340px;
        display: flex;
    }
    
    .action-container .stButton {
        flex: 1;
        display: flex;
    }
    
    .action-container .stButton > button {
        width: 100% !important;
        white-space: nowrap;
        padding: 0.6rem 1rem !important;
        font-size: 0.95rem !important;
        height: 100%;
    }
    
    /* Fix untuk alignment columns Streamlit */
    .action-container > div[data-testid="column"] {
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Container tombol navigasi - DIPERBAIKI AGAR CENTER */
    .nav-buttons-wrapper {
        max-width: 700px;
        margin: 10px;
        padding: 0 1rem;
    }
    
    .nav-buttons-container {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        align-items: stretch !important;
        gap: 1.5rem !important;
        margin: 1.5rem auto !important;
    }
    
    .nav-buttons-container > div[data-testid="column"] {
        flex: 1 1 0px !important;
        max-width: 340px !important;
        min-width: 0 !important;
    }
    
    .nav-buttons-container .element-container {
        display: flex !important;
        width: 100% !important;
    }
    
    .nav-buttons-container .stButton {
        width: 100% !important;
        display: flex !important;
    }
    
    .nav-buttons-container .stButton > button {
        width: 100% !important;
        height: auto !important;
        min-height: 45px !important;
    }

    /* RESPONSIVE: Media queries untuk layar kecil */
    @media screen and (max-width: 768px) {
        .nav-buttons-wrapper {
            max-width: 100% !important;
            padding: 0 0.5rem !important;
        }
        
        .nav-buttons-container {
            flex-direction: column !important;
            gap: 1rem !important;
        }
        
        .nav-buttons-container > div[data-testid="column"] {
            max-width: 100% !important;
            width: 100% !important;
        }
        
        .nav-buttons-container .stButton > button {
            font-size: 0.9rem !important;
            padding: 0.7rem 1rem !important;
        }
    }
    
    @media screen and (max-width: 480px) {
        .nav-buttons-container .stButton > button {
            font-size: 0.85rem !important;
            padding: 0.6rem 0.8rem !important;
        }
        
        .explanation-text {
            font-size: 0.85rem !important;
        }
    }
    
    /* Teks penjelas - CENTER */
    .explanation-text {
        text-align: center;
        color: #8B5E3C;
        font-size: 0.95rem;
        margin: 1.5rem auto;
        opacity: 0.85;
        max-width: 600px;
    }
    
    /* Status indikator */
    .status-good { color: #27AE60; font-weight: 600; }
    .status-fair { color: #F39C12; font-weight: 600; }
    .status-poor { color: #E74C3C; font-weight: 600; }
    
    /* PERBAIKAN: Container untuk ringkasan kualitas - MARGIN DIKURANGI */
    .quality-summary-box {
        text-align: center;
        padding: 1rem;
        background: #E8F8F5;
        border-radius: 12px;
        border: 2px solid #27AE60;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .quality-summary-box h2 {
        margin: 0 0 0.3rem 0 !important;
        font-size: 1.3rem;
    }
    
    .quality-summary-box h1 {
        margin: 0.2rem 0 !important;
        font-size: 2.5rem;
    }
    
    .quality-summary-box p {
        margin: 0.2rem 0 0 0 !important;
        font-size: 1rem;
    }
    
    /* Probabilitas dengan warna - DITAMBAHKAN */
    .prob-label-bagus { color: #27AE60 !important; font-weight: 700 !important; }
    .prob-label-rusak { color: #E74C3C !important; font-weight: 700 !important; }
    .prob-label-jamur { color: #F39C12 !important; font-weight: 700 !important; }
</style>
"""

# Apply styles
st.markdown(COMPLETE_UPLOAD_STYLES, unsafe_allow_html=True)

# JavaScript untuk integrasi upload
UPLOAD_JS = """
<script>
function initCustomUploader() {
    const fileUploader = document.querySelector('input[type="file"]');
    const customBox = document.getElementById('custom-upload-trigger');
    
    if (fileUploader && customBox) {
        customBox.addEventListener('click', function(e) {
            e.preventDefault();
            fileUploader.click();
        });
        
        customBox.addEventListener('dragover', function(e) {
            e.preventDefault();
            e.stopPropagation();
            customBox.classList.add('drag-over');
        });
        
        customBox.addEventListener('dragleave', function(e) {
            e.preventDefault();
            e.stopPropagation();
            customBox.classList.remove('drag-over');
        });
        
        customBox.addEventListener('drop', function(e) {
            e.preventDefault();
            e.stopPropagation();
            customBox.classList.remove('drag-over');
            
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                const dataTransfer = new DataTransfer();
                for (let file of files) {
                    dataTransfer.items.add(file);
                }
                fileUploader.files = dataTransfer.files;
                
                const event = new Event('change', { bubbles: true });
                fileUploader.dispatchEvent(event);
            }
        });
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCustomUploader);
} else {
    initCustomUploader();
}

setTimeout(initCustomUploader, 500);
</script>
"""

# Set current page untuk navigasi
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'klasifikasi'

# Tampilkan sidebar header dengan navigasi
display_sidebar_header()

# Handle navigasi
if st.session_state.current_page == 'dashboard':
    st.switch_page("app.py")
elif st.session_state.current_page == 'tentang':
    st.switch_page("pages/tentang.py")

# Load model functions
@st.cache_resource
def load_model():
    """Load the trained model and scaler"""
    try:
        model_path = 'd:\Sem 7\PP_AAA\Rampung\Model_SVM.pkl'
        scaler_path = 'D:\Sem 7\PP_AAA\Rampung\Model_Scaler.pkl'
        
        if not os.path.exists(model_path) or not os.path.exists(scaler_path):
            st.error("Model tidak ditemukan! Pastikan file model ada di direktori.")
            return None, None
        
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

# Preprocessing functions
def sharpen_image_fast(image):
    """Sharpening yang lebih cepat"""
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def reduce_blur_fast(image):
    """Denoising yang lebih cepat"""
    denoised = cv2.medianBlur(image, 3)
    sharpened = sharpen_image_fast(denoised)
    return sharpened

def segment_image_otsu(img_gray):
    """Otsu thresholding"""
    try:
        _, binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary
    except Exception as e:
        st.error(f"Error in segmentation: {str(e)}")
        return None

def extract_features(img_gray, img_rgb, binary):
    """Extract features from image"""
    features = {}
    
    # Color features
    mask = binary > 0
    if np.sum(mask) > 0:
        features['red_mean'] = np.mean(img_rgb[:, :, 0][mask])
        features['green_mean'] = np.mean(img_rgb[:, :, 1][mask])
        features['blue_mean'] = np.mean(img_rgb[:, :, 2][mask])
        
        img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
        features['hue_mean'] = np.mean(img_hsv[:, :, 0][mask])
        features['saturation_mean'] = np.mean(img_hsv[:, :, 1][mask])
        features['value_mean'] = np.mean(img_hsv[:, :, 2][mask])
    else:
        features.update({
            'red_mean': np.mean(img_rgb[:, :, 0]),
            'green_mean': np.mean(img_rgb[:, :, 1]),
            'blue_mean': np.mean(img_rgb[:, :, 2]),
            'hue_mean': 90, 'saturation_mean': 100, 'value_mean': 100
        })
    
    # Texture features
    img_uint8 = img_gray.astype(np.uint8)
    glcm = graycomatrix(img_uint8, distances=[1, 3], angles=[0], 
                      levels=256, symmetric=True, normed=True)
    
    features['energy'] = np.mean(graycoprops(glcm, 'energy'))
    features['contrast'] = np.mean(graycoprops(glcm, 'contrast'))
    features['homogeneity'] = np.mean(graycoprops(glcm, 'homogeneity'))
    features['correlation'] = np.mean(graycoprops(glcm, 'correlation'))
    
    # Shape features
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        main_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(main_contour)
        perimeter = cv2.arcLength(main_contour, True)
        
        features['area'] = area
        features['perimeter'] = perimeter
        
        if perimeter > 0:
            features['circularity'] = (4 * np.pi * area) / (perimeter ** 2)
        else:
            features['circularity'] = 0
    else:
        features.update({'area': 0, 'perimeter': 0, 'circularity': 0})
    
    # Statistical features
    features['intensity_mean'] = np.mean(img_gray)
    features['intensity_std'] = np.std(img_gray)
    
    return features

def classify_single_bean(image, model, scaler):
    """Klasifikasi gambar dengan SATU BIJI KOPI"""
    try:
        if isinstance(image, Image.Image):
            img_array = np.array(image)
            img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        else:
            img_bgr = image
            
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        
        img_rgb = cv2.resize(img_rgb, (400, 400))
        img_gray = cv2.resize(img_gray, (400, 400))
        
        img_gray = reduce_blur_fast(img_gray)
        binary = segment_image_otsu(img_gray)
        
        features = extract_features(img_gray, img_rgb, binary)
        
        feature_names = ['red_mean', 'green_mean', 'blue_mean', 'hue_mean', 
                        'saturation_mean', 'value_mean', 'energy', 'contrast', 
                        'homogeneity', 'correlation', 'area', 'perimeter', 
                        'circularity', 'intensity_mean', 'intensity_std']
        
        feature_vector = np.array([[features[name] for name in feature_names]])
        feature_scaled = scaler.transform(feature_vector)
        
        probabilities = model.predict_proba(feature_scaled)[0]
        predicted_class_idx = np.argmax(probabilities)
        prediction = model.classes_[predicted_class_idx]
        confidence = probabilities[predicted_class_idx] * 100
        
        return prediction, confidence, img_rgb, binary, probabilities
        
    except Exception as e:
        st.error(f"Error in single bean classification: {e}")
        return None, 0, None, None, None

def detect_multiple_beans(image, model, scaler, min_area=300, max_area=5000):
    """Deteksi gambar dengan MULTIPLE BIJI KOPI"""
    try:
        if isinstance(image, Image.Image):
            img_array = np.array(image)
            img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        else:
            img_bgr = image
            
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        
        scale_factor = 400 / max(img_gray.shape)
        new_width = int(img_gray.shape[1] * scale_factor)
        new_height = int(img_gray.shape[0] * scale_factor)
        
        img_rgb_detection = cv2.resize(img_rgb, (new_width, new_height))
        img_gray_detection = cv2.resize(img_gray, (new_width, new_height))
        
        img_blur = cv2.GaussianBlur(img_gray_detection, (5, 5), 0)
        
        binary_adaptive = cv2.adaptiveThreshold(
            img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, 11, 2
        )
        
        _, binary_otsu = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        contours_adaptive, _ = cv2.findContours(binary_adaptive, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_otsu, _ = cv2.findContours(binary_otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        meaningful_adaptive = [c for c in contours_adaptive if min_area <= cv2.contourArea(c) <= max_area]
        meaningful_otsu = [c for c in contours_otsu if min_area <= cv2.contourArea(c) <= max_area]
        
        if len(meaningful_adaptive) >= len(meaningful_otsu):
            binary_used = binary_adaptive
            contours = contours_adaptive
        else:
            binary_used = binary_otsu
            contours = contours_otsu
        
        kernel = np.ones((3, 3), np.uint8)
        binary_cleaned = cv2.morphologyEx(binary_used, cv2.MORPH_CLOSE, kernel)
        binary_cleaned = cv2.morphologyEx(binary_cleaned, cv2.MORPH_OPEN, kernel)
        
        contours, _ = cv2.findContours(binary_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        bean_results = []
        img_display = img_rgb_detection.copy()
        colors = {'Bagus': (0, 255, 0), 'Rusak': (255, 0, 0), 'Jamur': (255, 165, 0)}
        
        meaningful_contours = [c for c in contours if min_area <= cv2.contourArea(c) <= max_area]
        
        if len(meaningful_contours) <= 1:
            return [], None
        
        for i, contour in enumerate(meaningful_contours):
            area = cv2.contourArea(contour)
            
            if min_area <= area <= max_area:
                x, y, w, h = cv2.boundingRect(contour)
                
                padding = 8
                x1 = max(0, x - padding)
                y1 = max(0, y - padding)
                x2 = min(img_rgb_detection.shape[1], x + w + padding)
                y2 = min(img_rgb_detection.shape[0], y + h + padding)
                
                roi_rgb = img_rgb_detection[y1:y2, x1:x2]
                roi_gray = img_gray_detection[y1:y2, x1:x2]
                
                if roi_rgb.size == 0 or roi_gray.size == 0:
                    continue
                
                roi_rgb_resized = cv2.resize(roi_rgb, (400, 400))
                roi_gray_resized = cv2.resize(roi_gray, (400, 400))
                
                roi_gray_processed = reduce_blur_fast(roi_gray_resized)
                roi_binary = segment_image_otsu(roi_gray_processed)
                
                features = extract_features(roi_gray_processed, roi_rgb_resized, roi_binary)
                
                if features:
                    feature_names = ['red_mean', 'green_mean', 'blue_mean', 'hue_mean', 
                                    'saturation_mean', 'value_mean', 'energy', 'contrast', 
                                    'homogeneity', 'correlation', 'area', 'perimeter', 
                                    'circularity', 'intensity_mean', 'intensity_std']
                    
                    feature_vector = [features[name] for name in feature_names]
                    
                    feature_scaled = scaler.transform([feature_vector])
                    probabilities = model.predict_proba(feature_scaled)[0]
                    predicted_class_idx = np.argmax(probabilities)
                    prediction = model.classes_[predicted_class_idx]
                    confidence = probabilities[predicted_class_idx] * 100
                    
                    if confidence > 60:
                        bean_results.append({
                            'bean_id': len(bean_results) + 1,
                            'prediction': prediction,
                            'confidence': confidence,
                            'bbox': (x, y, w, h),
                            'area': area,
                            'is_single_bean': False
                        })
                        
                        color = colors.get(prediction, (255, 255, 255))
                        cv2.rectangle(img_display, (x, y), (x+w, y+h), color, 2)
                        
                        label_text = f"{prediction}({confidence:.0f}%)"
                        cv2.putText(img_display, label_text, (x, y-10), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        return bean_results, img_display
        
    except Exception as e:
        st.error(f"Error in multiple beans detection: {e}")
        return None, None

def smart_coffee_analysis(image, model, scaler):
    """SMART ANALYSIS: Otomatis deteksi jenis gambar"""
    bean_results, detection_img = detect_multiple_beans(image, model, scaler)
    
    if bean_results is None:
        return None
    
    if len(bean_results) <= 1:
        single_pred, single_conf, img_rgb, binary, probabilities = classify_single_bean(image, model, scaler)
        
        if single_pred:
            return {
                'analysis_type': 'SINGLE_BEAN',
                'prediction': single_pred,
                'confidence': single_conf,
                'probabilities': probabilities,
                'processed_image': img_rgb,
                'binary_image': binary,
                'bean_count': 1
            }
        else:
            return None
    else:
        class_counts = {}
        for res in bean_results:
            class_name = res['prediction']
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
        
        return {
            'analysis_type': 'MULTIPLE_BEANS',
            'bean_detections': bean_results,
            'class_distribution': class_counts,
            'detection_image': detection_img,
            'total_beans': len(bean_results)
        }

import base64

def get_base64_of_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Logo tidak ditemukan: {image_path}")
        return None

logo_base64 = get_base64_of_image("assets/logo3.png")

# Main app
st.markdown(
    f'''
    <div class="main-header-container">
        <div class="main-header-line1">Klasifikasi Kualitas Biji Kopi</div>
        <div class="main-header-line2" style= "color: #4B2E05; font-family: Playfair Display">
        <img src="data:image/png;base64,{logo_base64}" width="50" style="vertical-align: middle;">
        Smart Analysis
        <img src="data:image/png;base64,{logo_base64}" width="50"
        </div>
    </div>
    ''', 
        unsafe_allow_html=True
    )

# Load model
with st.spinner("Loading model..."):
    model, scaler = load_model()

if model is None or scaler is None:
    st.stop()

# Initialize session state
if 'uploaded_file_state' not in st.session_state:
    st.session_state.uploaded_file_state = None

# Inject JavaScript
st.markdown(UPLOAD_JS, unsafe_allow_html=True)

# Custom upload box (tampil jika belum ada file)
if st.session_state.uploaded_file_state is None:
    st.markdown("""
        <div id="custom-upload-trigger" class="custom-upload-box">
            <div class="upload-icon-animated">📷</div>
            <div class="upload-text-primary">Klik di sini untuk mengunggah gambar</div>
            <div class="upload-text-secondary">atau seret dan jatuhkan gambar ke area ini</div>
            <div class="upload-text-info">Format: JPG, PNG, JPEG • Maks: 200MB</div>
        </div>
    """, unsafe_allow_html=True)

# File uploader (tersembunyi via CSS)
uploaded_file = st.file_uploader(
    "Upload",
    type=['jpg', 'jpeg', 'png', 'webp'],
    help="Format yang didukung: JPG, JPEG, PNG, WEBP. Ukuran maksimum: 100MB.",
    key="file-upload",
    label_visibility="collapsed"
)

# Update session state
if uploaded_file is not None:
    st.session_state.uploaded_file_state = uploaded_file

# Tampilkan preview jika ada file
if st.session_state.uploaded_file_state is not None:
    # Kotak sukses yang lebih kecil
    st.markdown("""
        <div class="preview-box">
            <h4>✅ Gambar Berhasil Diunggah</h4>
        </div>
    """, unsafe_allow_html=True)
    
    # Container untuk gambar dengan ukuran terbatas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        image = Image.open(st.session_state.uploaded_file_state)
        st.image(image, caption="📸 Preview Gambar", use_container_width=True)
    
    # Container untuk tombol dengan lebar penuh yang sama - DIPERBAIKI AGAR SEJAJAR
    st.markdown('<div class="action-container">', unsafe_allow_html=True)
    
    # TOMBOL DI TENGAH - menggunakan 3 kolom dengan kolom tengah lebih besar
    col1, col2, col3 = st.columns([1, 2.5, 1])
    
    with col2:
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            # Tombol Hapus dengan warna merah
            if st.button("🗑️ Hapus & Unggah Gambar Baru", type="secondary", use_container_width=True, key="clear_image_btn"):
                st.session_state.uploaded_file_state = None
                if 'file-upload' in st.session_state:
                    del st.session_state['file-upload']
                st.rerun()
        
        with col_btn2:
            # Tombol Mulai Analisis dengan styling khusus
            start_analysis = st.button("🚀 Mulai Analisis", type="primary", use_container_width=True, key="start_analysis_btn")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    if start_analysis:
        try:
            image = Image.open(st.session_state.uploaded_file_state)
            
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            with st.spinner("Menganalisis gambar dengan smart analysis..."):
                results = smart_coffee_analysis(image, model, scaler)
                
                if results:
                    # Container untuk hasil tanpa kotak putih besar
                    st.markdown('<div class="result-section">', unsafe_allow_html=True)
                    
                    # Header dalam kotak kecil yang center - DIPERBESAR DAN GRADASI COKLAT
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.markdown("""
                            <div class="result-header-box">
                                <h3>Hasil Analisis Klasifikasi Gambar Biji Kopi</h3>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    if results['analysis_type'] == 'SINGLE_BEAN':
                        prediction = results['prediction']
                        confidence = results['confidence']
                        probabilities = results['probabilities']
                        
                        col1, col2, col3 = st.columns(3)
                        
                        color_map = {
                            'Bagus': '🟢',
                            'Rusak': '🔴',
                            'Jamur': '🟠'
                        }
                        
                        status_class = "status-good" if prediction == 'Bagus' else "status-fair" if prediction == 'Jamur' else "status-poor"
                        
                        with col2:
                            st.markdown(f"""
                                <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%); border-radius: 12px; border-left: 4px solid #A86B43;">
                                    <h3 style="margin: 0; color: #3B2A1A;">Prediksi Kualitas:</h3>
                                    <h2 style="margin: 0.5rem 0; color: #3B2A1A;">{color_map.get(prediction, '❓')} {prediction}</h2>
                                    <p class="{status_class}" style="font-size: 1.2rem; margin: 0;">{confidence:.1f}% confidence</p>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        st.markdown("<h4 style='text-align: center; margin-top: 40px'>Probabilitas Klasifikasi</h4>", unsafe_allow_html=True)
                        
                        # Probabilitas dalam satu baris dengan warna - DITAMBAHKAN WARNA
                        cols = st.columns(3)
                        class_order = list(model.classes_)
                        class_colors = {
                            'Bagus': 'prob-label-bagus',
                            'Rusak': 'prob-label-rusak',
                            'Jamur': 'prob-label-jamur'
                        }
                        class_icons = {
                            'Bagus': '🟢',
                            'Rusak': '🔴',
                            'Jamur': '🟠'
                        }
                        
                        for i, cls in enumerate(class_order):
                            with cols[i]:
                                prob = probabilities[i] * 100
                                color_class = class_colors.get(cls, '')
                                icon = class_icons.get(cls, '')
                                st.markdown(f"<p class='{color_class}'><strong>{icon} {cls}: {prob:.1f}%</strong></p>", unsafe_allow_html=True)
                                st.progress(prob / 100)
                        
                        st.markdown("<h5 style='text-align: center; margin-top: 40px'>🖼️ Hasil Preprocessing</h5>", unsafe_allow_html=True)
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            if results['processed_image'] is not None:
                                st.image(results['processed_image'], caption="RGB Processed", use_container_width=True)
                        
                        with col2:
                            if results['processed_image'] is not None:
                                img_gray = cv2.cvtColor(results['processed_image'], cv2.COLOR_RGB2GRAY)
                                img_gray_rgb = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
                                st.image(img_gray_rgb, caption="Grayscale", use_container_width=True)
                        
                        with col3:
                            if results['binary_image'] is not None:
                                binary_rgb = cv2.cvtColor(results['binary_image'], cv2.COLOR_GRAY2RGB)
                                st.image(binary_rgb, caption="Segmentasi (Otsu)", use_container_width=True)
                        
                        if prediction == 'Bagus':
                            st.success("✅ Biji kopi berkualitas baik! Siap untuk proses roasting.")
                        elif prediction == 'Rusak':
                            st.warning("⚠️ Biji kopi terdeteksi rusak atau patah. Perlu diseleksi ulang.")
                        else:
                            st.error("🍄 Biji kopi terdeteksi berjamur. Tidak disarankan untuk diproses.")
                    
                    else:
                        # MULTIPLE BEANS - Preview gambar diperkecil
                        bean_detections = results['bean_detections']
                        class_distribution = results['class_distribution']
                        total_beans = results['total_beans']
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown(f"""
                                <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%); border-radius: 12px; border-left: 4px solid #A86B43;">
                                    <h3 style="margin: 0; color: #3B2A1A;">Total Biji Terdeteksi</h3>
                                    <h1 style="margin: 0.5rem 0; color: #3B2A1A;">{total_beans}</h1>
                                    <p style="color: #8B5E3C; margin: 0;">Multiple Beans</p>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            if class_distribution:
                                majority_class = max(class_distribution.items(), key=lambda x: x[1])
                                st.markdown(f"""
                                    <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%); border-radius: 12px; border-left: 4px solid #A86B43;">
                                        <h3 style="margin: 0; color: #3B2A1A;">Kualitas Dominan</h3>
                                        <h2 style="margin: 0.5rem 0; color: #3B2A1A;">{majority_class[0]}</h2>
                                        <p style="color: #8B5E3C; margin: 0;">{majority_class[1]} biji ({(majority_class[1]/total_beans)*100:.1f}%)</p>
                                    </div>
                                """, unsafe_allow_html=True)
                        
                        st.markdown("")
                        # Preview gambar diperkecil
                        if results['detection_image'] is not None:
                            col1, col2, col3 = st.columns([1, 3, 1])
                            with col2:
                                st.image(results['detection_image'], caption=f"Deteksi {total_beans} biji kopi", use_container_width=True)
                        
                        st.markdown("<h6 style='text-align: center; font-size: 2rem; margin-top: 20px'>📊 Ringkasan Kualitas</h6>", unsafe_allow_html=True)
                        
                        # Container dengan margin dikurangi
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            bagus_count = class_distribution.get('Bagus', 0)
                            bagus_pct = (bagus_count / total_beans * 100) if total_beans > 0 else 0
                            st.markdown(f"""
                                <div class="quality-summary-box" style=" text-align: center; background: #E8F8F5; border-color: #27AE60;">
                                    <h2 style="color: #27AE60;">🟢 Bagus</h2>
                                    <h1 style="color: #27AE60;">{bagus_count}</h1>
                                    <p style="color: #27AE60; font-weight: 600;">{bagus_pct:.1f}%</p>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            rusak_count = class_distribution.get('Rusak', 0)
                            rusak_pct = (rusak_count / total_beans * 100) if total_beans > 0 else 0
                            st.markdown(f"""
                                <div class="quality-summary-box"  style=" text-align: center; background: #FADBD8; border-color: #E74C3C;">
                                    <h2 style="color: #E74C3C;">🔴 Rusak</h2>
                                    <h1 style="color: #E74C3C;">{rusak_count}</h1>
                                    <p style="color: #E74C3C; font-weight: 600;">{rusak_pct:.1f}%</p>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        with col3:
                            jamur_count = class_distribution.get('Jamur', 0)
                            jamur_pct = (jamur_count / total_beans * 100) if total_beans > 0 else 0
                            st.markdown(f"""
                                <div class="quality-summary-box" style=" text-align: center; background: #FEF5E7; border-color: #F39C12;">
                                    <h2 style="color: #F39C12;">🟠 Jamur</h2>
                                    <h1 style="color: #F39C12;">{jamur_count}</h1>
                                    <p style="color: #F39C12; font-weight: 600;">{jamur_pct:.1f}%</p>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        # Status keseluruhan
                        if 'Bagus' in class_distribution:
                            good_percentage = (class_distribution['Bagus'] / total_beans) * 100
                            if good_percentage >= 80:
                                st.success(f"✅ Kualitas keseluruhan BAIK ({good_percentage:.1f}% biji bagus)")
                            elif good_percentage >= 60:
                                st.warning(f"⚠️ Kualitas keseluruhan SEDANG ({good_percentage:.1f}% biji bagus)")
                            else:
                                st.error(f"❌ Kualitas keseluruhan BURUK ({good_percentage:.1f}% biji bagus)")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                else:
                    st.error("❌ Gagal menganalisis gambar. Pastikan gambar mengandung biji kopi yang jelas.")
                    
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

# Container untuk tombol
st.markdown('<div class="nav-buttons-container">', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;font-size: 1.2rem">Klik button di bawah ini untuk melanjutkan ke halaman Tentang Sistem / kembali ke Beranda.</p>', unsafe_allow_html=True)

# TOMBOL DI TENGAH - menggunakan 3 kolom dengan kolom tengah lebih besar
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        if st.button("🏠 Kembali ke Beranda", type="primary", use_container_width=True, key="nav_home_btn"):
            st.session_state.current_page = 'dashboard'
            st.switch_page("app.py")

    with col_btn2:
        if st.button(" ℹ️ Tentang Sistem", type="primary", use_container_width=True, key="nav_about_btn"):
            st.session_state.current_page = 'tentang'
            st.switch_page("pages/tentang.py")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer dengan tips
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #8B7355; padding: 30px; background: linear-gradient(135deg, #f5f0e8 0%, #e8dcc8 100%); border-radius: 20px; margin-top: 40px;'>
        <p style='font-size: 16px; font-weight: 600; margin-bottom: 10px;'>© 2024 BeanClassify - Sistem Klasifikasi Kualitas Biji Kopi</p>
        <p style='font-size: 14px;'>Dibuat dengan ❤️ menggunakan Python dan Machine Learning</p>
    </div>
""", unsafe_allow_html=True)