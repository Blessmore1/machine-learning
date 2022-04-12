#%%writefile home.py
import streamlit as st
from Base_app import *
import time
'''
files = [f for f in os.listdir("images ") if os.path.isfile(os.path.join("images ", f))]
fi = [i.split()[0] for i in files] 
detected_obj = list(set(fi))
'''
'''
detected_obj = ['1 quill','2 boathouse','3 torch','4 bow_tie','5 beaker','6 vault','7 bookshop','8 dough','9 Windsor_tie','10 restaurant','11 palace','12 cocktail_shaker','13 library',
'14 monitor','15 water_jug','16 eel','17 suit','18 pier','19 jean','20 barbershop','21 lakeside','22 monastery','23 West_Highland_white_terrier','24 web_site','25 eggnog',
'26 saltshaker','27 hand-held_computer','28 beer_glass','29 fountain','30 balance_beam','31 candle','32 stage','33 groom','34 plane','35 potters_wheel',
'36 coffee_mug','37 valley','38 cellular_telephone','39 steel_arch_bridge']
detected_obj=[]
'''
'''
def filter_frame(txt_search):
    files = [f for f in os.listdir("images ") if os.path.isfile(os.path.join("images  ", f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))
    indices = [i for i, s in enumerate(files) if txt_search.lower() in s]
    return files[indices[0]]
'''
def app():
    global h_rez

    h_rez = "..."

    st.title('Object Detection Model using InceptionV3')

    st.write('Blessmore Majongwe')
    st.write('Samatha Jowa')

    hs1, hs2, hs3 = st.columns([1,4,2])
    with st.sidebar:
        with st.spinner("Loading..."):
            time.sleep(3)
            st.success("WELCOME TO  OUR OBJECT PRIDICTION APP")
            st.success("DONE BY BLESSMORE MAJONGWE")
            st.success("SAMATHA JOWA")
    
    
    with hs2:
        h_search = st.text_input("Search for objects in video")
        if h_search.lower() in detected_obj:
            h_rez = "found"
        else:
            h_rez = "not found--error"
        
    with hs3:
        st.write('Search results')
        if h_search.lower() is None:
            status = st.write(f'{h_search} ...')
        else:
            status = st.write(f'{h_search} {h_rez}')


    if len(detected_obj) > 6:
        col1, col2, col3 = st.columns([2,2,6])
        with col1:
            st.subheader("List of objects in  a video")
            for i in range(0,7):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            for i in range(7,len(detected_obj)-1):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col3:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            if h_search.lower() in detected_obj:
                h_rez = "found"
                img = Image.open('mages'+str(filter_frame(h_search)))
                st.image(img, caption=h_search.lower() + " frame found")
            else:
                play_video("video.mp4")
    else:
        col1, col2 = st.columns([2,6])
        with col1:  
            st.write("Objects in video")
            for i in range(len(detected_obj)):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col2:
            play_video("video.mp4")
