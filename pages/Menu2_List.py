import streamlit as st

def main_01():
    st.markdown("<h1 style='color: white;'>แนะนำ</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>Game of Thrones</h1>", unsafe_allow_html=True)
    st.image('image/PMG/5.png')
    st.markdown("<h1 style='color: white;'>Movie Trailer</h1>", unsafe_allow_html=True)
    video_path = 'pages/VDO/House of the Dragon Season 2 _ Official Teaser _ Max.mp4'
    st.video(video_path)
    st.markdown("<h1 style='color: white;'>------------------------------------------------</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>Halo The Series<", unsafe_allow_html=True)
    st.image('image/PMG/Action/Action02.png')
    video_path = 'pages/VDO/Halo The Series (2022) _ Official Trailer _ Paramount+.mp4'
    st.video(video_path)
    st.markdown("<h1 style='color: white;'>------------------------------------------------</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>Pacific Rim<", unsafe_allow_html=True)
    st.image('image/PMG/Action/Action04.png')
    video_path = 'pages/VDO/Pacific Rim - Official Main Trailer [HD].mp4'
    st.video(video_path)

def main_02():
    st.header('ประเภทหนัง')
    st.image('image/PMG/6.png')

    if st.button("โรแมนติก"):
        st.header("โรแมนติก")
        st.image("image/PMG/Romace/Romace01.png")
        video_path = 'pages/VDO/One Day _ Official Trailer _ Netflix.mp4'
        st.video(video_path)
        

    if st.button("สยองขวัญ"):
        st.header("สยองขวัญ")
        st.image("image/PMG/Horror/Horror1.png")
        video_path = 'pages/VDO/The Walking Dead_ Daryl Dixon Official Trailer.mp4'
        st.video(video_path)

    if st.button("หนังแอ็คชั่น"):
        st.image("image/PMG/Action/Action02.png")
        video_path = 'pages/VDO/Halo The Series (2022) _ Official Trailer _ Paramount+.mp4'
        st.video(video_path)
        st.image("image/PMG/Action/Action04.png")
        video_path = 'pages/VDO/Pacific Rim - Official Main Trailer [HD].mp4'
        st.video(video_path)
        st.image("image/PMG/Action/Action01.png")
        video_path = 'pages/VDO/Hacksaw Ridge (2016) Official Trailer – “Believe” - Andrew Garfield.mp4'
        st.video(video_path)
        st.image("image/PMG/Action/Action03.png")
        video_path = 'pages/VDO/Kung Fu Panda 4 _ กังฟูแพนด้า 4 - Official Trailer [พากย์ไทย].mp4'
         

page_bg_img = '''<style>
.stApp {
    background-image: url("https://wallpapercave.com/wp/wp3428333.jpg");
    background-size: cover;
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)

menu = ["แนะนำ", "ประเภทหนัง"]
menu_selection = st.sidebar.radio("Main menu", menu)

if menu_selection == "แนะนำ":
    main_01()  

elif menu_selection == "ประเภทหนัง":
    main_02()
