from schemas import BaseUser
from handlers.base_handler import BaseHandler

class UpdateUserHandler(BaseHandler):
    def __init__(self, users_service):
        self.service = users_service

    def update_user(self, user_id: int, user: BaseUser):
        return self.service.update(user_id, user)
