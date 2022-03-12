import streamlit as st

def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    uploaded_files = st.sidebar.file_uploader("Upload your file here", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.sidebar.write("filename:", uploaded_file.name)
        st.sidebar.write(bytes_data)

    number = st.sidebar.number_input("Insert a number")
    st.sidebar.write("The current number is ", number)