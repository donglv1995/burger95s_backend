from http.client import HTTPException
import src.database.db_context as dbcontext
from src.burger95s.models.user_info import UserInfo

def get_all_users():
    try:
        query = "SELECT * FROM Users WHERE is_deleted = false;"
        db = dbcontext.connect_db()
        cur = db.cursor()
        cur.execute(query)
        res = cur.fetchall()

    except:
        raise HTTPException(status_code=500, detail="Cause some issues relate to connection with database, please check it")

    finally:
        db.close()

    return res

def get_user_by_id(user_id):
    # to prevent SQL injection we use query parameter
    try:
        query = "SELECT * FROM Users WHERE user_id = %s;"
        db = dbcontext.connect_db()
        cur = db.cursor()
        cur.execute(query, (user_id,))
        res = cur.fetchone()
    
    except:
        raise HTTPException(status_code=500, detail="Cause some issues relate to connection with database or there is no User such, please check it")

    finally:
        db.close()

    return res

def create_user(user: UserInfo):
    try:
        query = "INSERT INTO Users(user_name, gender, phone) VALUES(%s, %s, %s);"
        db = dbcontext.connect_db()
        cur = db.cursor()
        cur.execute(query,(user.user_name, user.gender, user.phone))
        db.commit()
    
    except:
        raise HTTPException(status_code=500, detail="Cause some issues relate to connection with database, please check it")

    finally:
        db.close()

    return "A newly user is created !"

def update_user(user_id, user: UserInfo):
    try:
        query = "UPDATE Users SET user_name = %s, gender = %s, phone = %s WHERE user_id = %s;"
        db = dbcontext.connect_db()
        cur = db.cursor()
        cur.execute(query,(user.user_name, user.gender, user.phone, user_id))
        db.commit()
    
    except:
        raise HTTPException(status_code=500, detail="Cause some issues relate to connection with database or there is no ID such, please check it")

    finally:
        db.close()

    return "Update information successfully !"


def delete_user(user_id, is_hard_delete: bool):
    try:
    
        if is_hard_delete:
            query = "DELETE FROM Users WHERE user_id = %s;"
            
        else:
            query = "UPDATE Users SET is_deleted = true WHERE user_id = %s;"

        db = dbcontext.connect_db()
        cur = db.cursor()
        cur.execute(query, (user_id,))
        db.commit()
        
    except:
        raise HTTPException(status_code=500, detail="Cause some issues relate to connection with database or there is no ID user such, please check it")
    
    finally:
        db.close()
    
    if is_hard_delete:

        return "Erase User permanently !"

    return "User has been deleted successfully !"




