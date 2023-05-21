import streamlit as st
import cv2
import numpy as np
import sys
import Chuong3 as c3

def main():
    st.set_page_config(page_title="Chương 3")

    st.subheader("Chương 3")
    st.sidebar.header("Chương 3")

    imgin = None
    imgout = None

    menu_choice = st.sidebar.selectbox("Chapter", ["Chapter 3", "Chapter 4", "Chapter 5", "Chapter 9"])

    if menu_choice == "Chapter 3":
        chapter_3_menu(imgin, imgout)

def chapter_3_menu(imgin, imgout):
    st.sidebar.subheader("Chapter 3 Menu")
    option = st.sidebar.selectbox("Choose an option", ["Open", "OpenColor", "Save", "Negative", "Logarit", "PiecewiseLinear"])

    if option == "Open":
        imgin = open_image()
        if imgin is not None:
            st.image(imgin, caption="Image In")

    elif option == "OpenColor":
        imgin = open_color_image()
        if imgin is not None:
            st.image(imgin, caption="Image In")

    elif option == "Save":
        if imgout is not None:
            save_image(imgout)

    elif option == "Negative":
        if imgin is not None:
            imgout = c3.Negative(imgin)
            st.image(imgout, caption="Image Out")

    elif option == "Logarit":
        if imgin is not None:
            imgout = c3.Logarit(imgin)
            st.image(imgout, caption="Image Out")

    elif option == "PiecewiseLinear":
        if imgin is not None:
            imgout = c3.PiecewiseLinear(imgin)
            st.image(imgout, caption="Image Out")

def open_image():
    file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if file is not None:
        image = np.array(Image.open(file))
        return image
    return None

def open_color_image():
    file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if file is not None:
        image = cv2.imread(file)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return None

def save_image(image):
    file = st.file_uploader("Save image as", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
    if file is not None:
        cv2.imwrite(file.name, image)

if __name__ == "__main__":
    main()