import streamlit as st
from pathlib import Path

page_bg_img = '''<style>
.stApp {
    background-image: url("https://wallpapercave.com/wp/wp3428333.jpg");
    background-size: cover;
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)

def main_Profile():
    st.markdown("<h1 style='color: white;'>Profile</h1>", unsafe_allow_html=True)
    st.image('image/PMG/3.png')

def main_Profile2():
    st.markdown("<h1 style='color: white;'>Profile</h1>", unsafe_allow_html=True)
    st.image('image/PMG/Profile2.png')

menu = ["Profile1", "Profile2"]
menu_selection = st.sidebar.radio("Main menu", menu)

if menu_selection == "Profile1":
    main_Profile()
    tab1, tab2 = st.columns(2)
    with tab1:
        st.markdown("<h1 style='color: white;'>Action</h1>", unsafe_allow_html=True)
        st.image("image/PMG/1248930.jpg", width=200)

elif menu_selection == "Profile2":
   main_Profile2()
   tab1, tab2 = st.columns(2)
   with tab1:
        st.markdown("<h1 style='color: white;'>Horror</h1>", unsafe_allow_html=True)
        st.image("image/PMG/1248934.jpg", width=200)
