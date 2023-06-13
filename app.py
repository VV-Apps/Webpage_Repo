import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Display the picture from the repository in the sidebar
st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/PGOS.png", use_column_width=True)

# Add the title "PGOS" beside the picture
st.sidebar.title("Project Gift of Song")

# Add tabs in a section next to the picture and title
tabs = st.sidebar.button("About Us")
if tabs:
    st.title("Aims")
    st.subheader("Vission & Mission")
    st.write("Founded by a group of zealous youths with a passion for music, Project Gift of Song aims to bridge the gap between music and terminal illnesses. We wish to bring joy and comfort to all stages of life through the spread of music.")

tabs = st.sidebar.button("Campaigns & Activities")
if tabs:
    st.title("Concerts")
    st.suheader("Our Inaugural Music Concert")
    st.write("Our Inaugural Music Concert to be held at the end of the year (3rd Dec)")

tabs = st.sidebar.button("Join Us")
if tabs:
    st.title("Structure")

    #any([st.session_state.get("Tab 1"), st.session_state.get("Tab 2"), st.session_state.get("Tab 3")])
# Add other content in the main section
with st.container():
    if not tabs:
        st.subheader("Hi, I am Vignesh :wave:")
        st.title("A student from Singapore")
        st.write("About ME")
        st.write("[Learn More 👈](https://tarannator.blogspot.com/)")

        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                
                
                """
            )

st.write("[YouTube Channel 👈](https://youtube.com)")

