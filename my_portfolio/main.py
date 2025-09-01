import streamlit as st 
from PIL import Image



st.set_page_config(page_title="ugochi stanley", page_icon="toda", layout="wide")
theme = st.sidebar.selectbox("select  theme", [
    'light', 'dark', 'system',  'blue'
])
 
st.title("theophilus  ugochukwu sylvanus")
st.subheader("Data Scientist | machine learning engineer | Network  Engineer | web developer | Cyber  security  enthusiast | ")
st.write("###")
st.image(Image.open("2.jpg"), width=200)
column1, column2, column3 = st.columns(3, gap="large")
column1.write("#####")
column1.header("About me")
column1.write("#")
column1.write(" I am a data scientist and a machine learning engineer with strong background in network engineering and web development. I have a passion for leveraging data  to drive insights, solve complex problems,  and create innovative solutions. with a understand of statistics and programming.")

column2.write("#####")
column2.header("Skills")
column2.write("python")
column2.write("Rust")
column2.write("C++")
column2.write("javascript")

column3.write("#####")
column3.header("Projects")

st.write("####")
st.header("contact")
st.write("phone: 0901 524 3199")
st.write("Email: theoboy669@gmail.com")
st.write("github: www.github.com/Ugo669")