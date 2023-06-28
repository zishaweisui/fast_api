from fastapi import FastAPI
from schemas import BaseUser, BaseNote

from structure import (
    get_users_handler, 
    get_user_handler, 
    create_user_handler, 
    update_user_handler, 
    delete_user_handler,
    get_note_handler, 
    create_note_handler, 
    update_note_handler, 
    delete_note_handler
)



app = FastAPI()

@app.get("/users")
def get_users():
    handler = get_users_handler
    return handler.get_users()

@app.post("/users")
def create_user(user: BaseUser):
    handler = create_user_handler
    return handler.create_user(user=user)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    handler = get_user_handler
    return handler.get_user(user_id=user_id)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: BaseUser):
    handler = update_user_handler
    return handler.update_user(user_id=user_id, user=user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    handler = delete_user_handler
    handler.delete_user(user_id=user_id)
    return {"message": "User deleted"}

@app.get("/users/{user_id}/notes/{note_id}")
def get_one_note(user_id: int, note_id: int):
    handler = get_note_handler
    return handler.get_note(note_id=note_id)

@app.post("/users/{user_id}/new")
def create_new_note(user_id: int, note: BaseNote):
    handler = create_note_handler
    content = {'user_id': user_id, 'content': note.content}
    return handler.create_note(note=content)

@app.put("/users/{user_id}/notes/{note_id}")
def update_one_note(user_id: int, note_id: int, note: BaseNote):
    handler = update_note_handler
    return handler.update_note(note_id=note_id, note=note)

@app.delete("/users/{user_id}/notes/{note_id}")
def delete_one_note(user_id: int, note_id: int):
    handler = delete_note_handler
    handler.delete_note(note_id=note_id)
    return {"message": "Note deleted"}
