import streamlit as st
from database import create_connection

st.set_page_config(page_title="Admin Dashboard")

st.title("Admin panel--Task Manages")

if "user" not in st.session_state or st.session_state.user is None:
    st.error("You must Login First!!")
    st.stop()

if st.session_state.user[1]!="Manasvi N":
    st.error("Only Admin can access this pages! ")
    st.stop()

conn=create_connection()
cur=conn.cursor()

st.subheader("Registered users")
cur.execute("SELECT id,username FROM users")
users=cur.fetchall()
st.table(users)

st.subheader("All Tasks")
cur.execute("SELECT * from tasks")
all_tasks=cur.fetchall()
st.table(all_tasks)

if all_tasks:
    task_ids=[task[0] for task in all_tasks]
    delete_task_id=st.selectbox("Select Task ID to delete",task_ids)

    if st.button("Delete task"):
        cur.execute("Delete from tasks where id=?",(delete_task_id,))
        conn.commit()
        st.warning("Task deleted successfully!")
        st.rerun()

st.subheader("Delete User")
user_ids=[user[0] for user in users]
delete_user_id=st.selectbox("Selete user ID to delete",user_ids)

if st.button("Delete User"):
    cur.execute("Delete from tasks where user_id=?",(delete_user_id,))
    cur.execute("Delete from users where id=?",(delete_user_id,))
    conn.commit()
    st.warning("User and their Tasks deleted successfully!!")
    

st.subheader("System Overview")

cur.execute("SELECT COUNT(*) FROM users")
total_users=cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM tasks")
tatal_tasks=cur.fetchone()[0]

col1,col2=st.columns(2)
col1.metric("Toatal users",total_users)
col2.metric("Total tasks",tatal_tasks)


