import streamlit as st
from tasks import add_tasks

st.title("➕ Add Task")
if not st.session_state.get("user"):
    st.error("Login first")
    st.stop()


title=st.text_input("Title")
desc=st.text_area("Description")
priority=st.selectbox("Priority",["Low","Medium","High"])
status=st.selectbox("Status",["Pending","Completed"])
deadline=st.date_input("Deadline")

if st.button("Save Task"):
    add_tasks(st.session_state.user[0],title,desc,priority,status,str(deadline))
    st.success("Task added Successfully😁")
    