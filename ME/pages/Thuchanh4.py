import streamlit as st
import cv2
import numpy as np
import Chuong3 as c3

def main():
    st.title("Digital Image Processing")

    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file_uploaded is not None:
        image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
        imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

        col1, col2 = st.beta_columns(2)
        with col1:
            st.image(imgin, caption="Input Image", use_column_width=True)

        with col2:
            if st.button("Apply Negative"):
                imgout = c3.Negative(imgin)
                st.image(imgout, caption="Negative Image", use_column_width=True)

            if st.button("Apply Logarithmic"):
                imgout = c3.Logarit(imgin)
                st.image(imgout, caption="Logarithmic Image", use_column_width=True)

            if st.button("Apply Power"):
                imgout = c3.Power(imgin)
                st.image(imgout, caption="Power Image", use_column_width=True)

            if st.button("Apply PiecewiseLinear"):
                imgout = c3.PiecewiseLinear(imgin)
                st.image(imgout, caption="PiecewiseLinear Image", use_column_width=True)

if __name__ == "__main__":
    main()