from re import U
from ..database.repositories import user_repository
from ..burger95s.models.user_info import User


def convert_to_user_model(user):
    # convert from tuple to a dict
    values = {
        key: user[i] for i, key in enumerate(User.__fields__.keys())
    }

    user_base_model = User(**values)

    return user_base_model



def get_all_users():
    # list of tuple values
    users = []

    final_result = []

    try:
        users = user_repository.get_all_users()
        for u in users:
            final_result.append(convert_to_user_model(u))
        
    except Exception as e:
        return e

    return final_result


def get_user_by_id(userid):
    user = None

    try:
        if int(userid) <= 0:

            raise ValueError("ID User must be a number bigger than 0, please try again !")
            
        user = user_repository.get_user_by_id(userid=userid)

    except Exception as e:
        return e

    return convert_to_user_model(user)

def create_user(user: User):
    created_user = None

    try:
        created_user = user_repository.create_user(user)

    except Exception as e:
        return e

    return created_user

def update_user(user: User):
    updated_user = None

    try:
        updated_user = user_repository.update_user(user)

    except Exception as e:
        return e

    return updated_user


def delete_user(userid, is_hard_delete: bool):
    isDeleted_user = None

    try: 
        if int(userid) <= 0:

            raise ValueError("ID User must be a number bigger than 0, please try again !")

        isDeleted_user = user_repository.delete_user(userid, is_hard_delete)
    
    except Exception as e:
        print(e)
    
    return isDeleted_user