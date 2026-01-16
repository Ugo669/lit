import streamlit as st 
from PIL import Image
import os



st.set_page_config(page_title="ugochi stanley", page_icon=":toda", layout="wide")

 
st.title("theophilus  ugochukwu sylvanus")
st.subheader("Data Scientist | machine learning engineer | Network  Engineer | web developer | Cyber  security  enthusiast | ")
st.write("###")



col1, col2, col3= st.columns(3, gap ="large")
def projects():
    col1.header("-Some Awesome Works-")
    #col1.image()
    col1.subheader("Autormated Decission Making machine")
    col1.write(" a responsive machine that could help make decission" \
    "by recomending music, outfits, videos and even what to eat")
    col1.button("view project")
    st.write("###")
    #col1.image()
    col1.header("The scrapper")
    col1.write("A command line web scrapping tool")
    col1.button("view project")

    st.write("###")

    #col1.image
    col1.header("Aladin")
    col1.write("a scalable e-commerse website")
    col1.button("view project")


projects()

st.write("###")


col2.header("-who i work with-")

def about():
    col3.header("About Me")
    col3.write("I am theophilus ugochukwu sylvanus a developer whom is passion driven" \
    "with over 5 years of eperience in the development space. Building scalable and user friendly software that solves real life problems in business enterprisses, " \
    "health wise and in the tech field  " \
    "" \
    " ")
about()





st.write("####")

st.header("contact")
st.write("phone: 0901 524 3199")
st.write("Email: theoboy669@gmail.com")
st.write("github: www.github.com/Ugo669")