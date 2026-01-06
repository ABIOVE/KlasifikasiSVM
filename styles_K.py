"""
STYLE KHUSUS UNTUK HALAMAN KLASIFIKASI
"""

KLASIFIKASI_STYLES = """
<style>
    /* Container utama upload */
    .upload-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #FDF8F2 100%);
        border: 2px dashed #C69C72;
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        margin: 2rem auto;
        max-width: 600px;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 8px 24px rgba(139, 94, 60, 0.1);
    }
    
    .upload-container:hover {
        border-color: #8B5E3C;
        background: linear-gradient(135deg, #FFFFFF 0%, #FEFCF9 100%);
        transform: translateY(-2px);
        box-shadow: 0 12px 32px rgba(139, 94, 60, 0.15);
    }
    
    .upload-container.dragover {
        border-color: #8B5E3C;
        background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%);
        transform: scale(1.02);
    }
    
    /* Ikon kamera */
    .upload-icon {
        font-size: 4rem;
        color: #8B5E3C;
        margin-bottom: 1rem;
        display: block;
    }
    
    /* Teks utama upload */
    .upload-text-main {
        font-size: 1.4rem;
        font-weight: 600;
        color: #3B2A1A;
        margin-bottom: 0.5rem;
    }
    
    /* Teks sekunder upload */
    .upload-text-secondary {
        font-size: 1rem;
        color: #8B5E3C;
        margin-bottom: 1rem;
        opacity: 0.8;
    }
    
    /* Info format file */
    .file-info {
        font-size: 0.85rem;
        color: #A86B43;
        margin-top: 1rem;
        opacity: 0.7;
    }
    
    /* Header utama dengan dua baris */
    .main-header-container {
        text-align: center;
        margin-bottom: 2rem;
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
    
    /* Container untuk tombol aksi */
    .action-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        margin: 2rem auto;
        max-width: 400px;
        padding: 0 1rem;
    }
    
    /* Container tombol navigasi */
    .nav-buttons-container {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
        margin: 1.5rem auto;
        max-width: 300px;
        width: 100%;
    }
    
    /* Teks penjelas */
    .explanation-text {
        text-align: center;
        color: #8B5E3C;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        opacity: 0.8;
    }
    
    /* Status indikator */
    .status-good { 
        color: #27AE60; 
        font-weight: 600; 
    }
    
    .status-fair { 
        color: #F39C12; 
        font-weight: 600; 
    }
    
    .status-poor { 
        color: #E74C3C; 
        font-weight: 600; 
    }
    
    /* Sembunyikan file uploader default */
    .uploadedFile { 
        display: none; 
    }
    
    .stFileUploader { 
        display: none; 
    }
    
    /* Info file yang diupload */
    .file-info-display {
        background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem auto;
        max-width: 600px;
        text-align: center;
        border-left: 4px solid #A86B43;
        box-shadow: 0 4px 12px rgba(139, 94, 60, 0.1);
    }
    
    /* Styling untuk area hasil */
    .result-section {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem auto;
        box-shadow: 0 4px 16px rgba(139, 94, 60, 0.08);
        border: 1px solid #F7E2C5;
    }
    
    /* Kartu hasil prediksi */
    .prediction-card {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%);
        border-radius: 12px;
        border-left: 4px solid #A86B43;
        margin: 1rem 0;
    }
    
    /* Progress bar custom */
    .stProgress > div > div > div > div {
        background-color: #A86B43;
    }
    
    /* Container untuk gambar hasil */
    .image-result-container {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(139, 94, 60, 0.1);
        border: 1px solid #F7E2C5;
    }
    
    /* Tips box */
    .tips-box {
        background: linear-gradient(135deg, #FDF8F2 0%, #F9E8D2 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem auto;
        max-width: 800px;
        border-left: 4px solid #A86B43;
    }
</style>
"""

# JavaScript untuk drag and drop
DRAG_DROP_JS = """
<script>
function setupDragDrop() {
    const uploadContainer = document.querySelector('.upload-container');
    const fileInput = document.getElementById('file-upload');
    
    if (!uploadContainer || !fileInput) return;
    
    // Prevent default drag behaviors
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadContainer.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });
    
    // Highlight drop area when item is dragged over it
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadContainer.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        uploadContainer.addEventListener(eventName, unhighlight, false);
    });
    
    // Handle dropped files
    uploadContainer.addEventListener('drop', handleDrop, false);
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    function highlight() {
        uploadContainer.classList.add('dragover');
    }
    
    function unhighlight() {
        uploadContainer.classList.remove('dragover');
    }
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length) {
            fileInput.files = files;
            // Trigger change event
            const event = new Event('change', { bubbles: true });
            fileInput.dispatchEvent(event);
        }
    }
}

// Setup when page loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupDragDrop);
} else {
    setupDragDrop();
}
</script>
"""