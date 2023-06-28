from sqlalchemy.orm import Session
from models import User

class UsersRepository:
    def __init__(self, user_translator):
        self.translator = user_translator

    def get_users(self, db: Session):
        users = db.query(User).all()
        return users

    def get_user(self, db: Session, user_id):
        user = db.query(User).filter(User.id == user_id).one_or_none()
        return user

    def create_user(self, db: Session, plain_user):
        user = self.translator.to_database(plain_user)
        new_user = User(**user)
        db.add(new_user)
        db.commit()
        return self.translator.from_database(new_user)

    def update_user(self, db: Session, user_id, plain_user):
        user = self.translator.to_database(plain_user)
        new_user = {'lname': user.get('lname'), 'fname': user.get('fname')}
        db.query(User).filter(User.id == user_id).update(new_user)
        updated_user = db.query(User).filter(User.id == user_id).one_or_none()
        db.commit()
        return self.translator.from_database(updated_user)

    def delete_user(self, db: Session, user_id):
        existing_user = db.query(User).filter(User.id == user_id).one_or_none()

        if existing_user:
            db.delete(existing_user)
            db.commit()
            return existing_user
