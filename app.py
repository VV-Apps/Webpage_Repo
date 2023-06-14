import streamlit as st

st.set_page_config(page_title="VV", page_icon=":waving:", layout="wide")

# Display the picture from the repository in the sidebar
st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.png", use_column_width=True)

# Add the title "PGOS" beside the picture
st.sidebar.title("VV_Webpage")

# Add tabs in a section next to the picture and title
tabs1 = st.sidebar.button("About Me")
tabs2 = st.sidebar.button("Resume")
tabs3 = st.sidebar.button("Contact Me")

# Create empty placeholders for tab contents
about_us_placeholder = st.empty()
campaigns_placeholder = st.empty()
join_us_placeholder = st.empty()

# Update tab content based on button press
if tabs1:
    about_us_placeholder.subheader("Vision")
else:
    about_us_placeholder.empty()

if tabs2:
    campaigns_placeholder.title("Resume")
    campaigns_placeholder.subheader("Education")
#    campaigns_placeholder.write("Our Inaugural Music Concert to be held at the end of the year (3rd Dec)")
else:
    campaigns_placeholder.empty()

if tabs3:
    join_us_placeholder.title("Contact Me")
else:
    join_us_placeholder.empty()

# Add other content in the main section
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
            st.write(
                ""
            )
    st.write("[My YouTube Channel 👈](https://youtube.com)")
