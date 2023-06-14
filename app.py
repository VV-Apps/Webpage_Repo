import streamlit as st

st.set_page_config(page_title="Project Gift of Song", page_icon=":notes:", layout="wide")

# Display the picture from the repository in the sidebar
st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/PGOS.png", use_column_width=True)

# Add the title "PGOS" beside the picture
st.sidebar.title("Project Gift of Song")

# Add tabs in a section next to the picture and title
tabs1 = st.sidebar.button("About Us")
tabs2 = st.sidebar.button("Campaigns & Activities")
tabs3 = st.sidebar.button("Join Us")

# Create empty placeholders for tab contents
about_us_placeholder = st.empty()
campaigns_placeholder = st.empty()
join_us_placeholder = st.empty()

# Update tab content based on button press
if tabs1:
    about_us_placeholder.title("Aims")
    about_us_placeholder.subheader("Vision & Mission")
    about_us_placeholder.write("Founded by a group of zealous youths with a passion for music, Project Gift of Song aims to bridge the gap between music and terminal illnesses. We wish to bring joy and comfort to all stages of life through the spread of music.")
else:
    about_us_placeholder.empty()

if tabs2:
    campaigns_placeholder.title("Concerts")
    campaigns_placeholder.subheader("Our Inaugural Music Concert")
#    campaigns_placeholder.write("Our Inaugural Music Concert to be held at the end of the year (3rd Dec)")
else:
    campaigns_placeholder.empty()

if tabs3:
    join_us_placeholder.title("Structure")
else:
    join_us_placeholder.empty()

# Add other content in the main section
with st.container():
    if not any([tabs1, tabs2, tabs3]):
        st.title(":notes: Project Gift of Song")
        st.subheader("A student-run organization founded in Singapore")
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
