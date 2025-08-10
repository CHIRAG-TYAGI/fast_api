from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

user_db={
    1:{"name":"Alice", "age": 30},
    2:{"name":"Bob", "age": 25}
    }

class User(BaseModel):
    name: str
    age: int

@app.put("/users/{user_id}")
def use_update(user_id: int, user: User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message": "User updated successfully", "user": user_db[user_id]}
       
    else:
        return {"message": "User not found"}    
    
@app.get("/users/{user_id}")
def get_user(user_id: int): 
    if user_id in user_db:
        return {"user": user_db[user_id]}
    else:
        return {"message": "User not found"}    


@app.delete("/user_db/data/v1/delete/{user_id}")    
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}
