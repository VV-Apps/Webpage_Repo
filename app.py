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


st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.png", use_column_width=True)
st.sidebar.title("Vignesh_Webpage")
iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6Kg8KoSEacO0Y21pL0ZcDj?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
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
        # Inject custom CSS to style the links
        st.markdown(
            """
            <style>
            /* Styling for the links */
            .styled-link {
                display: inline-block;
                padding: 7px 16px;
                background-color: #f2e9e4;
                color: black !important;
                text-decoration: none;
                font-weight: bold;
                border-radius: 10px;
                transition: background-color 0.4s ease;
            }

            .styled-link:hover {
                background-color: #c9ada7;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display the styled links
        st.markdown(
            """
            <a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiIiN6go8X_AhX4yDgGHaybDlcQwqsBegQIDxAG&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&usg=AOvVaw0aHtehaphMhOCAkCydRLZU" class="styled-link">Home</a>
            <a href="https://example.com/about" class="styled-link">About</a>
            <a href="https://example.com/contact" class="styled-link">What Do We Do</a>
            """,
            unsafe_allow_html=True
        )
        
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
