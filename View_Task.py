import streamlit as st
from tasks import view_tasks,update_task,delete_task

st.title("Your Tasks")
if not st.session_state.get("user"):
    st.error("Login first")
    st.stop()

user_id=st.session_state.user[0]
tasks=view_tasks(user_id)
st.table(tasks)

if tasks:
    ids=[t[0] for t in tasks]
    sel=st.selectbox("Select Task ID",ids)
    sel_task=[t for t in tasks if t[0]==sel]
    if sel_task:
        sel_task=sel_task[0]
        t=st.text_input("Title",sel_task[2])
        d=st.text_area("Desc",sel_task[3])
        p=st.selectbox("Priority",["Low","Medium","High"],index=["Low","Medium","High"].index(sel_task[4]))
        s=st.selectbox("Status",["Pending","Completed"],index=["Pending","Completed"].index(sel_task[5]))
        dl=st.text_input("Deadline",sel_task[6])

        if st.button("Update Task"):
            update_task(sel,t,d,p,s,dl)
            st.success("Updated")
            st.rerun()
        if st.button("Delete Task"):
            delete_task(sel)
            st.warning("Deleted")
            st.rerun()    

