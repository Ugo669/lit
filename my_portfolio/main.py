import streamlit as st 
from PIL import Image
import os



st.set_page_config(page_title="ugochi stanley", page_icon="toda", layout="wide")
theme = st.sidebar.selectbox("select  theme", [
    'light', 'dark', 'system',  'blue'
])
 
st.title("theophilus  ugochukwu sylvanus")
st.subheader("Data Scientist | machine learning engineer | Network  Engineer | web developer | Cyber  security  enthusiast | ")
st.write("###")
profile = Image.open(os.path.join(r'C:\project\lit\my_portfolio\2.jpg'))
st.image(profile, width=200)
column1, column2, column3 = st.columns(3, gap="large")
column1.write("#####")
column1.header("About me")
column1.write("#")
column1.write(" I am a data scientist and a machine learning engineer with strong background in network engineering and web development. I have a passion for leveraging data  to drive insights, solve complex problems,  and create innovative solutions. with a understand of statistics and programming.")

column2.write("#####")

column2.header("Skills")
def skills_progress():
    skills_progress = {
        "python": 90,
        "Rust": 60,
        "C++": 40,
        "SQL": 70,
        "HTML/CSS":80,
        "Javascript": 30,
          "Machine learning": 70,
          "Data analysis":80,
          }
    return skills_progress

for skill, progress in skills_progress().items():
    column2.write(f"{skill}")
    column2.progress(progress)

column3.write("#####")
column3.header("Projects")
column3.write("1. Automated Decision Making")

st.write("####")

st.header("contact")
st.write("phone: 0901 524 3199")
st.write("Email: theoboy669@gmail.com")
st.write("github: www.github.com/Ugo669")