import streamlit as st
import cv2
import numpy as np
import Chuong3 as c3

def main():
    st.title("Digital Image Processing")

    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png","tif"])
    if file_uploaded is not None:
        image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
        imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

        col1, col2, col3 = st.columns([3, 3, 2])
        with col2:
            st.subheader("Output Image")
        with col1:
            st.subheader("Input Image")
            st.image(imgin, use_column_width=True)

        with col3:
            st.subheader("Buttons")
            if st.button("Apply Negative"):
                imgout = c3.Negative(imgin)
                display_image(col2, imgout, caption="Negative Image")

            if st.button("Apply Logarithmic"):
                imgout = c3.Logarit(imgin)
                display_image(col2, imgout, caption="Logarithmic Image")

            if st.button("Apply Power"):
                imgout = c3.Power(imgin)
                display_image(col2, imgout, caption="Power Image")

            if st.button("Apply PiecewiseLinear"):
                imgout = c3.PiecewiseLinear(imgin)
                display_image(col2, imgout, "PiecewiseLinear Image")

def display_image(column, img, caption):
    #column.subheader(caption)
    column.image(img,caption, use_column_width=True)

if __name__ == "__main__":
    main()