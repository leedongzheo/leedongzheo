import streamlit as st
import cv2
import numpy as np
import Chuong3 as c3
import os

class SessionState(object):
    def __init__(self):
        self.imgin = None
        self.imgout = None

def main():
    session_state = SessionState()

    st.title("Machine Vision")
    menu = st.sidebar.selectbox("Menu", ("Chuong3", "Chuong4", "Chuong5", "Chuong9"))

    if menu == "Chuong3":
        chuong3(session_state)

def chuong3(session_state):
    st.subheader("Chương 3")
    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "tif"])

    if file_uploaded is not None:
        image = np.array(bytearray(file_uploaded.read()), dtype=np.uint8)
        session_state.imgin = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

        col1, col2, col3 = st.columns([3, 3, 2])

        with col2:
            st.subheader("Output Image")

        with col1:
            st.subheader("Input Image")
            st.image(session_state.imgin, use_column_width=True)

        with col3:
            st.subheader("Buttons")

            if st.button("Apply Negative"):
                session_state.imgout = c3.Negative(session_state.imgin)
                display_image(col2, session_state.imgout, "Negative Image")

            if st.button("Apply Logarithmic"):
                session_state.imgout = c3.Logarit(session_state.imgin)
                display_image(col2, session_state.imgout, "Logarithmic Image")

            if st.sidebar.button("Save Image"):
                if session_state.imgout is not None:
                    save_image(session_state.imgout)
                else:
                    st.sidebar.warning("Không có ảnh đầu ra để lưu.")

def save_image(image):
    output_folder = st.sidebar.text_input("Nhập đường dẫn đến thư mục:", placeholder="path/to/output/folder")

    if output_folder:
        if os.path.isdir(output_folder):
            output_filename = "ảnh.jpg"
            output_path = os.path.join(output_folder, output_filename)
            cv2.imwrite(output_path, image)
            st.sidebar.success(f"Ảnh đã được lưu vào: {output_path}")
        else:
            st.sidebar.warning("Đường dẫn thư mục không hợp lệ.")
    else:
        st.sidebar.warning("Vui lòng nhập đường dẫn đến thư mục.")

def display_image(column, img, caption):
    column.image(img, caption, use_column_width=True)

if __name__ == "__main__":
    main()
