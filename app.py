import streamlit as st
from database import create_tables
from login import verify_user,register_user

create_tables()
st.set_page_config(page_title="TASK MANAGEMENT --LOGIN", layout="centered")
bg_url="https://i.pinimg.com/1200x/eb/71/c0/eb71c0c122fc4102080357bbdca4acc3.jpg"
st.markdown(f"""
<style>
.stApp{{
        background-image:url("{bg_url}");
        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;                 
}}  
</style>
""",unsafe_allow_html=True)                                  
st.title("TASK MANAGEMENT")
if "user" not in st.session_state:
    st.session_state.user=None

choice= st.selectbox("Choose",["Login","Register"])

if choice=="Login":
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    if st.button("Login"):
        user=verify_user(username,password)
        if user:
            st.session_state.user=user
            st.success("Logged in Successfully!!")
            if st.session_state.user[1]=='Manasvi N':
               st.switch_page('pages/Admin.py')
            else:
               st.switch_page('pages/Add_task.py')
        
        else:
            st.error("Invaild Credentials")

else:
    new_user=st.text_input("Username",key="reg_user")
    new_pass=st.text_input("Password",type="password",key="reg_pass")
    if st.button("Create Account"):
        ok=register_user(new_user,new_pass)
        if ok:
            st.success("Account created-Please login")
        else:
            st.error("Username already taken ")
                        