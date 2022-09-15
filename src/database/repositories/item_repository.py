from http.client import HTTPException
from ..db_context import connect_db
from ...burger95s.dto.models.item_info import Item, ItemInfo

def get_items():
    res = None
    try:
        query = "SELECT * FROM item WHERE is_deleted = false ORDER BY id;"
        db = connect_db()
        cur = db.cursor()
        cur.execute(query)
        res = cur.fetchall()
    except:
        raise HTTPException("check for connection of database. There are something wrong about it !")
    finally:
        db.close()

    return res

def get_particular_items(type):
    res = None
    try:
        query = " SELECT * FROM item WHERE type = %s ORDER BY id;"
        db = connect_db()
        cur = db.cursor()
        cur.execute(query, (type, ))
        res = cur.fetchall()
    
    except:
        raise HTTPException("check for connection of database. There are something wrong about it !")

    finally:
        db.close()

    return res


def get_item_by_id(itemid):
    res = None
    try:
        query = "SELECT * FROM item WHERE id = %s;"
        db = connect_db()
        cur = db.cursor()
        cur.execute(query,(itemid, ))
        res = cur.fetchone()
    
    except:
        raise HTTPException("check for connection of database. There are something wrong about it !")
    
    finally:
        db.close()

    return res


def create_item(item: ItemInfo):
    try:
        query = "INSERT INTO item(name, price, type) VALUES(%s, %s, %s);"
        db = connect_db()
        cur = db.cursor()
        cur.execute(query,(item.item_name, item.price, item.type))
        db.commit()
    
    except:
        raise HTTPException("check for connection of database. There are something wrong about it !")
    
    finally:
        db.close()
    
    return "New item is created successfully !"

def update_item(itemid, item: ItemInfo):
    try:
        query = "UPDATE item SET name = %s, price = %s, type = %s, size = %s WHERE id = %s;"
        db = connect_db()
        cur = db.cursor()
        cur.execute(query,(item.item_name, item.price, item.type, item.size, itemid))
        db.commit()
    except:
        raise HTTPException("check for connection of database. There are something wrong about it !")
    
    finally:
        db.close()
    
    return "Item have been updated !"



def delete_item(itemid, is_hard_delete):
    try:
        if is_hard_delete:
            query = "DELETE FROM item WHERE id = %s;"

        else:
            query = "UPDATE item SET is_deleted = true WHERE id = %s;"
        db = connect_db()
        cur = db.cursor()
        cur.execute(query, (itemid, ))
        db.commit()
    
    except:
        raise HTTPException("check for connection of database. There are something wrong about it !")
    
    finally:
        db.close()
    
    if is_hard_delete:

        return "Erase Item permanently !"

    return 'Item has been deleted successfully !'

