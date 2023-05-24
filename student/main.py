import uuid
import uvicorn
import os
from fastapi import FastAPI, Body, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()
 
@app.get("/")
async def main():
    
    return FileResponse("public/index.html")
 
@app.get("/api/users")
def get_people():
    return people
 
@app.get("/api/users/{id}")
def get_person(id):
    # получаем пользователя по id
    person = find_person(id)
    print(person)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person==None:  
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    #если пользователь найден, отправляем его
    return person
 
 
@app.post("/api/users")
def create_person(data  = Body()):
    person = Person(data["name"], data["age"])
    # добавляем объект в список people
    people.append(person)
    return person

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")