from schemas import BaseUser
from handlers.base_handler import BaseHandler

class CreateUserHandler(BaseHandler):
    def __init__(self, users_service):
        self.service = users_service

    def create_user(self, user: BaseUser):
        return self.service.create(user)
