import streamlit as st

st.set_page_config(page_title="VV", page_icon=":wave:", layout="wide")

st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.png", use_column_width=True)
st.sidebar.title("VV_Webpage")

tabs1 = st.sidebar.button("About Me")
tabs2 = st.sidebar.button("Resume")
tabs3 = st.sidebar.button("Contact Me")


about_me_placeholder = st.empty()
resume_placeholder = st.empty()
contact_placeholder = st.empty()

with st.container():
    if tabs1:
        st.empty(title("About Me"))
        about_me_placeholder.subheader("Vision")
        about_me_placeholder.write("Founded by a group of zealous youths with a passion for music, Project Gift of Song aims to bridge the gap between music and terminal illnesses. We wish to bring joy and comfort to all stages of life through the spread of music.")
        about_me_button = about_us_placeholder.button("Back to Main Page")
        if about_me_button:
            st.experimental_set_query_params()
    else:
        about_me_placeholder.empty()
with st.container():
    if tabs2:
        resume_placeholder.title("Resume")
        resume_placeholder.subheader("Education")
        resume_placeholder.write("Educational details go here.")
        resume_button = resume_placeholder.button("Back to Main Page")
        if resume_button:
            st.experimental_set_query_params()
    else:
        resume_placeholder.empty()
with st.container():
    if tabs3:
        contact_placeholder.title("Contact Me")
        contact_button = contact_placeholder.button("Back to Main Page")
        if contact_button:
            st.experimental_set_query_params()
    else:
        contact_placeholder.empty()


with st.container():
    if not any([tabs1, tabs2, tabs3]):
        st.title(":grinning: VV")
        st.subheader("A student in Singapore")
        st.write("[Find out more about me 👈](https://tarannator.blogspot.com/)")

        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Latest Updates")
            st.write("##")
            st.write("")
    st.write("[My YouTube Channel 👈](https://youtube.com)")
