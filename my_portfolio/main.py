import streamlit as st 
from PIL import Image

mage = "https://media.istockphoto.com/id/2217582550/photo/blank-magazine-cover-mockup-array.webp?a=1&b=1&s=612x612&w=0&k=20&c=CxlJhDdyzaZaOPjZK1U81fKmyRm9ua6KQF9h0vjmxTU="
page_elements= f'''
<style>
[data-testid="stAppViewcontainer"]{{
    background-image: url({mage});
    background-size: cover;
}}

</style>
'''
st.markdown(page_elements, unsafe_allow_html=True)


#st.set_page_config(page_title="ugochi stanley", page_icon=":toda", layout="wide")

 
st.title("theophilus  ugochukwu sylvanus")
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("images/2.jpg", width=200)
st.subheader("Data Scientist | machine learning engineer | Network  Engineer | web developer | Cyber  security  enthusiast | ")
st.write("###")



col1, col2, col3= st.columns(3, gap ="large")
def projects(col1):
    col1.header("-Some Awesome Works-")
    st.write("###")
    #col1.image()
    col1.subheader("Autormated Decission Making machine")
    col1.write(" a responsive machine that could help make decission" \
    "by recomending music, outfits, videos and even what to eat")
    lnk1 = "https://github.com/Ugo669/Automated-DM.git"
    w = col1.link_button("view project", lnk1)
    col1.write("###")
    #col1.image()
    col1.subheader("The scrapper")
    col1.write("An interactive python command line web scrapping tool that aids in advance web scrapping")
    viw =""
    col1.button("view project", viw)
    st.write("###")
    #col1.image
    col1.subheader("Aladin")
    col1.write("a scalable e-commerse website built with django framework")
    url = "www.github.com/ugo669/alladin"
    st = col1.button("view project", url)
    
    st.write("###")

    col1.subheader("mfinance")
    col1.write(" is a web finance solution that help :")
    col1.write("* calculate income, expenses and gives you a total of both " )
    col1.write("* the ability to compare between present and past month expenses")
    col1.write("* gives tips on how to improve your income and money flow")
    url2 = "www.github.com/ugo669/mfinance"
    de= col1.button("view project",url2)




    

projects(col1)

st.write("###")


col2.header("-who i work with-")
col2.write("I am open to work with founders, startups, small and medium enterprises."\
"I am also open to work with individuals who are looking to build solutions to their problems")

def about():
    col3.header("About Me")
    col3.write("I am theophilus ugochukwu sylvanus a developer whom is passion driven" \
    "with over 5 years of eperience in the development space. Building scalable and user friendly software that solves real life problems in business enterprisses, " \
    "health institutions and in the tech field  " \
    "" \
    " ")
about()
st.button("HIRE ME", url="https://wa.me/09015243199")




st.write("####")

st.header("contact")
st.write("phone: 0901 524 3199")
st.write("Email: theoboy669@gmail.com")
st.write("Linkedin: wwww.linkedin.com/in/theophilus-ugochukwu-sylvanus-6999a4248")

