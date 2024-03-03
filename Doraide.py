import streamlit as st
import base64

def main_content():
    st.header('Erroneous')
    st.image('image/8.png') 

def main_Doraide():
    st.markdown("<h1 style='color: white;'>Doraide</h1>", unsafe_allow_html=True)
    st.image('image/PMG/1.png', width=800)

def main_ChangeBG():
    st.markdown("<h1 style='color: white;'>Change background picture</h1>", unsafe_allow_html=True)
    st.image('image/PMG/11.png') 

page_bg_img = '''<style>
.stApp {
    background-image: url("https://wallpapercave.com/wp/wp3428333.jpg");
    background-size: cover;
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
 
def bg_image_upload():
    bg_image = st.file_uploader("Upload background image", type=["jpg", "jpeg", "png"])

    if bg_image is not None:
        bg_image_bytes = bg_image.read()
        bg_image_base64 = base64.b64encode(bg_image_bytes).decode()
        page_bg_img = f'''
        <style>
        .stApp {{
        background-image: url("data:image/png;base64,{bg_image_base64}");
        background-size: cover;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

menu = ["Doreide", "Change background picture"]
menu_selection = st.sidebar.radio("Main menu", menu)

if menu_selection == "Doreide":
    main_Doraide()

elif menu_selection == "Change background picture":
    main_ChangeBG()
    bg_image_upload()
    
tab1, tab2, tab3 = st.columns(3)

with tab1:
 st.markdown("<h1 style='color: white;'>Romace</h1>", unsafe_allow_html=True)
 st.image("image/PMG/1248927.jpg", width=200)

with tab2:
 st.markdown("<h1 style='color: white;'>Horror</h1>", unsafe_allow_html=True)
 st.image("image/PMG/1248934.jpg", width=200)

with tab3:
 st.markdown("<h1 style='color: white;'>Action</h1>", unsafe_allow_html=True)
 st.image("image/PMG/1248930.jpg", width=200)