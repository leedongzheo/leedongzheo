import streamlit as st
import cv2
import numpy as np
import Chuong3 as c3
import os
import shutil

output_dir = "output_images"
output_image = None

def main():
    st.title("Computer Vision")
    menu = st.sidebar.selectbox("Menu", ("Chuong3", "Chuong4", "Chuong5", "Chuong9"))

    if menu == "Chuong3":
        chuong3()

def chuong3():
    global output_image

    st.subheader("Chương 3")
    file_uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "tif"])

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
                output_image = imgout
                display_image(col2, imgout, "Negative Image")

            if st.button("Apply Logarithmic"):
                imgout = c3.Logarit(imgin)
                output_image = imgout
                display_image(col2, imgout, "Logarithmic Image")

            if st.sidebar.button("Save Image"):
                if output_image is not None:
                    save_image(output_image)
                else:
                    st.sidebar.warning("Không có ảnh đầu ra để lưu.")

def save_image(image):
    output_folder = st.sidebar.text_input("Nhập đường dẫn đến thư mục:", placeholder="path/to/output/folder")
    output_folder = output_folder.replace("\\", "/")

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
    # Xóa thư mục tạm nếu tồn tại
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    
    # Tạo thư mục tạm
    os.makedirs(output_dir)
    
    main()
