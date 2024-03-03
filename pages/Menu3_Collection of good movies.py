import streamlit as st

def tab_content(tab):
    if tab == "Romace":
        st.image("image/PMG/Romace/Romace02.png")
        video_path = 'pages/VDO/POOR THINGS _ Official Trailer _ Searchlight Pictures.mp4'
        st.video(video_path) 
        st.image("image/PMG/Romace/Romace01.png")
        video_path = 'pages/VDO/One Day _ Official Trailer _ Netflix.mp4'
        st.video(video_path)
    elif tab == "Horror":
        st.image("image/PMG/Horror/Horror1.png")
        video_path = 'pages/VDO/The Walking Dead_ Daryl Dixon Official Trailer.mp4'
        st.video(video_path)

    elif tab == "Action":
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
         
def main():
    page_bg_img = '''<style>
    .stApp {
        background-image: url("https://wallpapercave.com/wp/wp3428333.jpg");
        background-size: cover;
    }
    </style>'''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("<h1 style='color: white;'>------------------------------------------------</h1>", unsafe_allow_html=True)

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

    tab_selected = st.radio("เลือกประเภทหนังที่ชอบ", ["Romace", "Horror", "Action"])
    tab_content(tab_selected)

if __name__ == "__main__":
    main()
