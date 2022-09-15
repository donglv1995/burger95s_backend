class UserInfoDTO():
    def __init__(self, user_id: int, user_name: str, gender: str , phone: str, is_deleted: str = False) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.gender = gender
        self.phone = phone
        self.is_deleted = is_deleted
    




