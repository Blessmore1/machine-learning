#%%writefile user.py
import streamlit as st
import tempfile
from Base_app import *
from Model import *
#from Video import *
import time
'''
def filter_frame(txt_search):
    files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))
    indices = [i for i, s in enumerate(files) if txt_search.lower() in s]
    return files[indices[0]]
'''
'''
files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
fi = [i.split()[0] for i in files] 
detected_obj = list(set(fi))
'''
detected_obj = ['1 quill','2 boathouse','3 torch','4 bow_tie','5 beaker','6 vault','7 bookshop','8 dough','9 Windsor_tie','10 restaurant','11 palace','12 cocktail_shaker,'13 library',
'14 monitor','15 water_jug','16 eel','17 suit','18 pier','19 jean','20 barbershop','21 lakeside','22 monastery','23 West_Highland_white_terrier','24 web_site','25 eggnog',
'26 saltshaker','27 hand-held_computer','28 beer_glass','29 fountain','30 balance_beam','31 candle','32 stage','33 groom','34 plane','35 potters_wheel',
'36 coffee_mug','37 valley','38 cellular_telephone','39 steel_arch_bridge']

with st.sidebar:
    with st.spinner("Loading..."):
        time.sleep(3)
    st.success("WELCOME TO  OUR OBJECT PRIDICTION APP")
    st.success("DONE BY BLESSMORE MAJONGWE")
    st.success("SAMATHA JOWA")
def app():

    global rez

    rez = "..."


    f = st.file_uploader("Upload video")

    s1, s2, s3 = st.columns([1,4,2])
    with s1:
        st.text_area("text area for the user")

    with s2:
    
        search = st.text_input("Search for objects in video")
        if search in detected_obj:
            rez = "Found"
        else:
            rez = "Not Found"
        
    with s3:
        st.write('Search results')
        if f is None:
            status = st.write(f'{search} ...')
        else:
            status = st.write(f'{search} {rez}')


    with st.container():

        col1, col2 = st.columns([2,6])

        with col1:
            st.write("Objects in video")
            for i in range(len(detected_obj)):
                st.write(str(i+1) +  " "+str(detected_obj[i]))
        with col2:

            if f is not None:
                tfile = tempfile.NamedTemporaryFile(delete=False)
                tfile.write(f.read())

                with st.spinner('[*Extracting Frames] - Process Initialized...'):
                    extract_frames(tfile.name, "./images")
                st.success('[*Extracting Frames] - Process Completed...')

                with st.spinner('[**Encoding Frames] - Process Initialized...'):
                    label_frames(inputpath="./images", outputpath='./encoded_images/', videoFile=r"./sample_vid/this1.mp4")
                st.success('[*Encoding Frames] - Process Completed...')

                with st.spinner('[***Building Frames] - Process Initialized...'):
                    build_video(inputpath='./encoded_images/', outputpath='./videos/video.mp4',fps=5)
                st.success('[*Building Frames] - Process Completed...')

                if search.lower() in detected_obj:
                    rez = "found"
                    img = Image.open('./encoded_images/'+str(filter_frame(search)))
                    st.image(img, caption=search.lower() + " frame found")
                else:
                    play_video('./videos/video.mp4')

