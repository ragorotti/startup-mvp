import streamlit as st

def app():
    st.title('Home')

    st.write('This is the `home page` of this multi-page app.')

    st.write('In this app, ...')

    col1, col2 = st.columns(2)

    with col1:
        st.header("Image Classification")
        st.write("Column 1 - classification options")

    with col2:
        st.header("Image Processing")
        st.write("Column 2 - image processing options")
