import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
astronaute_lire = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_bqmgf5tx.json")

def main() : 
    st.title("article summarizer")
    st.write('##')
    
    st.subheader("Why this project")
    with st.container() :
        left_column, right_column = st.columns(2)
        with left_column :
            st.write("##")
            st.write(
                """
                Sometimes when you look for informations on press or wikipedia you are looking for clear and concise informations, a summary like.
                But instead you find a VERY long article or wikipedia page and you have to read it completely and cope with details you don't want.
                So we had the idea to summarize articles from some newspaper websites and from wikipedia using NLP algorithm.
                
                """)
        with right_column :
            st_lottie(astronaute_lire, height=250)

    st.write("##")
    st.subheader("Limits") 
    st.write("This application only works for wikipedia and for a selection of newspaper websites (only free contents) : lemonde.fr, lefigaro.fr, leparisien.fr, lesechos.fr, liberation.fr, lequipe.fr, bbc.com. If you try with other websites or for not free article the model will ne work and will give you nothing.")

if __name__ == '__main__' :
    main()

