import repositry.UserRepository as UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

    def create_user(self, user):
        return self.user_repository.create_user(user)
