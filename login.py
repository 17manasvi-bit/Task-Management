import hashlib
from database import create_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username,password):
    conn=create_connection()
    cur=conn.cursor()
    try:
        cur.execute("Insert into users(username,password) Values (?,?)",(username,hash_password(password)))
        conn.commit()
        return True
    except Exception as e:
        return False
    finally:
        conn.close()

def verify_user(username,password):
    conn=create_connection()
    cur=conn.cursor()
    cur.execute("Select id,username from users where username=? and password=?",(username,hash_password(password)))  
    user=cur.fetchone()
    conn.close()
    return user      
                        
                            