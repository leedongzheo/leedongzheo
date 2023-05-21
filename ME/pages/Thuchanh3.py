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

        st.image(imgin, caption="Input Image", use_column_width=True)

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

    if st.button("Apply Histogram"):
        imgout = c3.Histogram(imgin)
        st.image(imgout, caption="Histogram Image", use_column_width=True)

    if st.button("Apply HistEqual"):
        imgout = c3.HistEqual(imgin)
        st.image(imgout, caption="HistEqual Image", use_column_width=True)

    if st.button("Apply HistEqualColor"):
        imgout = c3.HistEqualColor(imgin)
        st.image(imgout, caption="HistEqualColor Image", use_column_width=True)

    if st.button("Apply LocalHist"):
        imgout = c3.LocalHist(imgin)
        st.image(imgout, caption="LocalHist Image", use_column_width=True)

    if st.button("Apply HistStat"):
        imgout = c3.HistStat(imgin)
        st.image(imgout, caption="HistStat Image", use_column_width=True)

    if st.button("Apply MyBoxFilter"):
        imgout = c3.MyBoxFilter(imgin)
        st.image(imgout, caption="MyBoxFilter Image", use_column_width=True)

    if st.button("Apply BoxFilter"):
        imgout = c3.BoxFilter(imgin)
        st.image(imgout, caption="BoxFilter Image", use_column_width=True)

    if st.button("Apply Threshold"):
        imgout = c3.Threshold(imgin)
        st.image(imgout, caption="Threshold Image", use_column_width=True)

    if st.button("Apply MedianFilter"):
        imgout = c3.MedianFilter(imgin)
        st.image(imgout, caption="MedianFilter Image", use_column_width=True)

    if st.button("Apply Sharpen"):
        imgout = c3.Sharpen(imgin)
        st.image(imgout, caption="Sharpen Image", use_column_width=True)

    if st.button("Apply Gradient"):
        imgout = c3.Gradient(imgin)
        st.image(imgout, caption="Gradient Image", use_column_width=True)
if __name__ == "__main__":
    main()
