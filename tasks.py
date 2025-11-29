import streamlit as st
from database import create_connection

def add_tasks(user_id,title,description,priority,status,deadline):
    conn=create_connection()
    cur=conn.cursor()
    cur.execute("""
    INSERT INTO tasks (user_id, title, description, priority, status, deadline)
    VALUES (?,?,?,?,?,?)""", (user_id, title, description, priority, status, deadline))

    conn.commit()
    conn.close() 

def view_tasks(user_id):
    conn=create_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM tasks where user_id=?",(user_id,))
    data=cur.fetchall()
    conn.close()
    return data

def update_task(task_id,title,description,priority,status,deadline):
    conn=create_connection()
    cur=conn.cursor()
    cur.execute(""" 
    Update tasks set title=?,description=?,priority=?,status=?,deadline=?where id=?""",(title,description,priority,status,deadline,task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn=create_connection()
    cur=conn.cursor()
    cur.execute("Delete from tasks where id=?",(task_id,))
    conn.commit()
    conn.close()    





