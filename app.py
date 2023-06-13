import streamlit as st

st.set_page_config(page_title="Project Gift of Song", page_icon=":notes:", layout="wide")

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
    st.subheader("Our Inaugural Music Concert")
    st.write("Our Inaugural Music Concert to be held at the end of the year (3rd Dec)")

tabs = st.sidebar.button("Join Us")
if tabs:
    st.title("Structure")

# Add other content in the main section
with st.container():
    if not any([st.session_state.get("Vission & Mission"), st.session_state.get("Campaigns & Activities"), st.session_state.get("Join Us")]):
        st.title(":notes: Project Gift of Song")
        st.subheader("A student run organisation founded in Singapore")
        st.write("[Find out more about us 👈](https://tarannator.blogspot.com/)")

        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Latest Events")
            st.write("##")
            st.write(
                "Electrical Boogaloo"
                "Electrical Boogaloo Part 2"
            )

st.write("[Our Very Own YouTube Channel 👈](https://youtube.com)")

