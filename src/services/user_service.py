from ..database.repositories import user_repository
from src.burger95s.models.user_info import  UserInfo
from fastapi import HTTPException, status
from src.burger95s.dto.user_info_dto import UserInfoDTO


# get all keys in order to match with tuple values
# def get_keys():
#     user_keys = ['user_id']
#     keys = list(UserInfo.__fields__.keys())
#     user_keys.extend(keys)
    
#     return user_keys


def convert_to_user_class_DTO(user):
    id, name, gender, phone, deleted = user
    u = UserInfoDTO(id, name, gender, phone, deleted)

    return u



def get_all_users():
    # list of tuple
    users = []

    final_result = []

    try:
        users = user_repository.get_all_users()
        for user in users:
            final_result.append(convert_to_user_class_DTO(user))
        
    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="There are something wrong with the Try statement, please check it !")
        
    return final_result


def get_user_by_id(user_id):
    user = None

    try:
        if int(user_id) <= 0:

            raise ValueError("ID User must be a number bigger than 0, please try again !")

        user = user_repository.get_user_by_id(user_id=user_id)
        user = convert_to_user_class_DTO(user)

    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="There are something with the Try statement, please check it")

    return user

def create_user(user: UserInfo):
    created_user = None

    try:
        created_user = user_repository.create_user(user)

    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="There are something with the Try statement, please check it")

    return created_user

def update_user(user_id, user: UserInfo):
    updated_user = None

    try:
        if int(user_id) <= 0:
            raise ValueError("ID must be greater than 0, please try again !")
        updated_user = user_repository.update_user(user_id, user)

    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="There are something with the Try statement, please check it")

    return updated_user


def delete_user(user_id, is_hard_delete: bool):
    isDeleted_user = None

    try: 
        if int(user_id) <= 0:

            raise ValueError("ID User must be a number bigger than 0, please try again !")

        isDeleted_user = user_repository.delete_user(user_id, is_hard_delete)
    
    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="There are something with the Try statement, please check it")
    
    return isDeleted_user