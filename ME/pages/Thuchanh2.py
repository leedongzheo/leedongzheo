import streamlit as st
import cv2
import numpy as np
import Chuong3 as c3

st.set_page_config(page_title="Chương 3")

st.subheader("Chương 3")
st.sidebar.header("Chương 3")

# Khai báo biến toàn cục
imgin = None
imgout = None

def main():
    global imgin, imgout

    st.title("Machine Vision")

    menu = st.sidebar.selectbox("Menu", ("File", "Chapter3", "Chapter4", "Chapter5", "Chapter9"))

    if menu == "File":
        st.header("File Menu")

        if st.button("Open"):
            imgin = open_image()
            if imgin is not None:
                st.image(imgin, caption="Ảnh đầu vào", use_column_width=True)

        if st.button("Save"):
            if imgout is not None:
                save_image(imgout)
                st.success("Đã lưu ảnh")

    elif menu == "Chapter3":
        st.header("Chapter 3 Menu")

        if st.button("Negative"):
            if imgin is not None:
                imgout = c3.Negative(imgin)
                st.image(imgout, caption="Ảnh sau khi áp dụng Negative", use_column_width=True)

        if st.button("Logarit"):
            if imgin is not None:
                imgout = c3.Logarit(imgin)
                st.image(imgout, caption="Ảnh sau khi áp dụng Logarit", use_column_width=True)

        if st.button("PiecewiseLinear"):
            if imgin is not None:
                imgout = c3.PiecewiseLinear(imgin)
                st.image(imgout, caption="Ảnh sau khi áp dụng Piecewise Linear", use_column_width=True)

        if st.button("Histogram"):
            if imgin is not None:
                imgout = c3.Histogram(imgin)
                st.image(imgout, caption="Ảnh sau khi áp dụng Histogram", use_column_width=True)

    # Thêm các phần khác của menu ở đây (Chapter4, Chapter5, Chapter9)

def open_image():
    ftypes = [('Images', '*.jpg *.tif *.bmp *.gif *.png')]
    fl = st.file_uploader("Chọn ảnh đầu vào", type=ftypes)
    if fl is not None:
        img = np.array(Image.open(fl))
        return img
    return None

def save_image(img):
    file_path = st.file_savebox("Lưu ảnh", type=ftypes)
    if file_path is not None:
        cv2.imwrite(file_path, img)

if __name__ == '__main__':
    main()