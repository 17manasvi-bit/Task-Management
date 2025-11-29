import sqlite3
def create_connection():
    return sqlite3.connect('tasks.db',check_same_thread=False)

def create_tables():
    conn=create_connection()
    cur=conn.cursor()
                
    cur.execute("""create table if not exists Users(
                                id Integer primary key autoincrement,
                                username text not null,
                                password varchar not null
                            )
                """)

    cur.execute("""
                            create table if not exists Tasks(
                            id integer primary key autoincrement,
                            user_id integer,
                            title text,
                            decription text,
                            priority text,
                            status text,
                            deadline text,
                            foreign key(user_id) references users(id)
                            )
                            """)    
    conn.commit()
    conn.close()
if __name__=="__main__":
    create_tables()    
                
