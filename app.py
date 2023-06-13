import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Add a picture at the top left corner
st.sidebar.image("C:\Users\Vignesh\Desktop\PGOS.png", use_column_width=True)

# Add the title "PGOS" beside the picture
st.sidebar.title("PGOS")

# Add tabs in a section next to the picture and title
tabs = st.sidebar.multiselect(
    "Select Tabs",
    ["Tab 1", "Tab 2", "Tab 3"],
    default=["Tab 1"]
)

# Render selected tabs
for tab in tabs:
    if tab == "Tab 1":
        st.write("Content of Tab 1")
    elif tab == "Tab 2":
        st.write("Content of Tab 2")
    elif tab == "Tab 3":
        st.write("Content of Tab 3")

# Add other content in the main section
with st.container():
    st.subheader("Hi, I am Vignesh :wave:")
    st.title("A student from Singapore")
    st.write("About ME")
    st.write("[Learn More 👈](https://tarannator.blogspot.com/)")

with st.container():
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

