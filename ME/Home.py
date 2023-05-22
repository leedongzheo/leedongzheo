import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("<h1 style='font-size: 50px;color:black'>Welcome to the website of Nguyen Tran Anh Thu! 👋</h1>", unsafe_allow_html=True)
st.sidebar.success("You can choose one of my projects above.")


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image.jpg')    
st.markdown(
    """
    <style>
    .red-text {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="red-text">
        Hello! Thank you for visiting my website. Here are the projects I have learned through the Machine Learning and Image Processing courses.
        This website is created for the purpose of reporting the final projects for these courses and is only used for educational purposes.
        👉 You can choose one of the projects I have learned on the left side.
    </div>
    """
)
