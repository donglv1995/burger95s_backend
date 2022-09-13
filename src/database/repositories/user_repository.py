import src.database.db_context as dbcontext
from ...burger95s.models.user_info import User 

def get_all_users():
    query = "SELECT * FROM UserInfo WHERE is_deleted = false;"
    db = dbcontext.connect_db()
    cur = db.cursor()
    cur.execute(query)
    res = cur.fetchall()
    db.close()

    return res

def get_user_by_id(userid):
    # to prevent SQL injection we're using query parameter
    query = "SELECT * FROM UserInfo WHERE user_id = %s;"
    db = dbcontext.connect_db()
    cur = db.cursor()
    cur.execute(query, (userid,))
    res = cur.fetchone()
    db.close()

    return res

def create_user(user: User):

    query = "INSERT INTO UserInfo(user_name, gender, phone) VALUES(%s, %s, %s);"
    db = dbcontext.connect_db()
    cur = db.cursor()
    cur.execute(query,(user.user_name, user.gender, user.phone))
    db.commit()
    db.close()

    return "A newly user is created !"

def update_user(user: User):

    query = "UPDATE UserInfo SET user_name = %s, gender = %s, phone = %s WHERE user_id = %s;"
    db = dbcontext.connect_db()
    cur = db.cursor()
    cur.execute(query,(user.user_name, user.gender, user.phone, user.user_id))
    db.commit()
    db.close()

    return "Update information successfully !"


def delete_user(userid, is_hard_delete: bool):
    soft_delete_query = "UPDATE UserInfo SET is_deleted = true WHERE user_id = %s;"
    hard_delete_query = "DELETE FROM UserInfo WHERE user_id = %s;"
    db = dbcontext.connect_db()
    cur = db.cursor()

    if is_hard_delete:
        cur.execute(hard_delete_query, (userid,))
        db.commit()
        db.close()

        return "Permanent deletion successfully !"
        
    else:
        cur.execute(soft_delete_query, (userid,))
        db.commit()
        db.close()

        return "Temporary deletion successfully !"



