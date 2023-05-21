import streamlit as st
import cv2
import numpy as np
import Chuong3 as c3
import tempfile
from PIL import Image
import os
imgin = None
imgout = None


def main():
    global imgin, imgout
    st.title("Machine Vision")
    menu = st.sidebar.selectbox("Menu", ("Chuong3", "Chuong4", "Chuong5", "Chuong9"))
    st.sidebar.success("save")
    if menu=="Chuong3":
        st.subheader("Chương 3")
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
                    display_image(col2, imgout, "Negative Image")

                if st.button("Apply Logarithmic"):
                    imgout = c3.Logarit(imgin)
                    display_image(col2, imgout, "Logarithmic Image")

                if st.button("Apply Power"):
                    imgout = c3.Power(imgin)
                    display_image(col2, imgout,"Power Image")

                if st.button("Apply PiecewiseLinear"):
                    imgout = c3.PiecewiseLinear(imgin)
                    display_image(col2, imgout, "PiecewiseLinear Image")
                    
                if st.button("Apply Histogram"):
                    imgout = c3.Histogram(imgin)
                    display_image(col2, imgout, "Histogram Image")
                    
                if st.button("Apply HistEqual"):
                    imgout = c3.HistEqual(imgin)

                if st.button("Apply HistEqualColor"):
                    imgout = c3.HistEqualColor(imgin)
                    display_image(col2, imgout, "HistEqualColor Image")
                    
                if st.button("Apply LocalHist"):
                    imgout = c3.LocalHist(imgin)
                    display_image(col2, imgout, "LocalHist Image")

                if st.button("Apply HistStat"):
                    imgout = c3.HistStat(imgin)
                    display_image(col2, imgout, "HistStat Image")
                if st.button("Apply MyBoxFilter"):
                    imgout = c3.MyBoxFilter(imgin)
                    display_image(col2, imgout, "MyBoxFilter Image")
                if st.button("Apply BoxFilter"):
                    imgout = c3.BoxFilter(imgin)
                    display_image(col2, imgout, "BoxFilter Image")

                if st.button("Apply Threshold"):
                    imgout = c3.Threshold(imgin)
                    display_image(col2, imgout, "Threshold Image")       

                if st.button("Apply MedianFilter"):
                    imgout = c3.MedianFilter(imgin)
                    display_image(col2, imgout, "MedianFilter Image")

                if st.button("Apply Sharpen"):
                    imgout = c3.Sharpen(imgin)
                    display_image(col2, imgout, "Sharpen Image")

                if st.button("Apply Gradient"):
                    imgout = c3.Gradient(imgin)
                    display_image(col2, imgout, "Gradient Image")
                if st.sidebar.button("Save Image"):
                    save_image(imgout)
                
    elif menu=="Chuong4":
        st.subheader("Chương 3")
        file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png","tif"])
        if file_uploaded is not None:
            image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
            imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
                
def save_image(image):
    dummy_file = st.file_uploader("Choose a file to select the directory", type=".txt", key="dummy")
    if dummy_file is not None:
        dummy_file_path = os.path.abspath(dummy_file.name)
        save_folder = st.select_folder("Select a folder to save the image")
        if save_folder:
            image.save(os.path.join(save_folder, "image.png"))

def display_image(column, img, caption):
    #column.subheader(caption)
    column.image(img,caption, use_column_width=True)

if __name__ == "__main__":
    main()
