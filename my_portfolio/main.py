import streamlit as st 
from PIL import Image
import os



st.set_page_config(page_title="ugochi stanley", page_icon="toda", layout="wide")

 
st.title("theophilus  ugochukwu sylvanus")
st.subheader("Data Scientist | machine learning engineer | Network  Engineer | web developer | Cyber  security  enthusiast | ")
st.write("###")
profile = Image.open(os.path.join("images", "2.jpg"), )
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
        "python 90%": 90,
        "Rust 60%": 60,
        "C++ 40%": 40,
        "SQL 70%": 70,
        "HTML/CSS 80%":80,
        "Javascript 30%": 30,
          "Machine learning 70%": 70,
          "Data analysis 80%":80,
          }
    return skills_progress

for skill, progress in skills_progress().items():
    column2.write(f"{skill}")
    column2.progress(progress)

column3.write("#####")
column3.header("Projects")
column3.link_button("1. Automated Decision Making","www.github.com/ugo669/Automated-DM")
column3.write("this project with simple decision making. Such as which music to  listen to, what movie to watch, what's the matching out to wear. All according to what mood you are in. ")

st.write("####")

st.header("contact")
st.write("phone: 0901 524 3199")
st.write("Email: theoboy669@gmail.com")
st.write("github: www.github.com/Ugo669")