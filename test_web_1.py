import streamlit as st
import requests

# API URL
api_url = "http://localhost:8000"


# Chức năng đăng ký
def register():
    st.title("Đăng Ký")
    name = st.text_input("Tên")
    email = st.text_input("Email")
    password = st.text_input("Mật khẩu", type="password")
    confirm_password = st.text_input("Xác nhận mật khẩu", type="password")

    if st.button("Đăng Ký"):
        if password == confirm_password:
            response = requests.post(
                f"{api_url}/register",
                data={"name": name, "email": email, "password": password},
            )
            st.write(response.json())
        else:
            st.write("Mật khẩu không khớp!")


# Chức năng đăng nhập
def login():
    st.title("Đăng Nhập")
    email = st.text_input("Email")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Đăng Nhập"):
        response = requests.post(
            f"{api_url}/login", data={"email": email, "password": password}
        )
        st.write(response.json())


# Chức năng suy luận
def predict():
    st.title("Suy Luận")
    file = st.file_uploader(
        "Tải lên hình ảnh cây khoai mì", type=["jpg", "jpeg", "png"]
    )

    if st.button("Suy Luận"):
        if file is not None:
            files = {"file": file.getvalue()}
            response = requests.post(f"{api_url}/predict", files=files)
            st.write(response.json())


# Chức năng xem lịch sử
def history():
    st.title("Lịch Sử Suy Luận")
    email = st.text_input("Email")

    if st.button("Xem Lịch Sử"):
        response = requests.get(f"{api_url}/history", params={"email": email})
        st.write(response.json())


# Sidebar navigation
st.sidebar.title("Menu")
page = st.sidebar.selectbox(
    "Chọn trang", ["Đăng Ký", "Đăng Nhập", "Suy Luận", "Lịch Sử Suy Luận"]
)

if page == "Đăng Ký":
    register()
elif page == "Đăng Nhập":
    login()
elif page == "Suy Luận":
    predict()
elif page == "Lịch Sử Suy Luận":
    history()
