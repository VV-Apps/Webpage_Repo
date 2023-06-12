import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")

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
