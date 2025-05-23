from fastapi import APIRouter , Depends 
from Models.user import users , base_users , user_func , oauth2_scheme
from sqlmodel import Session
from Services.db import db_session
from fastapi.responses import RedirectResponse
from fastapi.security import  OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/sign_up")
async def sign_up(user:users,session : Session = Depends(db_session)) -> RedirectResponse:
    user.signin(session)
    return RedirectResponse(url="")

@router.post("/log_in")
async def log_in(form = Depends(OAuth2PasswordRequestForm),session : Session = Depends(db_session)) -> dict:
    user = base_users(form.username,form.password)
    return user.login_user(session)

@router.post("/log_out")
async def log_out(token : str = Depends(oauth2_scheme),session : Session = Depends(db_session)) -> RedirectResponse:
    username = user_func.verification(token,["customer","admin"],session)
    user_func.logout(username,session)
    return RedirectResponse(url="")

@router.put("/change_password")
async def change_password(password:str,token:str = Depends(oauth2_scheme),session : Session = Depends(db_session)) -> RedirectResponse:
    username = user_func.verification(token,["customer","admin"],session)
    user_func.update_password(session,username,password)
    return RedirectResponse(url="")


@router.delete("/delete_user")
async def delete_user(token:str = Depends(oauth2_scheme),session : Session = Depends(db_session))-> RedirectResponse:
    username = user_func.verification(token,["customer","admin"],session)
    user_func.delete_account(session,username)
    return RedirectResponse(url="")
