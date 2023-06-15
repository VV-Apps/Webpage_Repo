#import requests
#import streamlit as st
#from PIL import Image
#import streamlit.components.v1 as components
#st.set_page_config(page_title="Vignesh", page_icon=":wave:", layout="wide")

#lottie_url = "https://assets4.lottiefiles.com/packages/lf20_au98facn.json"
import requests
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
st.set_page_config(page_title="Vignesh", page_icon=":wave:", layout="wide")

# Set the background image
background_image = "https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.png"

# Set the link bar
link_bar = "[Home](https://example.com/home) [About](https://example.com/about) [Contact](https://example.com/contact)"

# Inject custom CSS to remove space at the top and adjust image size
st.markdown(
    """
    <style>
    .stApp {
        margin-top: 0;
    }
    .background-image {
        background-image: url('"""+background_image+"""');
        background-repeat: no-repeat;
        background-position: center top;
        background-size: cover;
        height: 10px;
        width: 50%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the link bar
st.markdown(link_bar)


st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.png", use_column_width=True)
st.sidebar.title("Vignesh_Webpage")

tabs1 = st.sidebar.button("About Me")
tabs2 = st.sidebar.button("Resume")
tabs3 = st.sidebar.button("Contact Me")

with st.container():
    if tabs1:
        st.empty().title("About Me")
        st.empty().subheader("Vision")
        st.empty().write("Man with a plan")
        about_me_button = st.empty().button("Back to Main Page")
        if about_me_button:
            st.experimental_set_query_params()
    else:
        st.empty().empty()
with st.container():
    if tabs2:
        st.empty().title("Resume")
        st.empty().subheader("Education")
        st.empty().write("Educational details go here.")
        resume_button = st.empty().button("Back to Main Page")
        if resume_button:
            st.experimental_set_query_params()
    else:
        st.empty().empty()
with st.container():
    if tabs3:
        st.empty().title("Contact Me")
        contact_button = st.empty().button("Back to Main Page")
        if contact_button:
            st.experimental_set_query_params()
    else:
        st.empty().empty()


with st.container():
    if not any([tabs1, tabs2, tabs3]):
        st.title(":grinning: Vignesh")
        st.sidebar.markdown("---")
        st.subheader("A student in Singapore")
        st.write("[Find out more about me 👈](https://tarannator.blogspot.com/)")
        
        with st.container():
                st.write("""
                        I am a high school student who:
                        - is on the lookout for internships and collaborations in the Science industries to boost my portfolio.
                        - has recently found the use of Python for web-app designing intuitive and very interesting.
                        - wants to learn and apply my knowledge for the betterment of mankind .
                        - is a hard worker and have made good use of my 6 years in high school to participate in activities from DSO to A STAR Agency."

                        While for now this webpage is merely a trial run, I hope to expand this in the future to connect with other science enthusiasts.

                        """)

                left_column, right_column = st.columns(2)
                with left_column:
                    st.header("My Works")
                    st.write("""
                    IN THE OVEN
                    """)
                with right_column:
                    gif_url = "https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.gif"
                    st.image(gif_url, use_column_width=True)
                st.write("[My YouTube Channel 👈](https://youtube.com)")
                
#import base64
#def add_bg_from_local(image_file):
#    with open(image_file, "rb") as image_file:
#        encoded_string = base64.b64encode(image_file.read())
#    st.markdown(
#    f"""
#    <style>
#    .stApp {{
#        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#        background-size: cover
#    }}
#    </style>
#    """,
#    unsafe_allow_html=True
#    )
#add_bg_from_local('Dark Planet.jpg')    
