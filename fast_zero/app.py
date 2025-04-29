from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', stautus_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}
