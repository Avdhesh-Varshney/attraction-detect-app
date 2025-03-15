from module.attractiveness_detection import FaceAttractivenessApp
import streamlit as st
import gdown
import os

st.set_page_config(
    page_title="Face Attractiveness Detection",
    page_icon="assets/logo.jpg"
)

@st.cache_resource
def download_weights():
    file_path = st.secrets['FILE_NAME']
    if not os.path.exists(file_path):
        with st.spinner("🔄 Downloading model weights..."):
            gdown.download(f"https://drive.google.com/uc?id={st.secrets['MODEL_ID']}", file_path, quiet=False)

def load_app():
    download_weights()
    return FaceAttractivenessApp(st.secrets['FILE_NAME'])

app = load_app()

st.markdown(
    """
    <style>
        .description { font-size: 1rem; text-align: center; color: #666; }
        .footer { font-size: 14px; text-align: center; margin-top: 20px; color: #888; }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header('🌟 Face Attractiveness Detection')
st.sidebar.image("assets/logo.jpg")
st.sidebar.markdown('<p class="description">Analyze facial features and predict attractiveness scores using AI.</p>', unsafe_allow_html=True)

with st.sidebar.expander("📌 How to Use"):
    st.markdown(
        """
        **📷 Image Mode**
        - Upload a **JPEG/PNG** file to analyze.

        **🎥 Video Mode**
        - Upload an **MP4/MKV/AVI** file for batch processing.
        
        **📡 Camera Mode**
        - Activate your webcam for live detection.
        """,
        unsafe_allow_html=True
    )

st.sidebar.markdown('<p class="footer">Developed with ❤️ by Avdhesh Varshney | © 2025</p>', unsafe_allow_html=True)

st.title("🎯 Choose Detection Mode")
option = st.radio(
    "", 
    ['Image', 'Video', 'Camera'], 
    horizontal=True, 
    format_func=lambda x: '📷 Image' if x == 'Image' else '🎥 Video' if x == 'Video' else '📸 Camera'
)

def process_file(option):
    if option == 'Image':
        image = st.file_uploader("📸 Upload an image:", type=['jpg', 'jpeg', 'png'])
        if image:
            with st.spinner("🔄 Processing Image..."):
                app.process_image(image)
            st.success("✨ Image processing completed!")
    elif option == 'Video':
        video = st.file_uploader("🎥 Upload a video:", type=['mp4', 'mkv', 'avi'])
        if video:
            with st.spinner("🔄 Processing Video..."):
                app.process_video(video)
            st.success("✅ Video processing completed!")
    elif option == 'Camera':
        st.toast("**Live Camera Mode**: Activating...", icon="🟢")
        app.process_camera()

process_file(option)
