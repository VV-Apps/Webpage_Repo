import streamlit as st

st.set_page_config(page_title="PGOS Website", page_icon=":music:",layout="wide")

with st.container():
    st.title("A Youth Led Organisation")
    st.subtitle("That hopes to leverage music as a platform to bring joy and comfort to people at all stages of life, by providing learning opportunities to the community.")
with st.container():
    st.write("Vision & Mission")
    st.subtitle("To leverage music as a platform to bring joy and comfort to people at all stages of life, by providing learning opportunities to the community.")
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
