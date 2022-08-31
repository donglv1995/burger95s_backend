import json
from pydantic import BaseModel
from fastapi import HTTPException


class User(BaseModel):
    userid: int
    username: str
    age: int


users = []


def read_all_users():
    file_read = open('src/dummy_data.json', 'r+')
    j = json.load(file_read)
    file_read.close()
    for user in j['users']:
        users.append(User(**user))


def read_user_byId(userid):
    file_read = open('src/dummy_data.json', 'r+')
    data = json.load(file_read)
    file_read.close()
    for u in data['users']:
        if userid == u['userid']:
            return u
    raise HTTPException(status_code=404, detail="User not found")
        


def create_user(user: User):
    f = open('src/dummy_data.json', 'r+')
    data = json.load(f)
    new_user = user.dict()
    for u in data['users']:
        if new_user['userid'] == u['userid']:
            return 'there was an User in the list, try another Id. For example: User Id {0}'.format(len(data['users'])+1)
    data['users'].append(new_user)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.close()
    return user


def update_user(userid, username, age):
    f = open("src/dummy_data.json", "r+")
    data = json.load(f)

    for user in data['users']:
        print(type(user['userid']))
        if userid == user['userid']:
            user['userid'] = userid
            user['username'] = username
            user['age'] = age

    f.seek(0)
    json.dump(data, f, indent=4)
    f.close()
    return
